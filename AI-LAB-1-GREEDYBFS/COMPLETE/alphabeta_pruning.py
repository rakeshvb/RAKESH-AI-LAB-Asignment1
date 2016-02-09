from BoxCell import BoxCell
from Position import Position
from copy import deepcopy

class GameNodeAlphaBeta:

	bestGridBoxOutput = []
	negativeInfinity = -100000
	positiveInfinity = 100000
	headerPrinted = False
	printRoot = False
	firstConstruct = 0
	prevPrintedStrings = ""


	def __init__(self, parentNodeObject, gridBoxCellValues, playerValue, opponentPlayerValue, 
		currentEvalFunctionValue, currentDepthOfNodeValue, playMaxValue, childNodesValues, 
		currentValueValue, currentPositionValue, cutOffDepthValue, alphaValue, betaValue):
		if GameNodeAlphaBeta.headerPrinted == False:
			outputFile = open('traverse_log.txt','w')
			outputFile.write("Node,Depth,Value,Alpha,Beta\n")
			outputFile.close()
			GameNodeAlphaBeta.headerPrinted = True
		self.alpha = alphaValue
		self.beta = betaValue
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
		self.isParentModified = False
		
		if(parentNodeObject != None):
			self.parentNode = parentNodeObject
		self.gridBoxCell = []
		for i in range(0, len(gridBoxCellValues)):
			self.gridBoxCell.append([])		# Append a new list
			for j in range(0, len(gridBoxCellValues)):
				bCell = BoxCell(gridBoxCellValues[i][j].value, gridBoxCellValues[i][j].occupiedBy)
				self.gridBoxCell[i].append(bCell)
		self.player = playerValue
		self.opponentPlayer = opponentPlayerValue
		self.currentEvalFunction = currentEvalFunctionValue
		self.currentDepthOfNode = currentDepthOfNodeValue
		self.playMax = playMaxValue
		for i in range(0, len(childNodesValues)):
			childNodes.append(childNodesValues[i])

		self.currentValue = currentValueValue

		# We can proceed ahead
		if currentPositionValue != None:
			self.currentPosition = currentPositionValue
			self.currentValue = self.gridBoxCell[self.currentPosition.rowIndex][self.currentPosition.columnIndex].value
			parentModified = False
			if self.playMax == True and self.parentNode != None:
				# occupy the grid cell
				self.gridBoxCell[currentPositionValue.rowIndex][currentPositionValue.columnIndex].occupiedBy = self.player
				enemyPositions = self.getEnemyBoxPositionsAdjacentToTheBox(self.gridBoxCell, currentPositionValue.rowIndex, currentPositionValue.columnIndex, self.player, self.opponentPlayer)
				# determine if it is raid or sneak
				for eachEnemyPosition in enemyPositions:
					self.gridBoxCell[eachEnemyPosition.rowIndex][eachEnemyPosition.columnIndex].occupiedBy = self.player

				# For leaf nodes calculate the E(S) and propogate to parent as necessary
				# print self
				if self.currentDepthOfNode == self.cutOffDepth:
					# Calculate the E(S)
					playerValue = 0
					opponentValue = 0
					for i in range(0, len(self.gridBoxCell)):
						for box in self.gridBoxCell[i]:
							if box.occupiedBy == self.player:
								playerValue+=box.value
							elif box.occupiedBy == self.opponentPlayer:
								opponentValue+=box.value
					self.currentEvalFunction = playerValue - opponentValue
					# print self
					# self.outputNodeInformationToFile()
					# self.alpha = self.currentEvalFunction
					self.parentNode.currentEvalFunction = max(self.currentEvalFunction, self.parentNode.currentEvalFunction)
					if self.parentNode.alpha < self.currentEvalFunction:
						# print "For node %s" %(self)
						# print "%d is max between %d and %d" %(max(self.currentEvalFunction, self.parentNode.alpha), self.currentEvalFunction, self.parentNode.alpha)
						
						# self.parentNode.outputNodeInformationToFile()
						self.parentNode.bestChild = currentPositionValue
						self.parentNode.bestGridBox = deepcopy(self.gridBoxCell)
						GameNodeAlphaBeta.bestGridBoxOutput = deepcopy(self.gridBoxCell)
						parentModified = True
						self.isParentModified = True
						if self.currentEvalFunction < self.parentNode.beta:
							self.parentNode.alpha = self.currentEvalFunction
						# if self.parentNode != None:
						# 	self.parentNode.currentEvalFunction = min(self.parentNode.currentEvalFunction, self.currentEvalFunction)

						# print "Modified %s, while creating leaf node %s" %(self.parentNode, self)
						# print self.parentNode
				
				else:
					parentModified = False
					self.isParentModified = False

 			elif self.playMax == False and self.parentNode != None:
				self.gridBoxCell[currentPositionValue.rowIndex][currentPositionValue.columnIndex].occupiedBy = self.opponentPlayer
				enemyPositions = self.getEnemyBoxPositionsAdjacentToTheBox(self.gridBoxCell, currentPositionValue.rowIndex, currentPositionValue.columnIndex, self.opponentPlayer, self.player)
				for eachEnemyPosition in enemyPositions:
					self.gridBoxCell[eachEnemyPosition.rowIndex][eachEnemyPosition.columnIndex].occupiedBy = self.opponentPlayer

				# For leaf nodes calculate the E(S) and propogate to parent as necessary
				if self.currentDepthOfNode == self.cutOffDepth:
					playerValue = 0
					opponentValue = 0
					for i in range(0, len(self.gridBoxCell)):
						for box in self.gridBoxCell[i]:
							# print box
							if box.occupiedBy == self.player:
								playerValue+=box.value
							elif box.occupiedBy == self.opponentPlayer:
								opponentValue+=box.value
					self.currentEvalFunction = playerValue - opponentValue
					# self.outputNodeInformationToFile()
					# self.beta = self.currentEvalFunction
					self.parentNode.currentEvalFunction = min(self.currentEvalFunction, self.parentNode.currentEvalFunction)
					if self.parentNode.beta >= self.currentEvalFunction:
						# print "For node %s" %(self)
						# print "%d is min between %d and %d as a new BETA\n" %( min(self.currentEvalFunction, self.parentNode.beta), self.currentEvalFunction, self.parentNode.beta  )
						
						self.parentNode.bestChild = currentPositionValue
						self.parentNode.bestGridBox = deepcopy(self.gridBoxCell)
						GameNodeAlphaBeta.bestGridBoxOutput = deepcopy(self.gridBoxCell)
						parentModified = True
						self.isParentModified = True
						if self.currentEvalFunction > self.parentNode.alpha:
							self.parentNode.beta = self.currentEvalFunction
						# if self.parentNode != None:
						# 	self.parentNode.currentEvalFunction = max(self.parentNode.currentEvalFunction, self.currentEvalFunction)
						# print "Modified %s, while creating leaf node %s" %(self.parentNode, self)
						# print self.parentNode
				else:
					parentModified = False
					self.isParentModified = False
				# print GameNodeAlphaBeta.firstConstruct
			
			# self.outputNodeInformationToFile()

			# if GameNodeAlphaBeta.firstConstruct > 0:
			# 	self.parentNode.outputNodeInformationToFile()
			# 	GameNodeAlphaBeta.firstConstruct += 1

			# if parentModified:
			# 	print self.parentNode
			
		

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


	def __str__(self):
		
		columnDict = {0:'A', 1:'B', 2:'C', 3:'D', 4:'E'}
		rowDict = {0:1, 1:2, 2:3, 3:4, 4:5}

		str = ""
		if self.parentNode == None:
			str += "root,"
		else:
			if self.currentPosition != None:
				str += "%s%d," %(columnDict[self.currentPosition.columnIndex], rowDict[self.currentPosition.rowIndex])
		
		currentEvalFunctionString = ""
		if (self.currentEvalFunction == GameNodeAlphaBeta.negativeInfinity) or (self.bestChild == None and self.playMax == False and self.currentDepthOfNode != self.cutOffDepth):
			currentEvalFunctionString = "-Infinity"
		elif self.currentEvalFunction == GameNodeAlphaBeta.positiveInfinity or (self.bestChild == None and self.playMax == True and self.currentDepthOfNode != self.cutOffDepth):
			currentEvalFunctionString = "Infinity"
		else:
			currentEvalFunctionString = "%s" %(self.currentEvalFunction)

		alpha = "-Infinity"
		beta = "Infinity"
		if self.alpha == GameNodeAlphaBeta.negativeInfinity:
			alpha = "-Infinity"
		elif self.alpha == GameNodeAlphaBeta.positiveInfinity:
			alpha = "Infinity"
		else:
			alpha = "%d" %(self.alpha)

		if self.beta == GameNodeAlphaBeta.negativeInfinity:
			beta = "-Infinity"
		elif self.beta == GameNodeAlphaBeta.positiveInfinity:
			beta = "Infinity"
		else:
			beta = "%d" %(self.beta)

		str += "%d,%s,%s,%s" %(self.currentDepthOfNode, currentEvalFunctionString, alpha, beta)
		# print str
		# outputFile = open('traverse_log.txt','a+')
		# outputFile.write(str+"\n")
		# outputFile.close()
		return str

	def __repr__(self):
		return self.__str__()

	def outputNodeInformationToFile(self):
		columnDict = {0:'A', 1:'B', 2:'C', 3:'D', 4:'E'}
		rowDict = {0:1, 1:2, 2:3, 3:4, 4:5}

		str = ""
		if self.parentNode == None:
			str += "root,"
		else:
			if self.currentPosition != None:
				str += "%s%d," %(columnDict[self.currentPosition.columnIndex], rowDict[self.currentPosition.rowIndex])
		
		currentEvalFunctionString = ""
		if (self.currentEvalFunction == GameNodeAlphaBeta.negativeInfinity): 
	# or (self.bestChild == None and self.playMax == False and self.currentDepthOfNode != self.cutOffDepth):
			currentEvalFunctionString = "-Infinity"
		elif self.currentEvalFunction == GameNodeAlphaBeta.positiveInfinity:
		 # or (self.bestChild == None and self.playMax == True and self.currentDepthOfNode != self.cutOffDepth):
			currentEvalFunctionString = "Infinity"
		else:
			currentEvalFunctionString = "%s" %(self.currentEvalFunction)

		alpha = "-Infinity"
		beta = "Infinity"
		if self.alpha == GameNodeAlphaBeta.negativeInfinity:
			alpha = "-Infinity"
		elif self.alpha == GameNodeAlphaBeta.positiveInfinity:
			alpha = "Infinity"
		else:
			alpha = "%d" %(self.alpha)

		if self.beta == GameNodeAlphaBeta.negativeInfinity:
			beta = "-Infinity"
		elif self.beta == GameNodeAlphaBeta.positiveInfinity:
			beta = "Infinity"
		else:
			beta = "%d" %(self.beta)

		str += "%d,%s,%s,%s" %(self.currentDepthOfNode, currentEvalFunctionString, alpha, beta)
		outputFile = open('traverse_log.txt','a+')
		if str != GameNodeAlphaBeta.prevPrintedStrings:
			outputFile.write(str+"\n")
			GameNodeAlphaBeta.prevPrintedStrings = str
			# opBox = ""
			# if(str == "B2,1,-3,-3,-3"):
			# 	for i in range(0, len(self.gridBoxCell)):
			# 		opBox+= "%s\n" %(self.gridBoxCell[i])
			# outputFile.write(opBox)
			
			
			
		outputFile.close()