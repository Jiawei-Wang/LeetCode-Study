class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.med = medium
        self.smo = small
        
    def addCar(self, carType: int) -> bool:
        if carType == 1:
            self.big -= 1
            return False if self.big < 0 else True
        elif carType == 2:
            self.med -= 1
            return False if self.med < 0 else True
        else:
            self.smo -= 1
            return False if self.smo < 0 else True
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)