class ParkingSystem {
    int[] carSpots = new int[3];
    
    public ParkingSystem(int big, int medium, int small) {
        carSpots[0] = big;
        carSpots[1] = medium;
        carSpots[2] = small;
        
    }
    
    public boolean addCar(int carType) {
        // If there are no parking spots available for the car's size,
        // return false
        if(carType == 1 && carSpots[0] == 0 ||
        carType == 2 && carSpots[1] == 0 ||
        carType == 3 && carSpots[2] == 0)
            return false;
        
        // If there is a parking spot available, subtract 1 from its
        // size availability
        if(carType == 1)
            carSpots[0]--;
        if(carType == 2)
            carSpots[1]--;
        if(carType == 3)
            carSpots[2]--;
        
        // The car has been parked, return true
        return true;
    }
}
