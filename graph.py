import time
import sys
import os

class graphSymbols:
    line = "─"
    fourtyFiveDegree = "/"
    ninetyDegreeUp = "┘"
    ninetyDegreeRight = "┌"

class graph:
    value = int()
    oldValue = int()
    graphResult = dict()
    data = dict()
    symbols = None
    numbers = list()
    width = 9

    def __init__(self, startingValue: int(), **kwargs): #width: int(9), symbols: graphSymbols()):
        self.value = startingValue
        self.width = 9 # Default value

        # Tinggi graph = 9 line (default)
        if kwargs["width"] != None:
            self.width = kwargs["width"]

        if kwargs["symbols"] != None:
            self.symbols = kwargs["symbols"]
        else:
            symbols = graphSymbols()

        for num in range(int(startingValue - self.width/2) + 1, int(startingValue + self.width/2) + 1):
            self.numbers.append(num)

        self.numbers.reverse()

    def setValue(self, value):
        self.value = value
        
    def calculateGraphic(self):
        nom = int()
        for num in range(int(self.value - self.width/2) + 1, int(self.value + self.width/2) + 1):
            self.numbers[nom] = num
            nom += 1 
        for i in range(len(self.numbers)):
            sys.stdout.write(str(self.numbers[i]) + " |" + "\n")
        sys.stdout.flush()

    def draw(self, stdout_output=True):
        pass

    def getString():
        return str()


if __name__ == "__main__":
    print("TESTING")
    myGraphsSymbols = graphSymbols()
    myGraph = graph(48, width=9, symbols=myGraphsSymbols)
    for a in range(48, 60):
        myGraph.calculateGraphic()
        myGraph.setValue(a)
        time.sleep(0.75)
        os.system("clear")

