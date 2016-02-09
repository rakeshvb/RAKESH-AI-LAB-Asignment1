class Position:
    rowIndex=0
    columnIndex=0
    def __init__(self,rowIndex,columnIndex):
        self.rowIndex=rowIndex
        self.columnIndex=columnIndex
    def __str__(self):
        return self.rowIndex
        return self.columnIndex
    def __repr__(self):
        return self.__str__()