from decisionmin import nextmin
from copy import deepcopy
class minimaxalgo:

	# gridBoxCell = []
	# player = ""
	# opponentPlayer = ""
	# rootEvalFunction = 0
	# cutOffDepth = 0
	# rootNode = None
	# negativeInfiniti = -100000
	# positiveInfiniti = 100000
	# bestRootNode = None

	bestGridBoxOutput = []

	def __init__(self, value,occupied_positions, playerValue, opponentPlayerValue, cutOffDepthValue):
            self.value=value
            self.occupied_positions = occupied_positions
            #print self.occupied_positions
            self.player = playerValue
            self.opponentPlayer = opponentPlayerValue
            self.cutOffDepth = cutOffDepthValue
            self.rootEvalFunction = self.calculateEvaluationFunction()
            # print "Current Eval Function is "
            # print self.rootEvalFunction
            # print "MiniMax start e(s)"
            self.negativeInfiniti = -100000
            self.positiveInfiniti = 100000
            self.bestRootNode = None
            print "Node,Depth,Value"
            self.rootNode = nextmin(None, value,occupied_positions, playerValue, opponentPlayerValue, self.negativeInfiniti, 0, False, [], self.negativeInfiniti, None, cutOffDepthValue)

	def calculateEvaluationFunction(self):
            evalFunctionValue = 0
            playerValue = 0
            opponentValue = 0
            for i in range(5):
                for j in range(5):
                        # print box
                    if self.occupied_positions[i][j] == self.player:
                        playerValue+=self.value[i][j]
                        #print self.occupied_positions[i][j]
                    elif self.occupied_positions[i][j] == self.opponentPlayer:
                        opponentValue+=self.value[i][j]
            evalFunctionValue = playerValue - opponentValue
            return evalFunctionValue


	def __str__(self):
            str = "---------------------------------------------------------\n"
            str += "Player = %s, Opponent = %s, E(s) = %d, cutOffDepth = %d\n" %(self.player, self.opponentPlayer, self.rootEvalFunction, self.cutOffDepth)
            for i in range(0, len(5)):
                for j in range(0, len(5)):
                            # print "%d, %d" %(i, j)
                    str += "[%3d, %s] " %(self.value[i][j], self.occupied_positions[i][j])
                    str += "\n"
            str += "%s" %(self.rootNode)+"\n"
            str += "---------------------------------------------------------"
            return str

	def __repr__(self):
            return self.__str__()


	def recursiveMiniMax(self, rootNodeObject=None):
            pos=[]
		
            if rootNodeObject.currentDepthOfNode < self.cutOffDepth:
                    # print "Main Process starts from the root game node"
                childNode = None
                for i in range(5):
                    for j in range(5):
                        #print self.occupied_positions[i][j]
                        if rootNodeObject.occupied_positions[i][j] == "*":
                                            # print "1 : Generate new successor node for [%d, %d]" %(i, j)
                            pos = [i,j]
                                            # print positionOfSuccessorToBeConsidered
                                            
                            if rootNodeObject.playMax == True:
                                # print "Parent Node being passed is "
                                # print rootNodeObject.currentEvalFunction
                                                    # print "----"
                                childNode = nextmin(rootNodeObject, rootNodeObject.value,rootNodeObject.occupied_positions, rootNodeObject.player, rootNodeObject.opponentPlayer, self.negativeInfiniti, rootNodeObject.currentDepthOfNode+1, False, [], rootNodeObject.value[i][j], pos, self.cutOffDepth)
                            else:
                                            
                                childNode = nextmin(rootNodeObject, rootNodeObject.value,rootNodeObject.occupied_positions, rootNodeObject.player, rootNodeObject.opponentPlayer, self.positiveInfiniti, rootNodeObject.currentDepthOfNode+1, True, [], rootNodeObject.value[i][j], pos, self.cutOffDepth)
                                            # 2 : Add it to the childNodeList of the rootObjectNode

                                rootNodeObject.childNodes.append(childNode)
                                self.recursiveMiniMax(childNode)
                                print rootNodeObject

                if rootNodeObject.playMax == True:
                        if rootNodeObject.parentNode != None:
                                if rootNodeObject.parentNode.currentEvalFunction < rootNodeObject.currentEvalFunction:
                                        rootNodeObject.parentNode.currentEvalFunction = rootNodeObject.currentEvalFunction
                                        rootNodeObject.parentNode.bestChild = rootNodeObject.currentPosition
                                        # rootNodeObject.parentNode.bestChild = deepcopy(rootNodeObject)
                                        # rootNodeObject.parentNode.bestChild.gridBoxCell = deepcopy(rootNodeObject.gridBoxCell)

                else:
                        # subtract for min
                        if rootNodeObject.parentNode != None:
                                if rootNodeObject.parentNode.currentEvalFunction >= rootNodeObject.currentEvalFunction:
                                        rootNodeObject.parentNode.currentEvalFunction = rootNodeObject.currentEvalFunction
                                        rootNodeObject.parentNode.bestChild = rootNodeObject.currentPosition
                                        # rootNodeObject.parentNode.bestChild = deepcopy(rootNodeObject)
                                        # rootNodeObject.parentNode.bestChild.gridBoxCell = deepcopy(rootNodeObject.gridBoxCell)
        # print "-____________________________________________-\n"

            return rootNodeObject

	def getBestRootNodeForMiniMax(self):
		# print "Calling recursive Method"
		# print self.rootNode
            self.bestRootNode = self.recursiveMiniMax(self.rootNode)
		# print self.rootNode
		# print "Printing all children's e(s)"
		# for i in range(0, len(self.rootNode.childNodes)):
		# 		print "[%d] - %d\n" %(i, self.rootNode.childNodes[i].currentEvalFunction)
		# print self.rootNode.childNodes

		# print "************* recursive Call is over now ****************"
		# print "Best Root Node is %s" %(self.bestRootNode.bestChild)
		# str = ""
            '''
            self.occupied_positions[self.bestRootNode.bestChild.rowIndex][self.bestRootNode.bestChild.columnIndex] = self.player
            enemyPositions = self.getEnemyBoxPositionsAdjacentToTheBox(self.value,self.occupied_positions, self.bestRootNode.bestChild.rowIndex, self.bestRootNode.bestChild.columnIndex, self.player, self.opponentPlayer)
            for eachEnemyPosition in enemyPositions:
		self.occupied_positions[eachEnemyPosition.rowIndex][eachEnemyPosition.columnIndex] = self.player
            '''
            i=self.bestRootNode.bestChild[0]
            j=self.bestRootNode.bestChild[1]
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
            str = ""
            for i in range(5):
		for j in range(5):
                    str += self.occupied_positions[i][j]
                    str += "\n"
            print str


			# for j in range(0, len(GameNode.bestGridBoxOutput)):
			# 	str += "%s " %(GameNode.bestGridBoxOutput[i][j])
			# str += "\n"
		# print str
		# print self.bestChild
		# str = ""
		# for i in range(0, len(self.bestRootNode.gridBoxCell)):
		# 	for j in range(0, len(self.bestRootNode.gridBoxCell)):
		# 		# print "%d, %d" %(i, j)
		# 		str += "[%3d, %s] " %(self.bestRootNode.gridBoxCell[i][j].value, self.bestRootNode.gridBoxCell[i][j].occupiedBy)
		# 	str += "\n"
		# print str
		# print "***********************"
		# str = ""
		# for i in range(0, len(self.rootNode.gridBoxCell)):
		# 	for j in range(0, len(self.gridBoxCell)):
		# 		# print "%d, %d" %(i, j)
		# 		str += "[%3d, %s] " %(self.rootNode.gridBoxCell[i][j].value, self.rootNode.gridBoxCell[i][j].occupiedBy)
		# 	str += "\n"
		# print str
            return "Task Completed"
        '''
	def isThisRaidOrSneak(self, value,occupied_positions, rowIndex, columnIndex, firstPlayerValue, secondPlayerValue):
            raid = False
            positions = []
		# Determine the position above
            if(rowIndex > 0):
                upPosition = Position(0, 0)
                upPosition.rowIndex = rowIndex - 1
                upPosition.columnIndex = columnIndex
                if(tempBoxState[upPosition.rowIndex][upPosition.columnIndex].occupiedBy == firstPlayerValue):
                    raid = True

                    # Determine the position to the right
            if(columnIndex < 4):
                rightPosition = Position(0, 0)
                rightPosition.rowIndex = rowIndex
                rightPosition.columnIndex = columnIndex + 1
                if(tempBoxState[rightPosition.rowIndex][rightPosition.columnIndex].occupiedBy == firstPlayerValue):
                    raid = True

                    # Determine the position below
            if(rowIndex < 4):
                bottomPosition = Position(0, 0)
                bottomPosition.rowIndex = rowIndex + 1
                bottomPosition.columnIndex = columnIndex
                if(tempBoxState[bottomPosition.rowIndex][bottomPosition.columnIndex].occupiedBy == firstPlayerValue):
                    raid = True

                    # Determine the position to the left
            if(columnIndex > 0):
                leftPosition = Position(0, 0)
                leftPosition.rowIndex = rowIndex
                leftPosition.columnIndex = columnIndex - 1
                if(tempBoxState[leftPosition.rowIndex][leftPosition.columnIndex].occupiedBy == firstPlayerValue):
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
                    if(tempBoxState[upPosition.rowIndex][upPosition.columnIndex].occupiedBy == secondPlayerValue):
                        positions.append(upPosition)
                                # print "up added"

                # Determine the position to the right
                if(columnIndex < (len(tempBoxState)-1)):
                    rightPosition = Position(0, 0)
                    rightPosition.rowIndex = rowIndex
                    rightPosition.columnIndex = columnIndex + 1
                    if(tempBoxState[rightPosition.rowIndex][rightPosition.columnIndex].occupiedBy == secondPlayerValue):
                        positions.append(rightPosition)
                                # print "right added"

                # Determine the position below
                if(rowIndex < len(tempBoxState)-1):
                    bottomPosition = Position(0, 0)
                    bottomPosition.rowIndex = rowIndex + 1
                    bottomPosition.columnIndex = columnIndex
                    if(tempBoxState[bottomPosition.rowIndex][bottomPosition.columnIndex].occupiedBy == secondPlayerValue):
                        positions.append(bottomPosition)
                                        # print "bottom added"

                # Determine the position to the left
                if(columnIndex > 0):
                    leftPosition = Position(0, 0)
                    leftPosition.rowIndex = rowIndex
                    leftPosition.columnIndex = columnIndex - 1
                    if(tempBoxState[leftPosition.rowIndex][leftPosition.columnIndex].occupiedBy == secondPlayerValue):
                        positions.append(leftPosition)
                                        # print "left added"
            return positions
        '''
            