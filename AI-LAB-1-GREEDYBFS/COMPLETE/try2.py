from BoxCell import BoxCell
from GameNode import GameNode
from Position import Position
from copy import deepcopy

class MiniMax:

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

	def __init__(self, gridBoxCellValues, playerValue, opponentPlayerValue, cutOffDepthValue):
		self.gridBoxCell = []
		for i in range(0, len(gridBoxCellValues)):
			self.gridBoxCell.append([])		# Append a new list
			for j in range(0, len(gridBoxCellValues)):
				self.gridBoxCell[i].append(BoxCell(gridBoxCellValues[i][j].value, gridBoxCellValues[i][j].occupiedBy))

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
		self.rootNode = GameNode(None, gridBoxCellValues, playerValue, opponentPlayerValue, self.negativeInfiniti, 0, False, [], self.negativeInfiniti, None, cutOffDepthValue)

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
				# print "%d, %d" %(i, j)
				str += "[%3d, %s] " %(self.gridBoxCell[i][j].value, self.gridBoxCell[i][j].occupiedBy)
			str += "\n"
		str += "%s" %(self.rootNode)+"\n"
		str += "---------------------------------------------------------"
		return str

	def __repr__(self):
		return self.__str__()


	def recursiveMiniMax(self, rootNodeObject=None):
		# global cutOffDepth
		# temp = "-> -> -> Working for %s - %d - %d" %(rootNodeObject.currentPosition, rootNodeObject.currentDepthOfNode, rootNodeObject.currentEvalFunction)
		# print temp.rjust(rootNodeObject.currentDepthOfNode*30, ' ')
		# print rootNodeObject
		# print "-> -> ->"
		# if rootNodeObject.currentDepthOfNode == self.cutOffDepth + 1:
			# Calculate the e(s) and check with parent.
			# print "Reached Leaf Node"
			# if rootNodeObject.currentDepthOfNode%2 == 1:
			# 	# add for max
			# else:
			# 	# subtract for min
		# originalRoot = deepcopy(rootNodeObject)
		# print "Size of Child Nodes %d" %(len(rootNodeObject.childNodes))
		# print rootNodeObject
		if rootNodeObject.currentDepthOfNode < self.cutOffDepth:
			# print "Main Process starts from the root game node"
			childNode = None
			for i in range(0, len(rootNodeObject.gridBoxCell)):
				for j in range(0, len(rootNodeObject.gridBoxCell)):
					if rootNodeObject.gridBoxCell[i][j].occupiedBy == "*":
						# print "1 : Generate new successor node for [%d, %d]" %(i, j)
						positionOfSuccessorToBeConsidered = Position(i, j)
						# print positionOfSuccessorToBeConsidered
						# str = ""
						# for i in range(0, len(rootNodeObject.gridBoxCell)):
						# 	for j in range(0, len(rootNodeObject.gridBoxCell)):
						# 		# print "%d, %d" %(i, j)
						# 		str += "[%3d, %s] " %(rootNodeObject.gridBoxCell[i][j].value, rootNodeObject.gridBoxCell[i][j].occupiedBy)
						# 	str += "\n"
						# print str
						# rootNodeObject.currentEvalFunction = originalRoot.currentEvalFunction
						# rootNodeObject.gridBoxCell = deepcopy(originalRoot.gridBoxCell)
						if rootNodeObject.playMax == True:
							# print "Parent Node being passed is "
							# print rootNodeObject.currentEvalFunction
							# print "----"
							childNode = GameNode(rootNodeObject, rootNodeObject.gridBoxCell, rootNodeObject.player, rootNodeObject.opponentPlayer, self.negativeInfiniti, rootNodeObject.currentDepthOfNode+1, False, [], rootNodeObject.gridBoxCell[i][j].value, positionOfSuccessorToBeConsidered, self.cutOffDepth)
						else:
							# print "Parent Node being passed is "
							# print rootNodeObject.currentEvalFunction
							# print "----"
							childNode = GameNode(rootNodeObject, rootNodeObject.gridBoxCell, rootNodeObject.player, rootNodeObject.opponentPlayer, self.positiveInfiniti, rootNodeObject.currentDepthOfNode+1, True, [], rootNodeObject.gridBoxCell[i][j].value, positionOfSuccessorToBeConsidered, self.cutOffDepth)
						# 2 : Add it to the childNodeList of the rootObjectNode
						
						rootNodeObject.childNodes.append(childNode)
						self.recursiveMiniMax(childNode)
						print rootNodeObject

			# temp = "-> -> -> Resumed for %s - %d" %(rootNodeObject.currentPosition, rootNodeObject.currentEvalFunction)
			# print temp.rjust(rootNodeObject.currentDepthOfNode*30, ' ')
			# temp = "Best child Node is %s" %(rootNodeObject.bestChild)
			# print temp.rjust(rootNodeObject.currentDepthOfNode*30, ' ')
			# temp = "Best grid box cell of the child is : "
			# print temp.rjust(rootNodeObject.currentDepthOfNode*30, ' ')
			# str = ""
			# for i in range(0, 5):
			# 	for j in range(0, 5):
			# 		str += "%s " %(rootNodeObject.bestGridBox[i][j])
			# 	str += "\n"
			# temp =  str
			# print temp.rjust(rootNodeObject.currentDepthOfNode*30, ' ')
			# temp = "Eval Function is %d" %(rootNodeObject.currentEvalFunction)
			# print temp.rjust(rootNodeObject.currentDepthOfNode*30, ' ')
			# we are still iterating through the child nodes
			# for i in range(0, len(rootNodeObject.childNodes)):
			# 	print "[%d] - %d\n" %(i, rootNodeObject.childNodes[i].currentEvalFunction)
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
		# print "Checking enemy boxes for "
		# print "[%d, %d]" %(rowIndex, columnIndex)
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