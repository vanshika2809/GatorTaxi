class Ride:
    def __init__(self, rNo, rCost, tripDuration):
        self.rNo = rNo # ride number (identifies the ride)
        self.rCost = rCost # ride cost
        self.tripDuration = tripDuration #duration of the ride

    #compare two rides 
    def comparator(self, diffRide):
        if self.rCost < diffRide.rCost:
            return True
        elif self.rCost > diffRide.rCost:
            return False
        elif self.rCost == diffRide.rCost: # if the ride cost is same, compare based on duration
            if self.tripDuration > diffRide.tripDuration:
                return False
            else:
                return True
