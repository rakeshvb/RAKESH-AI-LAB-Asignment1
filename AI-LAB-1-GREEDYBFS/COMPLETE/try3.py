from BoxCell import BoxCell
from Position import Position
from copy import deepcopy

class GameNode:

	bestGridBoxOutput = []
	negativeInfinity = -100000
	positiveInfinity = 100000

	def __init__(self, parentNodeObject, gridBoxCellValues, playerValue, opponentPlayerValue, currentEvalFunctionValue, currentDepthOfNodeValue, playMaxValue, childNodesValues, currentValueValue, currentPositionValue, cutOffDepthValue):
		
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
		# print "Constructing new GameNode"
		if(parentNodeObject != None):
			self.parentNode = parentNodeObject
			# print "Parent Node Object in constructor is "
			print parentNodeObject.currentEvalFunction
			# print "*****------*****"
		self.gridBoxCell = []
		for i in range(0, len(gridBoxCellValues)):
			self.gridBoxCell.append([])		# Append a new list
			for j in range(0, len(gridBoxCellValues)):
				bCell = BoxCell(gridBoxCellValues[i][j].value, gridBoxCellValues[i][j].occupiedBy)
				self.gridBoxCell[i].append(bCell)
			# print self.gridBoxCell[i]
			# print "\n"

		# print "Normal construction resumes"

		self.player = playerValue
		self.opponentPlayer = opponentPlayerValue
		self.currentEvalFunction = currentEvalFunctionValue
		self.currentDepthOfNode = currentDepthOfNodeValue
		self.playMax = playMaxValue
		for i in range(0, len(childNodesValues)):
			childNodes.append(childNodesValues[i])

		self.currentValue = currentValueValue
		if currentPositionValue != None:
			# print "Current Position is not null"
			# self.currentPosition = Position(currentPositionValue.rowIndex, currentPositionValue.columnIndex)
			self.currentPosition = currentPositionValue
			# self.currentPosition.columnIndex = currentPositionValue.columnIndex
			# print self.currentPosition
			self.currentValue = self.gridBoxCell[self.currentPosition.rowIndex][self.currentPosition.columnIndex].value
			# print "self.currentValue is %d" %(self.currentValue)

			if self.playMax == True and self.parentNode != None:
				# print "For %s, current Value %d added to %d " %(playerValue, self.currentValue, self.currentEvalFunction)
				# self.currentEvalFunction = parentsOriginalEvalFunction + self.currentValue
				# print self.currentValue
				self.gridBoxCell[currentPositionValue.rowIndex][currentPositionValue.columnIndex].occupiedBy = self.player
				enemyPositions = self.getEnemyBoxPositionsAdjacentToTheBox(self.gridBoxCell, currentPositionValue.rowIndex, currentPositionValue.columnIndex, self.player, self.opponentPlayer)
				for eachEnemyPosition in enemyPositions:
					self.gridBoxCell[eachEnemyPosition.rowIndex][eachEnemyPosition.columnIndex].occupiedBy = self.player

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
					# self.currentEvalFunction += (2 * self.gridBoxCell[eachEnemyPosition.rowIndex][eachEnemyPosition.columnIndex].value)
				# print self.gridBoxCell[currentPositionValue.rowIndex][currentPositionValue.columnIndex].occupiedBy
				# print self.parentNode
				# print "\nthat was parent \n"
				# print self.parentNode.currentEvalFunction
				# print self.currentEvalFunction
				# print "self.parentNode.currentEvalFunction < self.currentEvalFunction"
				# print self.parentNode.currentEvalFunction < self.currentEvalFunction
				# print "If checking as above"
				if self.parentNode.currentEvalFunction < self.currentEvalFunction and self.parentNode != None and self.currentDepthOfNode == self.cutOffDepth:
					# print "maximizing parent %s " %(self.parentNode.currentPosition)
					self.parentNode.currentEvalFunction = self.currentEvalFunction
					self.parentNode.bestChild = currentPositionValue
					self.parentNode.bestGridBox = deepcopy(self.gridBoxCell)
					GameNode.bestGridBoxOutput = deepcopy(self.gridBoxCell)
					
					# GameNode.bestGridBoxOutput = []
					# for i in range(0, len(self.gridBoxCell)):
					# 	GameNode.bestGridBoxOutput.append([])
					# 	for j in range(0, len(self.gridBoxCell)):
					# 		GameNode.bestGridBoxOutput[i].append(self.gridBoxCell[i][j])
					# self.parentNode.bestChild = deepcopy(self)

 			elif self.playMax == False and self.parentNode != None:
 				# print "For %s, current Value %d subtracted from %d " %(opponentPlayerValue, self.currentValue, self.currentEvalFunction) 				
				# self.currentEvalFunction = parentsOriginalEvalFunction - self.currentValue
				self.gridBoxCell[currentPositionValue.rowIndex][currentPositionValue.columnIndex].occupiedBy = self.opponentPlayer
				enemyPositions = self.getEnemyBoxPositionsAdjacentToTheBox(self.gridBoxCell, currentPositionValue.rowIndex, currentPositionValue.columnIndex, self.opponentPlayer, self.player)
				for eachEnemyPosition in enemyPositions:
					self.gridBoxCell[eachEnemyPosition.rowIndex][eachEnemyPosition.columnIndex].occupiedBy = self.opponentPlayer
					# self.currentEvalFunction += (2 * self.gridBoxCell[eachEnemyPosition.rowIndex][eachEnemyPosition.columnIndex].value)

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
				# print self.gridBoxCell[currentPositionValue.rowIndex][currentPositionValue.columnIndex].occupiedBy
				# print self.parentNode
				# print "\nthat was parent \n"
				# print self.parentNode.currentEvalFunction
				# print self.currentEvalFunction
				# print "self.parentNode.currentEvalFunction >= self.currentEvalFunction"
				# print self.parentNode.currentEvalFunction >= self.currentEvalFunction
				# print "If checking as above"

				if self.parentNode.currentEvalFunction >= self.currentEvalFunction and self.parentNode != None and self.currentDepthOfNode == self.cutOffDepth:
					# print "minimizing parent %s " %(self.parentNode.currentPosition)
					self.parentNode.currentEvalFunction = self.currentEvalFunction
					self.parentNode.bestChild = currentPositionValue
					self.parentNode.bestGridBox = deepcopy(self.gridBoxCell)
					GameNode.bestGridBoxOutput = deepcopy(self.gridBoxCell)
					# GameNode.bestGridBoxOutput = []
					# for i in range(0, len(self.gridBoxCell)):
					# 	GameNode.bestGridBoxOutput.append([])
					# 	for j in range(0, len(self.gridBoxCell)):
					# 		GameNode.bestGridBoxOutput[i].append(self.gridBoxCell[i][j])
					# self.parentNode.bestChild = deepcopy(self)
			# print "After constructing new Game Node"
		# else:
		# 	print "Current Position is null"
		# if(self.parentNode == None):
		print self
		# else:
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
		# str = " *****\nGameNode : Current Value = %3d " %self.currentValue
		# if(self.playMax):
		# 	str += "Playing for %s\n" %(self.player)
		# else:
		# 	str += "Playing for %s\n" %(self.opponentPlayer)

		# for i in range(0, len(self.gridBoxCell)):
		# 	for j in range(0, len(self.gridBoxCell)):
		# 		# print "%d, %d" %(i, j)
		# 		str += "[%3d, %s] " %(self.gridBoxCell[i][j].value, self.gridBoxCell[i][j].occupiedBy)
		# 	str += "\n"
		# str += " ***** "
		# str = "%2d | %10d" %(self.currentDepthOfNode, self.currentEvalFunction)
		# str = "---------------------------GAMENODE-------------------------------------------------\n"
		# str = ""
		# if self.parentNode == None:
		# 	str = "root,%d,%d" %(self.currentDepthOfNode, self.currentEvalFunction)
		# else:
		# 	str = "%s,%d,%d" %(self.parentNode.currentPosition, self.parentNode.currentDepthOfNode, self.parentNode.currentEvalFunction)
		# 	parentNode1 = self.parentNode
			# if(parentNode1.parentNode == None):
			# 	str += "root,%d,%d" %(parentNode1.parentNode.currentDepthOfNode, parentNode1.parentNode.currentEvalFunction)
			# else:
			# 	str += "%s,%d,%d" %(parentNode1.parentNode.currentPosition, parentNode1.parentNode.currentDepthOfNode, parentNode1.parentNode.currentEvalFunction)

		columnDict = {0:'A', 1:'B', 2:'C', 3:'D', 4:'E'}
		rowDict = {0:1, 1:2, 2:3, 3:4, 4:5}

		str = ""
		if self.parentNode == None:
			str += "root,"
		else:
			# str += "%s," %(self.currentPosition)
			if self.currentPosition != None:
				str += "%s%d," %(columnDict[self.currentPosition.columnIndex], rowDict[self.currentPosition.rowIndex])
		
		currentEvalFunctionString = ""
		if (self.currentEvalFunction == GameNode.negativeInfinity) or (self.bestChild == None and self.playMax == False and self.currentDepthOfNode != self.cutOffDepth):
			currentEvalFunctionString = "-Infinity"
		elif self.currentEvalFunction == GameNode.positiveInfinity or (self.bestChild == None and self.playMax == True and self.currentDepthOfNode != self.cutOffDepth):
			currentEvalFunctionString = "Infinity"
		else:
			currentEvalFunctionString = "%s" %(self.currentEvalFunction)

		str += "%d,%s" %(self.currentDepthOfNode, currentEvalFunctionString)
		# str += "\n"
		# str += ""

		# if self.parentNode == None:
		# 	str += "root,"
		# 	currentEvalFunctionString = ""
		# 	if self.currentEvalFunction == GameNode.negativeInfinity:
		# 		currentEvalFunctionString = "-Infinity"
		# 	elif self.currentEvalFunction == GameNode.positiveInfinity:
		# 		currentEvalFunctionString = "Infinity"
		# 	else:
		# 		currentEvalFunctionString = "%s" %(self.currentEvalFunction)
		# 	str += "%d,%s" %(self.currentDepthOfNode, currentEvalFunctionString)
		# else:
		# 	if self.parentNode.currentPosition != None:
		# 		str += "%s%d," %(columnDict[self.parentNode.currentPosition.columnIndex], rowDict[self.parentNode.currentPosition.rowIndex])
		# 	else:
		# 		str += "root,"

		# 	currentEvalFunctionString = ""
		# 	if self.parentNode.currentEvalFunction == GameNode.negativeInfinity:
		# 		currentEvalFunctionString = "-Infinity"
		# 	elif self.parentNode.currentEvalFunction == GameNode.positiveInfinity:
		# 		currentEvalFunctionString = "Infinity"
		# 	else:
		# 		currentEvalFunctionString = "%s" %(self.parentNode.currentEvalFunction)

		# 	str += "%d,%s" %(self.parentNode.currentDepthOfNode, currentEvalFunctionString)

		# str += "\n Current Grid box as follows\n"
		# for i in range(0, len(self.gridBoxCell)):
		# 	for j in range(0, len(self.gridBoxCell)):
		# 		str += "%s " %(self.gridBoxCell[i][j])
		# 	str += "\n"
		# print str
		# str += "\n Best Grid box as follow\n"
		# for i in range(0, len(self.bestGridBox)):
		# 	for j in range(0, len(self.bestGridBox)):
		# 		str += "%s " %(self.bestGridBox[i][j])
		# 	str += "\n"
		# # print str
		# str += "\n---------------------------*******-------------------------------------------------"
		return str

	def __repr__(self):
		return self.__str__()