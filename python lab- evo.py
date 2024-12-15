from abc import ABC, abstractmethod
class Vehicle(ABC):
    def __init__(self, ID, Is_available, fuelData, DistanceData):
        self.__ID = ID
        self.__Is_available = Is_available  
        self.__fuelData = fuelData
        self.__DistanceData = DistanceData 

    @abstractmethod
    def calculateFuel(self):
        pass

    def get_DistanceData(self):
        return self.__DistanceData

    def is_available(self):
        return self.__Is_available

    def get_fuelData(self):
        return self.__fuelData

class Car(Vehicle):
    def __init__(self, ID, Is_available, fuelData, DistanceData):
        super().__init__(ID, Is_available, fuelData, DistanceData)

    def calculateFuel(self):
        return self.get_DistanceData() * 10

    def rent(self):
        print("Car rented successfully.")

class Bike(Vehicle):
    def __init__(self, ID, Is_available, fuelData, DistanceData, helmet):
        super().__init__(ID, Is_available, fuelData, DistanceData)
        self.helmet = helmet

    def calculateFuel(self):
        return self.get_DistanceData() * 5

    def rent(self):
        print("Bike rented successfully.")
        if self.helmet:
            print("Helmet is provided for safety.")

def output():
    car = Car(ID="CAR123", Is_available=True, fuelData="Full Tank", DistanceData=50)
    print("Rent Car:", car.calculateFuel())
    car.rent()

    print("\n")

    bike = Bike(ID="BIKE456", Is_available=True, fuelData="Half Tank", DistanceData=30, helmet=True)
    print("Rent Bike:", bike.calculateFuel())
    bike.rent()

output()
