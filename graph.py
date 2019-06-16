import time
import sys

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
    
    def __init__(self, startingValue: int(), **kwargs): #width: int(9), symbols: graphSymbols()):
        self.value = startingValue
        width = 9 # Default value

        # Tinggi graph = 9 line (default)
        if kwargs["width"] != None:
            width = kwargs["width"]

        if kwargs["symbols"] != None:
            self.symbols = kwargs["symbols"]
        else:
            symbols = graphSymbols()

        for num in range(int(startingValue - width/2) + 1, int(startingValue + width/2) + 1):
            self.numbers.append(num)

        self.numbers.reverse()

    def setValue(self, value):
        self.value = value
        
    def calculateGraphic(self):
        sys.stdout.write("\r")
        for i in range(len(self.numbers)):
            sys.stdout.write(str(self.numbers[i]) + " |" + "\n")
        sys.stdout.flush()

    def draw(self, stdout_output=True):
        pass


if __name__ == "__main__":
    print("TESTING")
    myGraphsSymbols = graphSymbols()
    myGraph = graph(48, width=9, symbols=myGraphsSymbols)
    myGraph.calculateGraphic()

