
from Position import Position
from copy import deepcopy
from evaluation_function import evaluation
class nextmin:

	bestGridBoxOutput = []
	negativeInfinity = -100000
	positiveInfinity = 100000
	head = False


	def __init__(self, parentNodeObject, value,occupied_positions, playerValue, opponentPlayerValue, currentEvalFunctionValue, currentDepthOfNodeValue, playMaxValue, childNodesValues, currentValueValue, currentPositionValue, cutOffDepthValue):
		
                if nextmin.head == False:
                        
			rr = open('traverse_log.txt','w')
                        rr.seek(0)
                        rr.truncate()
			rr.write("Node,Depth,Value\n")
			rr.close()
			nextmin.head = True
		self.parentNode = None
                self.occupied_positions=occupied_positions
                self.value=value
		
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
		
		if(parentNodeObject != None):
			self.parentNode = parentNodeObject
		
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
			
			self.currentValue = self.value[self.currentPosition.rowIndex][self.currentPosition.columnIndex]
			
			if self.playMax == True and self.parentNode != None:
				
				#self.occupied_positions[currentPositionValue.rowIndex][currentPositionValue.columnIndex] = self.player
				
                                i=currentPositionValue.rowIndex
                                j=currentPositionValue.columnIndex
                                self.occupied_positions[i][j]=self.player
                
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
                                
                                
                                zaa=evaluation(self.value,self.occupied_positions,self.player,self.opponentPlayer)
                                self.currentEvalFunction=zaa.eval()
				if self.parentNode.currentEvalFunction < self.currentEvalFunction and self.parentNode != None and self.currentDepthOfNode == self.cutOffDepth:
					# print "maximizing parent %s " %(self.parentNode.currentPosition)
					self.parentNode.currentEvalFunction = self.currentEvalFunction
					self.parentNode.bestChild = currentPositionValue
					self.parentNode.bestGridBox = deepcopy(self.occupied_positions)
					nextmin.bestGridBoxOutput = deepcopy(self.occupied_positions)
					
					

 			elif self.playMax == False and self.parentNode != None:
 				
                                
                                i=currentPositionValue.rowIndex
                                j=currentPositionValue.columnIndex
                                self.occupied_positions[i][j]=self.opponentPlayer
                
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
                                
                                
                                zaa=evaluation(self.value,self.occupied_positions,self.player,self.opponentPlayer)
                                self.currentEvalFunction=zaa.eval()
				if self.parentNode.currentEvalFunction >= self.currentEvalFunction and self.parentNode != None and self.currentDepthOfNode == self.cutOffDepth:
					# print "minimizing parent %s " %(self.parentNode.currentPosition)
					self.parentNode.currentEvalFunction = self.currentEvalFunction
					self.parentNode.bestChild = currentPositionValue
					self.parentNode.bestGridBox = deepcopy(self.occupied_positions)
					nextmin.bestGridBoxOutput = deepcopy(self.occupied_positions)
					
		print self
		

	def __str__(self):
		
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
		if (self.currentEvalFunction == nextmin.negativeInfinity) or (self.bestChild == None and self.playMax == False and self.currentDepthOfNode != self.cutOffDepth):
			currentEvalFunctionString = "-Infinity"
		elif self.currentEvalFunction == nextmin.positiveInfinity or (self.bestChild == None and self.playMax == True and self.currentDepthOfNode != self.cutOffDepth):
			currentEvalFunctionString = "Infinity"
		else:
			currentEvalFunctionString = "%s" %(self.currentEvalFunction)

		str += "%d,%s" %(self.currentDepthOfNode, currentEvalFunctionString)
		rr = open('traverse_log.txt','a+')
		rr.write(str+"\n")
		rr.close()
		
		return str

	def __repr__(self):
		return self.__str__()