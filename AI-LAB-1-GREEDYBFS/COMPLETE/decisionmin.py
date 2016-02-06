from copy import deepcopy
from evaluation_function import evaluation
class nextmin:

	bestGridBoxOutput = []
	negativeInfinity = -100000
	positiveInfinity = 100000

	def __init__(self, parentNodeObject, value,occupied_positions, playerValue, opponentPlayerValue, currentEvalFunctionValue, currentDepthOfNodeValue, playMaxValue, childNodesValues, currentValueValue, currentPositionValue, cutOffDepthValue):
            self.value=value
            self.occupied_positions=occupied_positions
            self.parentNode = None
            self.gridBoxCell = []
            self.player = ""
            self.opponentPlayer = ""
            self.currentEvalFunction = 0
            self.currentDepthOfNode = 0
            self.playMax = True
            self.childNodes = []
            self.currentValue = 0
            self.currentPosition = None
            self.bestChild = None
            self.bestGridBox = []
            self.cutOffDepth = cutOffDepthValue
            #print self.cutOffDepth,"AAAAAAAAAAAAA"
            if(parentNodeObject != None):
                self.parentNode = parentNodeObject
                    
                print parentNodeObject.currentEvalFunction
                    
            self.gridBoxCell = []

            self.player = playerValue
            self.opponentPlayer = opponentPlayerValue
            self.currentEvalFunction = currentEvalFunctionValue
            self.currentDepthOfNode = currentDepthOfNodeValue
            self.playMax = playMaxValue
            for i in range(0, len(childNodesValues)):
                childNodes.append(childNodesValues[i])

            self.currentValue = currentValueValue
            if currentPositionValue != None:
                    
                self.currentPosition = currentPositionValue
                
                self.currentValue = self.value[self.currentPosition[0]][self.currentPosition[1]]
                
                if self.playMax == True and self.parentNode != None:
                
                    i=currentPositionValue[0]
                    j=currentPositionValue[1]
                    self.occupied_positions[i][j] = self.player
                    for k in range(5):
                        for l in range(5):
                            print occupied_positions[k][l],
                        print    
                    if((i!=0 and self.occupied_positions[i-1][j]==self.opponentPlayer) and ((i!=4 and self.occupied_positions[i+1][j]==self.player) or (j!=0 and self.occupied_positions[i][j-1]==self.player) or (j!=4 and self.occupied_positions[i][j+1]==self.player))):
                        self.occupied_positions[i-1][j]=self.player
                    #print occupied_positions[i-1][j]
                    if((i!=4 and self.occupied_positions[i+1][j]==self.opponentPlayer) and ((i!=0 and self.occupied_positions[i-1][j]==self.player) or (j!=0 and self.occupied_positions[i][j-1]==self.player) or (j!=4 and self.occupied_positions[i][j+1]==self.player))):
                        self.occupied_positions[i+1][j]=self.player
                    #print occupied_positions[i+1][j]
                    if((j!=4 and self.occupied_positions[i][j+1]==self.opponentPlayer) and ((i!=4 and self.occupied_positions[i+1][j]==self.player) or (i!=0 and self.occupied_positions[i-1][j]==self.player) or (j!=0 and self.occupied_positions[i][j-1]==self.player) )):
                        self.occupied_positions[i][j+1]=self.player
                    #print occupied_positions[i][j-1]
                    if((j!=0 and self.occupied_positions[i][j-1]==self.opponentPlayer) and ((i!=4 and self.occupied_positions[i+1][j]==self.player)or (i!=0 and self.occupied_positions[i-1][j]==self.player) or (j!=4 and self.occupied_positions[i][j+1]==self.player))):
                        self.occupied_positions[i][j-1]=self.player
                    
                    q=evaluation(self.value,self.occupied_positions,self.player,self.opponentPlayer)
                    self.currentEvalFunction=q.eval()
                    
                    '''
                    enemyPositions = self.getEnemyBoxPositionsAdjacentToTheBox(self.value,self.occupied_positions, currentPositionValue.rowIndex, currentPositionValue.columnIndex, self.player, self.opponentPlayer)
                    for eachEnemyPosition in enemyPositions:
                        self.occupied_positions[eachEnemyPosition.rowIndex][eachEnemyPosition.columnIndex] = self.player
                    
                    playerValue = 0
                    opponentValue = 0
                    for i in range(5):
                        for j in range(5):
                            # print box
                            if self.occupied_positions[i][j] == self.player:
                                playerValue+=self.value[i][j]
                            elif self.occupied_positions[i][j] == self.opponentPlayer:
                                opponentValue+=self.value[i][j]
                    self.currentEvalFunction = playerValue - opponentValue		
                    '''
                    
                    if self.parentNode.currentEvalFunction < self.currentEvalFunction and  self.currentDepthOfNode == self.cutOffDepth:
                            # print "maximizing parent %s " %(self.parentNode.currentPosition)
                        self.parentNode.currentEvalFunction = self.currentEvalFunction
                        self.parentNode.bestChild = currentPositionValue
                        self.parentNode.bestGridBox = deepcopy(self.occupied_positions)
                        nextmin.bestGridBoxOutput = deepcopy(self.occupied_positions)

                            # GameNode.bestGridBoxOutput = []
                            # for i in range(0, len(self.gridBoxCell)):
                            # 	GameNode.bestGridBoxOutput.append([])
                            # 	for j in range(0, len(self.gridBoxCell)):
                            # 		GameNode.bestGridBoxOutput[i].append(self.gridBoxCell[i][j])
                            # self.parentNode.bestChild = deepcopy(self)

                elif self.playMax == False and self.parentNode != None:
                        # print "For %s, current Value %d subtracted from %d " %(opponentPlayerValue, self.currentValue, self.currentEvalFunction) 				
                        # self.currentEvalFunction = parentsOriginalEvalFunction - self.currentValue
                    '''
                    self.occupied_positions[currentPositionValue.rowIndex][currentPositionValue.columnIndex] = self.opponentPlayer
                    enemyPositions = self.getEnemyBoxPositionsAdjacentToTheBox(self.value,self.occupied_positions, currentPositionValue.rowIndex, currentPositionValue.columnIndex, self.opponentPlayer, self.player)
                    for eachEnemyPosition in enemyPositions:
                        self.gridBoxCell[eachEnemyPosition.rowIndex][eachEnemyPosition.columnIndex].occupiedBy = self.opponentPlayer
                            # self.currentEvalFunction += (2 * self.gridBoxCell[eachEnemyPosition.rowIndex][eachEnemyPosition.columnIndex].value)
                    '''
                    i=currentPositionValue[0]
                    j=currentPositionValue[1]
                    self.occupied_positions[i][j] = self.opponentPlayer
                    if((i!=0 and self.occupied_positions[i-1][j]==self.player) and ((i!=4 and self.occupied_positions[i+1][j]==self.opponentPlayer) or (j!=0 and self.occupied_positions[i][j-1]==self.opponentPlayer) or (j!=4 and self.occupied_positions[i][j+1]==self.opponentPlayer))):
                        self.occupied_positions[i-1][j]=self.opponentPlayer
                    #print occupied_positions[i-1][j]
                    if((i!=4 and self.occupied_positions[i+1][j]==self.player) and ((i!=0 and self.occupied_positions[i-1][j]==self.opponentPlayer) or (j!=0 and self.occupied_positions[i][j-1]==self.opponentPlayer) or (j!=4 and self.occupied_positions[i][j+1]==self.opponentPlayer))):
                        self.occupied_positions[i+1][j]=self.opponentPlayer
                    #print occupied_positions[i+1][j]
                    if((j!=4 and self.occupied_positions[i][j+1]==self.player) and ((i!=4 and self.occupied_positions[i+1][j]==self.opponentPlayer) or (i!=0 and self.occupied_positions[i-1][j]==self.opponentPlayer) or (j!=0 and self.occupied_positions[i][j-1]==self.opponentPlayer) )):
                        self.occupied_positions[i][j+1]=self.opponentPlayer
                    #print occupied_positions[i][j-1]
                    if((j!=0 and self.occupied_positions[i][j-1]==self.player) and ((i!=4 and self.occupied_positions[i+1][j]==self.opponentPlayer)or (i!=0 and self.occupied_positions[i-1][j]==self.opponentPlayer) or (j!=4 and self.occupied_positions[i][j+1]==self.opponentPlayer))):
                        self.occupied_positions[i][j-1]=self.opponentPlayer
                    qq=evaluation(self.value,self.occupied_positions,self.player,self.opponentPlayer)
                    self.currentEvalFunction=qq.eval()
                    
                    '''
                    playerValue = 0
                    opponentValue = 0
                    for i in range(5):
                        for j in range(5):
                            if (self.occupied_positions[i][j] == self.player):
                                playerValue+=self.value[i][j]
                            elif (self.occupied_positions[i][j] == self.opponentPlayer):
                                opponentValue+=self.value[i][j]
                    self.currentEvalFunction = playerValue - opponentValue
                    '''
                    if self.parentNode.currentEvalFunction >= self.currentEvalFunction and self.currentDepthOfNode == self.cutOffDepth:
                            # print "minimizing parent %s " %(self.parentNode.currentPosition)
                        self.parentNode.currentEvalFunction = self.currentEvalFunction
                        self.parentNode.bestChild = currentPositionValue
                        self.parentNode.bestGridBox = deepcopy(self.occupied_positions)
                        nextmin.bestGridBoxOutput = deepcopy(self.occupied_positions)
                    
            #if(self.parentNode == None):
                print self
            #else:
            #    print self.parentNode
        '''
	def isThisRaidOrSneak(self, value,occupied_positions, rowIndex, columnIndex, firstPlayerValue, secondPlayerValue):
		raid = False
		positions = []
		# Determine the position above
		if(rowIndex > 0):
			upPosition = Position(0, 0)
			upPosition.rowIndex = rowIndex - 1
			upPosition.columnIndex = columnIndex
			if(occupied_positions[upPosition.rowIndex][upPosition.columnIndex] == firstPlayerValue):
				raid = True

		# Determine the position to the right
		if(columnIndex < 4):
			rightPosition = Position(0, 0)
			rightPosition.rowIndex = rowIndex
			rightPosition.columnIndex = columnIndex + 1
			if(occupied_positions[rightPosition.rowIndex][rightPosition.columnIndex] == firstPlayerValue):
				raid = True

		# Determine the position below
		if(rowIndex < 4):
			bottomPosition = Position(0, 0)
			bottomPosition.rowIndex = rowIndex + 1
			bottomPosition.columnIndex = columnIndex
			if(occupied_positions[bottomPosition.rowIndex][bottomPosition.columnIndex] == firstPlayerValue):
				raid = True

		# Determine the position to the left
		if(columnIndex > 0):
			leftPosition = Position(0, 0)
			leftPosition.rowIndex = rowIndex
			leftPosition.columnIndex = columnIndex - 1
			if(occupied_positions[leftPosition.rowIndex][leftPosition.columnIndex] == firstPlayerValue):
				raid = True

		return raid

	def getEnemyBoxPositionsAdjacentToTheBox(self, value,occupied_positions, rowIndex, columnIndex, firstPlayerValue, secondPlayerValue):
		# print "Checking enemy boxes for "
		# print "[%d, %d]" %(rowIndex, columnIndex)
		raidOrSneak = True
		raidOrSneak = self.isThisRaidOrSneak(value,occupied_positions, rowIndex, columnIndex, firstPlayerValue, secondPlayerValue)

		positions = []
		if(raidOrSneak == True):
			# Determine the position above
			if(rowIndex > 0):
				upPosition = Position(0, 0)
				upPosition.rowIndex = rowIndex - 1
				upPosition.columnIndex = columnIndex
				if(occupied_positions[upPosition.rowIndex][upPosition.columnIndex] == secondPlayerValue):
					positions.append(upPosition)
					# print "up added"

			# Determine the position to the right
			if(columnIndex < 4):
				rightPosition = Position(0, 0)
				rightPosition.rowIndex = rowIndex
				rightPosition.columnIndex = columnIndex + 1
				if(occupied_positions[rightPosition.rowIndex][rightPosition.columnIndex] == secondPlayerValue):
					positions.append(rightPosition)
					# print "right added"

			# Determine the position below
			if(rowIndex < 4):
				bottomPosition = Position(0, 0)
				bottomPosition.rowIndex = rowIndex + 1
				bottomPosition.columnIndex = columnIndex
				if(occupied_positions[bottomPosition.rowIndex][bottomPosition.columnIndex] == secondPlayerValue):
						positions.append(bottomPosition)
						# print "bottom added"

			# Determine the position to the left
			if(columnIndex > 0):
				leftPosition = Position(0, 0)
				leftPosition.rowIndex = rowIndex
				leftPosition.columnIndex = columnIndex - 1
				if(occupied_positions[leftPosition.rowIndex][leftPosition.columnIndex] == secondPlayerValue):
						positions.append(leftPosition)
						# print "left added"
		return positions
        '''

	def __str__(self):
		
            columnDict = {0:'A', 1:'B', 2:'C', 3:'D', 4:'E'}
            rowDict = {0:1, 1:2, 2:3, 3:4, 4:5}

            str = ""
            if self.parentNode == None:
                str += "root,"
            else:
                    # str += "%s," %(self.currentPosition)
                if self.currentPosition != None:
                    str += "%s%d," %(columnDict[self.currentPosition[0]], rowDict[self.currentPosition[1]])

            currentEvalFunctionString = ""
            if (self.currentEvalFunction == nextmin.negativeInfinity) or (self.bestChild == None and self.playMax == False and self.currentDepthOfNode != self.cutOffDepth):
                currentEvalFunctionString = "-Infinity"
            elif self.currentEvalFunction == nextmin.positiveInfinity or (self.bestChild == None and self.playMax == True and self.currentDepthOfNode != self.cutOffDepth):
                currentEvalFunctionString = "Infinity"
            else:
                currentEvalFunctionString = "%s" %(self.currentEvalFunction)

            str += "%d,%s" %(self.currentDepthOfNode, currentEvalFunctionString)

            return str

	def __repr__(self):
            return self.__str__()