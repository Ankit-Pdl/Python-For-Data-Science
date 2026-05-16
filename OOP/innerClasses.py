
# class University :
#     def __init__(self):
#         self.name = "Parent College"

#     class Oxford:
#       def __init__(self):
#        self.name = "Child College"

#       def display(self):
#          print("Hello form Oxford college")    

# uni = University()
# oxf = uni.Oxford()
# oxf.display()



#! practical example

class Car:
    def __init__(self,brand,model):
        self.brand =brand
        self.model = model
        self.engine = self.Engine()
    class Engine:
        def __init__(self):
            self.status = "OFF"
        def start_Engine(self):
            self.status == "ONN"
            print("Engine Runnig!")
        def stop_Engine(self):
            self.status == "OFF"
            print("Engine Stopped!")
    def driving(self):
        if self.engine.status =="ONN":
            print(f'Driving {self.brand} {self.model} model')
        else:
            print("Start the engine first!")


car = Car("Corolla",2025)
car.driving()
car.engine.start_Engine()
