import os
import json
import random
import time
from datetime import datetime, date
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# ─── File Paths ───────────────────────────────────────────────────────────────
NOTES_FILE = "notes.json"
STREAK_FILE = "streak.json"
QUOTES_FILE = "quotes.json"

# ─── ANSI Color Codes ─────────────────────────────────────────────────────────
class Colors:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"
    BG_BLUE = "\033[44m"
    BG_GREEN = "\033[42m"
    BG_MAGENTA = "\033[45m"

def colorize(text, color):
    return f"{color}{text}{Colors.RESET}"

# ─── File I/O Functions ───────────────────────────────────────────────────────
def load_json(filepath, default):
    if os.path.exists(filepath):
        with open(filepath, "r") as f:
            return json.load(f)
    return default

def save_json(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f, indent=2)

# ─── Notes Functions ──────────────────────────────────────────────────────────
def load_notes():
    return load_json(NOTES_FILE, [])

def save_notes(notes):
    save_json(NOTES_FILE, notes)

def add_note():
    print(colorize("\n📝  ADD STUDY NOTE", Colors.CYAN + Colors.BOLD))
    print(colorize("─" * 40, Colors.CYAN))
    subject = input(colorize("  Subject/Topic : ", Colors.YELLOW)).strip()
    if not subject:
        print(colorize("  ⚠  Subject cannot be empty.", Colors.RED))
        return
    print(colorize("  Note Content  : ", Colors.YELLOW))
    content = input("  → ").strip()
    if not content:
        print(colorize("  ⚠  Content cannot be empty.", Colors.RED))
        return

    notes = load_notes()
    note = {
        "id": len(notes) + 1,
        "subject": subject,
        "content": content,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
    }
    notes.append(note)
    save_notes(notes)
    print(colorize(f"\n  ✅  Note saved successfully! (ID: {note['id']})", Colors.GREEN))

def view_notes():
    notes = load_notes()
    print(colorize("\n📚  ALL STUDY NOTES", Colors.BLUE + Colors.BOLD))
    print(colorize("─" * 60, Colors.BLUE))
    if not notes:
        print(colorize("  No notes found. Start adding some!", Colors.YELLOW))
        return
    for note in notes:
        print(colorize(f"  [{note['id']}] {note['subject']}", Colors.CYAN + Colors.BOLD))
        print(f"      {note['content']}")
        print(colorize(f"      🕐 {note['timestamp']}", Colors.MAGENTA))
        print(colorize("  " + "·" * 56, Colors.BLUE))

def search_notes():
    keyword = input(colorize("\n🔍  Enter keyword to search: ", Colors.YELLOW)).strip().lower()
    if not keyword:
        print(colorize("  ⚠  Keyword cannot be empty.", Colors.RED))
        return
    notes = load_notes()
    results = [
        n for n in notes
        if keyword in n["subject"].lower() or keyword in n["content"].lower()
    ]
    print(colorize(f"\n🔎  SEARCH RESULTS for '{keyword}'", Colors.CYAN + Colors.BOLD))
    print(colorize("─" * 60, Colors.CYAN))
    if not results:
        print(colorize("  No matching notes found.", Colors.RED))
        return
    for note in results:
        print(colorize(f"  [{note['id']}] {note['subject']}", Colors.GREEN + Colors.BOLD))
        print(f"      {note['content']}")
        print(colorize(f"      🕐 {note['timestamp']}", Colors.MAGENTA))
        print(colorize("  " + "·" * 56, Colors.CYAN))
    print(colorize(f"\n  Found {len(results)} result(s).", Colors.GREEN))

def delete_note():
    view_notes()
    notes = load_notes()
    if not notes:
        return
    try:
        note_id = int(input(colorize("\n🗑  Enter Note ID to delete: ", Colors.RED)))
        note_to_delete = next((n for n in notes if n["id"] == note_id), None)
        if not note_to_delete:
            print(colorize("  ⚠  Note ID not found.", Colors.RED))
            return
        confirm = input(colorize(f"  Delete '{note_to_delete['subject']}'? (y/n): ", Colors.YELLOW)).lower()
        if confirm == "y":
            notes = [n for n in notes if n["id"] != note_id]
            save_notes(notes)
            print(colorize("  ✅  Note deleted.", Colors.GREEN))
        else:
            print(colorize("  Cancelled.", Colors.YELLOW))
    except ValueError:
        print(colorize("  ⚠  Please enter a valid number.", Colors.RED))

# ─── Streak Tracking ──────────────────────────────────────────────────────────
def update_streak():
    """Track daily study streak using saved dates."""
    streak_data = load_json(STREAK_FILE, {"last_date": None, "streak": 0, "longest": 0})
    today = str(date.today())

    if streak_data["last_date"] == today:
        return streak_data["streak"]  # Already logged today

    yesterday = str(date.fromordinal(date.today().toordinal() - 1))
    if streak_data["last_date"] == yesterday:
        streak_data["streak"] += 1
    else:
        streak_data["streak"] = 1  # Reset if gap in days

    streak_data["last_date"] = today
    streak_data["longest"] = max(streak_data["longest"], streak_data["streak"])
    save_json(STREAK_FILE, streak_data)
    return streak_data["streak"]

def show_streak():
    streak_data = load_json(STREAK_FILE, {"last_date": None, "streak": 0, "longest": 0})
    streak = streak_data.get("streak", 0)
    longest = streak_data.get("longest", 0)
    print(colorize("\n🔥  STUDY STREAK", Colors.YELLOW + Colors.BOLD))
    print(colorize("─" * 40, Colors.YELLOW))
    fire = "🔥" * min(streak, 10)
    print(f"  Current Streak : {colorize(str(streak) + ' day(s)', Colors.GREEN + Colors.BOLD)} {fire}")
    print(f"  Longest Streak : {colorize(str(longest) + ' day(s)', Colors.CYAN + Colors.BOLD)}")
    print(f"  Last Studied   : {colorize(streak_data.get('last_date', 'Never'), Colors.MAGENTA)}")

# ─── Quiz Generator ───────────────────────────────────────────────────────────
def generate_quiz():
    """Generate a fill-in-the-blank style quiz from saved notes."""
    notes = load_notes()
    if len(notes) < 2:
        print(colorize("\n  ⚠  Add at least 2 notes to generate a quiz!", Colors.YELLOW))
        return

    print(colorize("\n🎯  QUICK QUIZ", Colors.MAGENTA + Colors.BOLD))
    print(colorize("─" * 60, Colors.MAGENTA))
    print(colorize("  Answer these questions from your notes:\n", Colors.CYAN))

    sample = random.sample(notes, min(3, len(notes)))
    score = 0

    for i, note in enumerate(sample, 1):
        print(colorize(f"  Q{i}. What do you know about: ", Colors.YELLOW) +
              colorize(note["subject"] + "?", Colors.WHITE + Colors.BOLD))
        input(colorize("  Your answer (press Enter when done): ", Colors.CYAN))
        print(colorize("  ✅  Correct Answer from your notes:", Colors.GREEN))
        print(f"      {note['content']}\n")
        mark = input(colorize("  Did you get it right? (y/n): ", Colors.YELLOW)).lower()
        if mark == "y":
            score += 1
        print(colorize("  " + "·" * 56, Colors.MAGENTA))

    print(colorize(f"\n  🏆  Quiz complete! Score: {score}/{len(sample)}", Colors.GREEN + Colors.BOLD))

# ─── Motivational Quotes ──────────────────────────────────────────────────────
DEFAULT_QUOTES = [
    "The secret of getting ahead is getting started. — Mark Twain",
    "It always seems impossible until it's done. — Nelson Mandela",
    "Push yourself, because no one else is going to do it for you.",
    "Success is the sum of small efforts, repeated daily.",
    "Don't watch the clock; do what it does. Keep going. — Sam Levenson",
    "Learning is not attained by chance; it must be sought with ardor. — Abigail Adams",
    "The beautiful thing about learning is nobody can take it away from you.",
    "Believe you can and you're halfway there. — Theodore Roosevelt",
]

def show_quote():
    quotes = load_json(QUOTES_FILE, DEFAULT_QUOTES)
    quote = random.choice(quotes)
    print(colorize("\n✨  MOTIVATION BOOST", Colors.GREEN + Colors.BOLD))
    print(colorize("─" * 60, Colors.GREEN))
    print(colorize(f'\n  "{quote}"\n', Colors.YELLOW))

# ─── Statistics Dashboard ─────────────────────────────────────────────────────
def show_statistics():
    notes = load_notes()
    streak_data = load_json(STREAK_FILE, {"streak": 0, "longest": 0, "last_date": "N/A"})

    # Count subjects
    subjects = {}
    for note in notes:
        subjects[note["subject"]] = subjects.get(note["subject"], 0) + 1
    top_subject = max(subjects, key=subjects.get) if subjects else "N/A"

    print(colorize("\n📊  STATISTICS DASHBOARD", Colors.BLUE + Colors.BOLD))
    print(colorize("═" * 50, Colors.BLUE))
    print(colorize("  📝  Notes", Colors.CYAN + Colors.BOLD))
    print(f"      Total Notes    : {colorize(str(len(notes)), Colors.GREEN + Colors.BOLD)}")
    print(f"      Unique Topics  : {colorize(str(len(subjects)), Colors.GREEN + Colors.BOLD)}")
    print(f"      Top Subject    : {colorize(top_subject, Colors.YELLOW + Colors.BOLD)}")
    print(colorize("  🔥  Streaks", Colors.CYAN + Colors.BOLD))
    print(f"      Current Streak : {colorize(str(streak_data['streak']) + ' days', Colors.GREEN + Colors.BOLD)}")
    print(f"      Best Streak    : {colorize(str(streak_data['longest']) + ' days', Colors.YELLOW + Colors.BOLD)}")
    print(f"      Last Studied   : {colorize(str(streak_data.get('last_date', 'N/A')), Colors.MAGENTA)}")

    if subjects:
        print(colorize("\n  📈  Notes per Subject:", Colors.CYAN + Colors.BOLD))
        for subj, count in sorted(subjects.items(), key=lambda x: -x[1]):
            bar = "█" * count
            print(f"      {subj[:20]:<22} {colorize(bar, Colors.BLUE)} {count}")
    print(colorize("═" * 50, Colors.BLUE))

# ─── Study Timer ──────────────────────────────────────────────────────────────
def study_timer():
    print(colorize("\n⏱  STUDY TIMER", Colors.CYAN + Colors.BOLD))
    print(colorize("─" * 40, Colors.CYAN))
    try:
        minutes = float(input(colorize("  Enter study duration (minutes): ", Colors.YELLOW)))
        if minutes <= 0:
            raise ValueError
    except ValueError:
        print(colorize("  ⚠  Please enter a valid positive number.", Colors.RED))
        return

    total_seconds = int(minutes * 60)
    print(colorize(f"\n  🚀  Timer started for {minutes} minute(s)! Focus up!\n", Colors.GREEN))

    start = time.time()
    try:
        while True:
            elapsed = int(time.time() - start)
            remaining = total_seconds - elapsed
            if remaining <= 0:
                break
            mins, secs = divmod(remaining, 60)
            timer_str = f"  ⏳  Remaining: {mins:02d}:{secs:02d}"
            print(colorize(timer_str, Colors.YELLOW), end="\r")
            time.sleep(1)
    except KeyboardInterrupt:
        print(colorize("\n\n  ⏹  Timer stopped early.", Colors.RED))
        return

    print(colorize("\n\n  🎉  Time's up! Great study session!", Colors.GREEN + Colors.BOLD))
    update_streak()

# ─── Menu UI ──────────────────────────────────────────────────────────────────
def print_header():
    os.system("cls" if os.name == "nt" else "clear")
    streak = update_streak()
    print(colorize("╔══════════════════════════════════════════════╗", Colors.BLUE + Colors.BOLD))
    print(colorize("║       📖  STUDY ASSISTANT  PRO  📖           ║", Colors.BLUE + Colors.BOLD))
    print(colorize("╚══════════════════════════════════════════════╝", Colors.BLUE + Colors.BOLD))
    print(colorize(f"  🔥 Streak: {streak} day(s)   📅 {date.today()}", Colors.YELLOW))
    print()

def print_menu():
    options = [
        ("1", "📝  Add Study Note"),
        ("2", "📚  View All Notes"),
        ("3", "🔍  Search Notes"),
        ("4", "🗑  Delete a Note"),
        ("5", "🔥  View Study Streak"),
        ("6", "🎯  Take a Quiz"),
        ("7", "✨  Motivational Quote"),
        ("8", "📊  Statistics Dashboard"),
        ("9", "⏱  Study Timer"),
        ("0", "🚪  Exit"),
    ]
    print(colorize("  ┌─────────────────────────────────────────┐", Colors.CYAN))
    print(colorize("  │              MAIN MENU                  │", Colors.CYAN + Colors.BOLD))
    print(colorize("  ├─────────────────────────────────────────┤", Colors.CYAN))
    for key, label in options:
        print(colorize(f"  │  [{key}]  {label:<35}│", Colors.CYAN))
    print(colorize("  └─────────────────────────────────────────┘", Colors.CYAN))

def main():
    # Save default quotes on first run
    if not os.path.exists(QUOTES_FILE):
        save_json(QUOTES_FILE, DEFAULT_QUOTES)

    actions = {
        "1": add_note,
        "2": view_notes,
        "3": search_notes,
        "4": delete_note,
        "5": show_streak,
        "6": generate_quiz,
        "7": show_quote,
        "8": show_statistics,
        "9": study_timer,
    }

    while True:
        print_header()
        print_menu()
        choice = input(colorize("\n  ➤  Enter your choice: ", Colors.WHITE + Colors.BOLD)).strip()

        if choice == "0":
            print(colorize("\n  👋  Keep studying! See you tomorrow!\n", Colors.GREEN + Colors.BOLD))
            break
        elif choice in actions:
            actions[choice]()
            input(colorize("\n  Press Enter to return to menu...", Colors.MAGENTA))
        else:
            print(colorize("  ⚠  Invalid choice. Please select from the menu.", Colors.RED))
            time.sleep(1)

if __name__ == "__main__":
    main()