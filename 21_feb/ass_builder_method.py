class Engine:
    def __init__(self, horsepowers):
        self.horsepower = horsepowers

class Body:
    def __init__(self, type):
        self.type = type

class Wheel:
    def __init__(self, width):
        self.width = width

class Car:
    def __init__(self):
        self.engine = None 
        self.body = None
        self.wheel = None

    def specification(self):
        print(f" Engine: {self.engine.horsepower} \n Body: {self.body.type} \n Wheel: {self.wheel.width}")

# ferrari = Car()
# ferrari.engine = Engine("1500")
# ferrari.body = Body("sports")
# ferrari.wheel = Wheel("21")

# print(ferrari.specification())

class CarBuilder:
    def add_body(self):
        pass
    
    def add_engine(self):
        pass
    
    def add_wheel(self):
        pass
    
    def build(self):
        pass

class FerrariBuild(CarBuilder):
    def __init__(self):
        self.car = Car()

    def add_body(self):
        body = Body("Sports")
        self.car.body = body
        return self
    
    def add_wheels(self):
        wheel = Wheel("21'")
        self.car.wheel = wheel
        return self
    
    def add_engine(self):
        engine = Engine("1500")
        self.car.engine = engine
        return self

    def build(self):
        return self.car
    
class Director:
    def __init__(self, car_builder):
        self.car_builder = car_builder

    def get_car(self):
        # method chaining
        
        """
        self.car_builder ==> FerrariBuild()
        FerrariBuild().add_boy() ==> return self ==> FerrariBuild()
        FerrariBuild().add_engine() ==> return self ==> FerrariBuild()
        FerrariBuild().add_wheels() ==> return self ==> FerrariBuild()
        FerrariBuild().build() ==> return self.car 
        Car().specification()
        """
        
        return self.car_builder.add_body().add_engine().add_wheels().build()
    
def main():
    ferrari_build = FerrariBuild()
    director = Director(ferrari_build)
    car = director.get_car()

    car.specification()

if __name__=="__main__":
    main()