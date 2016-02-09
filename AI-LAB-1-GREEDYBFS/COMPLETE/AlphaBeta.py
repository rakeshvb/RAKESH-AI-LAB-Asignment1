from BoxCell import BoxCell
from GameNodeAlphaBeta import GameNodeAlphaBeta
from Position import Position
from copy import deepcopy

class AlphaBeta:

	bestGridBoxOutput = []

	def __init__(self, gridBoxCellValues, playerValue, opponentPlayerValue, cutOffDepthValue):
		print "Constructing the gridBoxCell for AlphaBeta"
		self.gridBoxCell = []
		for i in range(0, len(gridBoxCellValues)):
			self.gridBoxCell.append([])		# Append a new list
			for j in range(0, len(gridBoxCellValues)):
				self.gridBoxCell[i].append(BoxCell(gridBoxCellValues[i][j].value, gridBoxCellValues[i][j].occupiedBy))
			print self.gridBoxCell[i]
			print "\n"
		print "GridBox constructed"
		self.player = playerValue
		self.opponentPlayer = opponentPlayerValue
		self.cutOffDepth = cutOffDepthValue
		self.rootEvalFunction = self.calculateEvaluationFunction()
		self.negativeInfiniti = -100000
		self.positiveInfiniti = 100000
		self.bestRootNode = None
		self.rootNode = GameNodeAlphaBeta(None, gridBoxCellValues, playerValue, opponentPlayerValue, self.negativeInfiniti, 0, False, [], self.negativeInfiniti, None, cutOffDepthValue, self.negativeInfiniti, self.positiveInfiniti)
		self.rootNode.outputNodeInformationToFile()
		GameNodeAlphaBeta.firstConstruct = 1
		self.outputFile = open('next_state.txt','w')
		print "Alpha Beta Constructed"
		# self.rootNode.outputNodeInformationToFile()

	def canWeContinuePlaying(self, stateBox):
		continueGame = False
		for i in range(0, len(stateBox)):
			for j in range(0, len(stateBox)):
				if stateBox[i][j].occupiedBy == "*":
					continueGame = True
					break
		return continueGame

	def calculateEvaluationFunction(self):
		evalFunctionValue = 0
		playerValue = 0
		opponentValue = 0
		for i in range(0, len(self.gridBoxCell)):
			for box in self.gridBoxCell[i]:
				# print box
				if box.occupiedBy == self.player:
					playerValue+=box.value
				elif box.occupiedBy == self.opponentPlayer:
					opponentValue+=box.value
		evalFunctionValue = playerValue - opponentValue
		return evalFunctionValue


	def __str__(self):
		str = "---------------------------------------------------------\n"
		str += "Player = %s, Opponent = %s, E(s) = %d, cutOffDepth = %d\n" %(self.player, self.opponentPlayer, self.rootEvalFunction, self.cutOffDepth)
		for i in range(0, len(self.gridBoxCell)):
			for j in range(0, len(self.gridBoxCell)):
				str += "[%3d, %s] " %(self.gridBoxCell[i][j].value, self.gridBoxCell[i][j].occupiedBy)
			str += "\n"
		str += "%s" %(self.rootNode)+"\n"
		str += "---------------------------------------------------------"
		return str

	def __repr__(self):
		return self.__str__()


	def recursiveAlphaBeta(self, rootNodeObject):
		if rootNodeObject.currentDepthOfNode < self.cutOffDepth:
			childNode = None
			pruningFlag = False
			# opFile = open("traverse_log.txt",'a+')
			# opFile.write("--------------------------------------------\n")
			# rootNodeObject.outputNodeInformationToFile()
			didItRun = False
			for i in range(0, len(rootNodeObject.gridBoxCell)):
				for j in range(0, len(rootNodeObject.gridBoxCell)):
					# rootNodeObject.outputNodeInformationToFile()
					if rootNodeObject.gridBoxCell[i][j].occupiedBy == "*" and pruningFlag == False:
						didItRun = True
						# decide if to prune or continue the recursion
						if rootNodeObject.playMax == True:
							if rootNodeObject.parentNode != None:
								# print "rootNodeObject.alpha > rootNodeObject.parentNode.beta"
								# print "%d greater than %d " %(rootNodeObject.alpha, rootNodeObject.parentNode.beta)
								if rootNodeObject.currentEvalFunction <= rootNodeObject.parentNode.alpha:
									# print "Pruning should work"
									pruningFlag = True
								else:
									# print "No Pruning"
									pruningFlag = False
						else:
							if rootNodeObject.parentNode != None:
								# print "rootNodeObject.beta > rootNodeObject.parentNode.alpha"
								# print "%d greater than %d " %(rootNodeObject.beta, rootNodeObject.parentNode.alpha)
								if rootNodeObject.currentEvalFunction >= rootNodeObject.parentNode.beta:
									# print "Pruning should work"
									pruningFlag = True
								else:
									# print "No Pruning"
									pruningFlag = False

						if pruningFlag == True:
							# print "pruning from ", rootNodeObject.currentPosition
							break					
						else:
							# print "1 : Generate new successor node for [%d, %d]" %(i, j)
							positionOfSuccessorToBeConsidered = Position(i, j)
							if rootNodeObject.playMax == True:
								childNode = GameNodeAlphaBeta(rootNodeObject, rootNodeObject.gridBoxCell, rootNodeObject.player, rootNodeObject.opponentPlayer, self.negativeInfiniti, rootNodeObject.currentDepthOfNode+1, False, [], rootNodeObject.gridBoxCell[i][j].value, positionOfSuccessorToBeConsidered, self.cutOffDepth, rootNodeObject.alpha, rootNodeObject.beta)
							else:
								childNode = GameNodeAlphaBeta(rootNodeObject, rootNodeObject.gridBoxCell, rootNodeObject.player, rootNodeObject.opponentPlayer, self.positiveInfiniti, rootNodeObject.currentDepthOfNode+1, True, [], rootNodeObject.gridBoxCell[i][j].value, positionOfSuccessorToBeConsidered, self.cutOffDepth, rootNodeObject.alpha, rootNodeObject.beta)


							# if rootNodeObject.playMax == True:
							# 	if rootNodeObject.currentEvalFunction < childNode.currentEvalFunction:
							# 		print "Parent was ", rootNodeObject
							# 		print "Modifying the parent's currentEvalFunction, childNode is playing Max at depth ", childNode.currentDepthOfNode, " - ", childNode.currentEvalFunction
							# 		rootNodeObject.currentEvalFunction = childNode.currentEvalFunction	
							# 		print "Parent is ", rootNodeObject
									
							# elif rootNodeObject.playMax == False:
							# 	if rootNodeObject.currentEvalFunction < childNode.currentEvalFunction:
							# 		print "Parent was ", rootNodeObject
							# 		print "Modifying the parent's currentEvalFunction, childNode is playing Min at depth ", childNode.currentDepthOfNode, " - ", childNode.currentEvalFunction
							# 		rootNodeObject.currentEvalFunction = childNode.currentEvalFunction
							# 		print "Parent is ", rootNodeObject
							

							childNode.outputNodeInformationToFile()
							if childNode.currentDepthOfNode == rootNodeObject.cutOffDepth:
								print rootNodeObject
								rootNodeObject.outputNodeInformationToFile()	

							rootNodeObject.childNodes.append(childNode)
							self.recursiveAlphaBeta(childNode)
							# print self
				# else:
				# 	break
				# print rootNodeObject
			if didItRun == False:
				# print "it did not run"
				playerValue = 0
				opponentValue = 0
				for i in range(0, len(rootNodeObject.gridBoxCell)):
					for box in rootNodeObject.gridBoxCell[i]:
						if box.occupiedBy == rootNodeObject.player:
							playerValue+=box.valuea
						elif box.occupiedBy == rootNodeObject.opponentPlayer:
							opponentValue+=box.value
				rootNodeObject.currentEvalFunction = playerValue - opponentValue

			
			if rootNodeObject.playMax == True:
				if rootNodeObject.parentNode != None:
					if rootNodeObject.parentNode.alpha < rootNodeObject.currentEvalFunction:
						if rootNodeObject.parentNode.currentEvalFunction < rootNodeObject.currentEvalFunction:
							rootNodeObject.parentNode.currentEvalFunction = rootNodeObject.currentEvalFunction
						rootNodeObject.parentNode.currentEvalFunction = rootNodeObject.currentEvalFunction
						if rootNodeObject.currentEvalFunction < rootNodeObject.parentNode.beta:
							rootNodeObject.parentNode.alpha = max(rootNodeObject.currentEvalFunction, rootNodeObject.alpha)
							rootNodeObject.parentNode.bestChild = rootNodeObject.currentPosition
						# print rootNodeObject.parentNode
						# rootNodeObject.parentNode.bestChild = deepcopy(rootNodeObject)
						# rootNodeObject.parentNode.bestChild.gridBoxCell = deepcopy(rootNodeObject.gridBoxCell)

			else:
				# subtract for min
				if rootNodeObject.parentNode != None:
					if rootNodeObject.parentNode.beta >= rootNodeObject.currentEvalFunction:
						rootNodeObject.parentNode.currentEvalFunction = rootNodeObject.currentEvalFunction
						# opFile = open("traverse_log.txt",'a+')
						# print("%d is max between %d and %d\n" %(max(rootNodeObject.currentEvalFunction, rootNodeObject.currentEvalFunction)), rootNodeObject.currentEvalFunction, rootNodeObject.currentEvalFunction)
						# opFile.close()
						if rootNodeObject.parentNode.currentEvalFunction < rootNodeObject.currentEvalFunction:
							rootNodeObject.parentNode.currentEvalFunction = rootNodeObject.currentEvalFunction
						if rootNodeObject.currentEvalFunction > rootNodeObject.parentNode.alpha:
							rootNodeObject.parentNode.beta = min(rootNodeObject.currentEvalFunction, rootNodeObject.beta)
							rootNodeObject.parentNode.bestChild = rootNodeObject.currentPosition
						# print rootNodeObject.parentNode
						# rootNodeObject.parentNode.bestChild = deepcopy(rootNodeObject)
						# rootNodeObject.parentNode.bestChild.gridBoxCell = deepcopy(rootNodeObject.gridBoxCell)
		if rootNodeObject.parentNode != None:
			rootNodeObject.parentNode.outputNodeInformationToFile()
		# print "-____________________________________________-\n"
		
		return rootNodeObject

	def getBestRootNodeForAlphaBeta(self):
		# print self.rootNode
		print "Calling recursiveAlphaBeta"
		self.bestRootNode = self.recursiveAlphaBeta(self.rootNode)
		# self.rootNode.outputNodeInformationToFile()
		# print "Printing all children's e(s)"
		# for i in range(0, len(self.rootNode.childNodes)):
		# 		print "[%d] - %d\n" %(i, self.rootNode.childNodes[i].currentEvalFunction)
		# print self.rootNode.childNodes

		print "************* recursive Call is over now ****************"
		print "Self.bestRootNode is ", self.bestRootNode.bestChild
		# print "Best Root Node is %s" %(self.bestRootNode.bestChild)
		# str = ""
		if self.bestRootNode.bestChild != None:
			self.gridBoxCell[self.bestRootNode.bestChild.rowIndex][self.bestRootNode.bestChild.columnIndex].occupiedBy = self.player
			enemyPositions = self.getEnemyBoxPositionsAdjacentToTheBox(self.gridBoxCell, self.bestRootNode.bestChild.rowIndex, self.bestRootNode.bestChild.columnIndex, self.player, self.opponentPlayer)
			for eachEnemyPosition in enemyPositions:
				self.gridBoxCell[eachEnemyPosition.rowIndex][eachEnemyPosition.columnIndex].occupiedBy = self.player

			str = ""
			for i in range(0, len(self.gridBoxCell)):
				for j in range(0, len(self.gridBoxCell)):
					str += self.gridBoxCell[i][j].occupiedBy
				str += "\n"
			print str

			self.outputFile = open('next_state.txt','w')
			self.outputFile.write(str)
			self.outputFile.close()
			print "Alpha Beta completed"
			return self.gridBoxCell
		else:
			print "Alpha Beta completed with error"
			return self.gridBoxCell

	def isThisRaidOrSneak(self, tempBoxState, rowIndex, columnIndex, firstPlayerValue, secondPlayerValue):
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
		if(columnIndex < (len(tempBoxState)-1)):
			rightPosition = Position(0, 0)
			rightPosition.rowIndex = rowIndex
			rightPosition.columnIndex = columnIndex + 1
			if(tempBoxState[rightPosition.rowIndex][rightPosition.columnIndex].occupiedBy == firstPlayerValue):
				raid = True

		# Determine the position below
		if(rowIndex < len(tempBoxState)-1):
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

	def getEnemyBoxPositionsAdjacentToTheBox(self, tempBoxState, rowIndex, columnIndex, firstPlayerValue, secondPlayerValue):
		raidOrSneak = True
		raidOrSneak = self.isThisRaidOrSneak(tempBoxState, rowIndex, columnIndex, firstPlayerValue, secondPlayerValue)

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