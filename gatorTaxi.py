import sys

#Import all necessary classes from the modules
from Ride import Ride
from minHeap import MinHeap
from minHeap import MHNode
from redBlackTree import RedBlackTree, RBNode

# Function to insert a new ride into the min heap and red-black tree.
def insertRide(ride, heap, node_rbt):
    if node_rbt.getRide(ride.rNo) is not None:
        appendOutput(None, "Duplicate RideNumber", False)
        sys.exit(0) # terminate
        return
    rbtNode = RBNode(None, None)
    # Create a new min heap node with the ride, red-black tree node, and current min heap size + 1.
    minHeapNode = MHNode(ride, rbtNode, heap.currentSize + 1)
    heap.insert(minHeapNode) #insert into min heap
    node_rbt.insert(ride, minHeapNode) #insert into rbt

# Function to update a ride's duration in the min heap and red-black tree.
def updateRide(rNo, newDuration, heap, node_rbt):
    rbtNode = node_rbt.getRide(rNo) # Get the ride from the red-black tree using the ride number.
    if rbtNode is None:
        print("")
    #update element based on duration
    elif newDuration <= rbtNode.ride.tripDuration:
        heap.updateElement(rbtNode.minHeapNode.minHeapIndex, newDuration)
    elif rbtNode.ride.tripDuration < newDuration <= (2 * rbtNode.ride.tripDuration):
        cancelRide(rbtNode.ride.rNo, heap, node_rbt)
        insertRide(Ride(rbtNode.ride.rNo, rbtNode.ride.rCost + 10, newDuration), heap, node_rbt)
    else:
        cancelRide(rbtNode.ride.rNo, heap, node_rbt)

#cancel ride from minHeap and rbt
def cancelRide(ride_number, heap, node_rbt):
    hNode = node_rbt.deleteNode(ride_number)
    if hNode is not None:
        heap.deleteElement(hNode.minHeapIndex)

#get Next Ride with shortest duration from the minHeap
def getNextRide(heap, node_rbt):
    if heap.currentSize != 0:
        popped_rbtNode = heap.pop()
        node_rbt.deleteNode(popped_rbtNode.ride.rNo)
        appendOutput(popped_rbtNode.ride, "", False) #add to the output
    else:
        appendOutput(None, "No active ride requests", False)

#append to the output file
def appendOutput(ride, msg, lst):
    file = open("output_file.txt", "a")
    if ride is None:
        file.write(msg + "\n")
    else:
        msg = ""
        if not lst:
            msg += ("(" + str(ride.rNo) + "," + str(ride.rCost) + "," + str(ride.tripDuration) + ")\n")
        else:
            if len(ride) == 0:
                msg += "(0,0,0)\n" # if ride list is empty
            for i in range(len(ride)):
                if i != len(ride) - 1:
                    msg = msg + ("(" + str(ride[i].rNo) + "," + str(ride[i].rCost) + "," + str(
                        ride[i].tripDuration) + "),")
                else:
                    msg = msg + ("(" + str(ride[i].rNo) + "," + str(ride[i].rCost) + "," + str(
                        ride[i].tripDuration) + ")\n")

        file.write(msg) # write message to output file
    file.close()

# print single rides details
def printRide(rNo, node_rbt):
    result = node_rbt.getRide(rNo)
    if result is None:
        appendOutput(Ride(0, 0, 0), "", False) #add to the output
    else:
        appendOutput(result.ride, "", False)#add to the output

#print ride details in a given range
def printRides(l, h, node_rbt):
    lst = node_rbt.getRidesInRange(l, h)
    appendOutput(lst, "", True)#add to the output


if __name__ == "__main__":
    # create new minHeap and RBT
    heap = MinHeap()
    rbtNode = RedBlackTree()
    file = open("output_file.txt", "w")
    file.close()
    input_file = sys.argv[1]
    file = open(input_file, "r") # reading and processing the input based on Insert/Print/UpdateTrip/GetNextRide/CancelRide
    for currLine in file.readlines():
        no = []
        for var_num in currLine[currLine.index("(") + 1:currLine.index(")")].split(","):
            if var_num != '':
                no.append(int(var_num))
        if "Insert" in currLine:
            insertRide(Ride(no[0], no[1], no[2]), heap, rbtNode)
        elif "Print" in currLine:
            if len(no) == 1:
                printRide(no[0], rbtNode)
            elif len(no) == 2:
                printRides(no[0], no[1], rbtNode)
        elif "UpdateTrip" in currLine:
            updateRide(no[0], no[1], heap, rbtNode)
        elif "GetNextRide" in currLine:
            getNextRide(heap, rbtNode)
        elif "CancelRide" in currLine:
            cancelRide(no[0], heap, rbtNode)

