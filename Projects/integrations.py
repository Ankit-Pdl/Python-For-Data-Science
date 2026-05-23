"""
integration_solver.py
=====================
Numerical integration in pure (vanilla) Python — no NumPy, no SciPy.

Supported methods
-----------------
1. Rectangle (midpoint) rule
2. Trapezoidal rule
3. Simpson's 1/3 rule
4. Simpson's 3/8 rule
5. Gaussian quadrature (5-point Legendre)
6. Adaptive Simpson's method (automatic step refinement)
7. Monte Carlo integration (for fun / high dimensions)

Usage
-----
Run the file directly for a demo:
    python integration_solver.py

Or import the functions into your own code:
    from integration_solver import integrate
"""

import math
import random


# ---------------------------------------------------------------------------
# Core integration methods
# ---------------------------------------------------------------------------

def _midpoint(f, a, b, n):
    """Rectangle (midpoint) rule with n sub-intervals."""
    h = (b - a) / n
    total = 0.0
    for i in range(n):
        mid = a + h * (i + 0.5)
        total += f(mid)
    return h * total


def _trapezoidal(f, a, b, n):
    """Trapezoidal rule with n sub-intervals."""
    h = (b - a) / n
    total = f(a) + f(b)
    for i in range(1, n):
        total += 2 * f(a + i * h)
    return (h / 2) * total


def _simpson_13(f, a, b, n):
    """
    Simpson's 1/3 rule with n sub-intervals.
    n must be even; if odd it is incremented by 1.
    """
    if n % 2 != 0:
        n += 1
    h = (b - a) / n
    total = f(a) + f(b)
    for i in range(1, n):
        coeff = 4 if i % 2 != 0 else 2
        total += coeff * f(a + i * h)
    return (h / 3) * total


def _simpson_38(f, a, b, n):
    """
    Simpson's 3/8 rule with n sub-intervals.
    n must be a multiple of 3; adjusted upward if not.
    """
    if n % 3 != 0:
        n += 3 - (n % 3)
    h = (b - a) / n
    total = f(a) + f(b)
    for i in range(1, n):
        coeff = 3 if i % 3 != 0 else 2
        total += coeff * f(a + i * h)
    return (3 * h / 8) * total


# 5-point Gauss–Legendre nodes and weights on [-1, 1]
_GL5_NODES = [
    -0.9061798459386640,
    -0.5384693101056831,
     0.0,
     0.5384693101056831,
     0.9061798459386640,
]
_GL5_WEIGHTS = [
    0.2369268850561891,
    0.4786286704993665,
    0.5688888888888889,
    0.4786286704993665,
    0.2369268850561891,
]

def _gauss_legendre(f, a, b, n):
    """
    5-point Gauss–Legendre quadrature applied over n panels.
    Very accurate for smooth functions.
    """
    h = (b - a) / n
    total = 0.0
    for k in range(n):
        x0 = a + k * h
        x1 = x0 + h
        mid = (x0 + x1) / 2
        half = h / 2
        for node, weight in zip(_GL5_NODES, _GL5_WEIGHTS):
            total += weight * f(mid + half * node)
    return half * total  # half == h/2 for last panel; always correct


def _adaptive_simpson(f, a, b, tol, depth, max_depth):
    """Recursive adaptive Simpson's method."""
    c = (a + b) / 2
    h = b - a
    fa, fb, fc = f(a), f(b), f(c)
    s_whole = (h / 6) * (fa + 4 * fc + fb)
    d = (a + c) / 2
    e = (c + b) / 2
    fd, fe = f(d), f(e)
    s_left  = (h / 12) * (fa + 4 * fd + fc)
    s_right = (h / 12) * (fc + 4 * fe + fb)
    delta = s_left + s_right - s_whole
    if depth >= max_depth or abs(delta) <= 15 * tol:
        return s_left + s_right + delta / 15
    return (_adaptive_simpson(f, a, c, tol / 2, depth + 1, max_depth) +
            _adaptive_simpson(f, c, b, tol / 2, depth + 1, max_depth))


def _monte_carlo(f, a, b, n):
    """Simple Monte Carlo integration using n random samples."""
    total = 0.0
    for _ in range(n):
        x = a + random.random() * (b - a)
        total += f(x)
    return (b - a) * total / n


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def integrate(f, a, b,
              method="simpson",
              n=1000,
              tol=1e-6,
              max_depth=50,
              seed=None):
    """
    Numerically integrate f(x) over [a, b].

    Parameters
    ----------
    f        : callable  — the function to integrate
    a, b     : float     — lower and upper limits
    method   : str       — one of:
                  'midpoint'   | 'rectangle'
                  'trapezoid'  | 'trapezoidal'
                  'simpson'    | 'simpson13'   (default)
                  'simpson38'
                  'gauss'      | 'gaussian'
                  'adaptive'
                  'montecarlo' | 'monte_carlo'
    n        : int       — number of sub-intervals / samples
    tol      : float     — tolerance for adaptive method
    max_depth: int       — max recursion depth for adaptive method
    seed     : int|None  — random seed for Monte Carlo

    Returns
    -------
    float — the approximate definite integral
    """
    method = method.lower().replace(" ", "").replace("-", "")

    if method in ("midpoint", "rectangle"):
        return _midpoint(f, a, b, n)
    elif method in ("trapezoid", "trapezoidal"):
        return _trapezoidal(f, a, b, n)
    elif method in ("simpson", "simpson13", "simpsons"):
        return _simpson_13(f, a, b, n)
    elif method == "simpson38":
        return _simpson_38(f, a, b, n)
    elif method in ("gauss", "gaussian", "gausslegendre"):
        return _gauss_legendre(f, a, b, n)
    elif method == "adaptive":
        return _adaptive_simpson(f, a, b, tol, 0, max_depth)
    elif method in ("montecarlo", "monte_carlo"):
        if seed is not None:
            random.seed(seed)
        return _monte_carlo(f, a, b, n)
    else:
        raise ValueError(f"Unknown method: '{method}'. "
                         "Choose from: midpoint, trapezoid, simpson, "
                         "simpson38, gauss, adaptive, montecarlo.")


# ---------------------------------------------------------------------------
# Convenience: compare all methods side-by-side
# ---------------------------------------------------------------------------

def compare_methods(f, a, b, exact=None, n=1000):
    """
    Print a comparison table of all integration methods.

    Parameters
    ----------
    f     : callable — function to integrate
    a, b  : float    — integration limits
    exact : float    — known exact value (optional, for error column)
    n     : int      — sub-intervals / samples
    """
    methods = [
        ("Midpoint",      "midpoint"),
        ("Trapezoidal",   "trapezoid"),
        ("Simpson 1/3",   "simpson"),
        ("Simpson 3/8",   "simpson38"),
        ("Gauss-Legendre","gauss"),
        ("Adaptive",      "adaptive"),
        ("Monte Carlo",   "montecarlo"),
    ]

    header = f"{'Method':<18} {'Result':>20}"
    if exact is not None:
        header += f"  {'Abs Error':>14}"
    print(header)
    print("-" * len(header))

    for name, key in methods:
        result = integrate(f, a, b, method=key, n=n, seed=42)
        row = f"{name:<18} {result:>20.12f}"
        if exact is not None:
            row += f"  {abs(result - exact):>14.2e}"
        print(row)

    if exact is not None:
        print(f"\n{'Exact value':<18} {exact:>20.12f}")


# ---------------------------------------------------------------------------
# Demo
# ---------------------------------------------------------------------------

if __name__ == "__main__":

    print("=" * 60)
    print(" Numerical Integration Solver — Vanilla Python")
    print("=" * 60)

    # --- Example 1: ∫₀^π sin(x) dx  = 2 ---
    print("\nExample 1:  ∫₀^π  sin(x) dx  (exact = 2)\n")
    compare_methods(math.sin, 0, math.pi, exact=2.0, n=100)

    # --- Example 2: ∫₀^1 x² dx = 1/3 ---
    print("\nExample 2:  ∫₀¹  x²  dx  (exact = 1/3)\n")
    compare_methods(lambda x: x**2, 0, 1, exact=1/3, n=100)

    # --- Example 3: ∫₁^e ln(x) dx = 1 ---
    print("\nExample 3:  ∫₁^e  ln(x) dx  (exact = 1)\n")
    compare_methods(math.log, 1, math.e, exact=1.0, n=100)

    # --- Example 4: ∫₀^1 e^(-x²) dx  (no closed form — Gaussian integral) ---
    import math
    exact_gauss = math.sqrt(math.pi) / 2 * math.erf(1)   # ≈ 0.7468241328...
    print("\nExample 4:  ∫₀¹  e^(-x²) dx  (exact ≈ 0.746824...)\n")
    compare_methods(lambda x: math.exp(-x**2), 0, 1,
                    exact=exact_gauss, n=100)

    # --- Quick single-method usage ---
    print("\n--- Single method usage ---")
    result = integrate(math.sin, 0, math.pi, method="adaptive")
    print(f"Adaptive Simpson ∫₀^π sin(x) dx = {result:.15f}")

    result = integrate(lambda x: x**3 - 2*x + 1, -1, 2,
                       method="gauss", n=10)
    print(f"Gauss-Legendre  ∫₋₁² (x³-2x+1) dx = {result:.15f}")
    print(f"  (exact = {(2**4/4 - 2**2 + 2) - ((-1)**4/4 - 2*(-1)**2/2 + (-1)):.15f})")