class DatasetModifier():
    
    def __init__(self,batchSize):
        self.startIndex = 0
        self.batchSize = batchSize
        self.endIndex = batchSize
    
    def updateIndices(self):
        self.startIndex = self.endIndex
        self.endIndex = self.endIndex + self.batchSize
    
    def getDataset(self):
        print(*list(range(self.startIndex,self.endIndex)),sep= " ")
        self.updateIndices()

if __name__ == "__main__":
    objDatasetModifer = DatasetModifier(5)

    objDatasetModifer.getDataset()
    objDatasetModifer.getDataset()
    objDatasetModifer.getDataset()

    