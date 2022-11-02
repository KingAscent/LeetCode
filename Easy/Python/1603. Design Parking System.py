class ParkingSystem(object):
    carSpots = []
    
    
    def __init__(self, big, medium, small):
        global carSpots
        carSpots = [big, medium, small]
        

    def addCar(self, carType):
        # If there are no parking spots available for the car's size,
        # return false
        if ((carType == 1 and carSpots[0] == 0) or 
            (carType == 2 and carSpots[1] == 0) or
            (carType == 3 and carSpots[2] == 0)):
            return False
        
        # If there is a parking spot available, subtract 1 from its
        # size availability
        if(carType == 1):
            carSpots[0] -= 1
        if(carType == 2):
            carSpots[1] -= 1
        if(carType == 3):
            carSpots[2] -= 1
        
        # The car has been parked, return true
        return True
