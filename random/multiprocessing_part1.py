import multiprocessing

def printCube(num):
    """
    function to print cube of a given num
    """

    print("Cube:{}".format(num**3))



def printSquare(num):
    """
    function to print cube of a given num
    """

    print("Cube:{}".format(num**2))

if __name__ == "__main__":

    #creating processes
    p1 = multiprocessing.Process(target=printSquare, args=(10,))
    p2 = multiprocessing.Process(target=printCube, args=(10,))

    #start process 1
    p1.start()
    #start process 2
    p2.start()

    #wait until process 1 is finished
    p1.join()
    #wait until process 2 is finished
    p2.join()

    #both processes finished
    print("Done!")