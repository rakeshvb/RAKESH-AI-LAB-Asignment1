from evaluation_function import evaluation
from Position import Position
from copy import deepcopy

class alphabeta_decision:
        flag2=False
	bestGridBoxOutput = []
	
	sempty = ""
        head = False
        negativeInfinity = -100000
	positiveInfinity = 100000
	
	def __init__(self, parentNodeObject, value,occupied_positions, player, oplayer, currentEvalFunctionValue, currentDepthOfNodeValue, playMaxValue, childNodesValues, currentValueValue, currentPositionValue, cutoffdepth, alphaValue, betaValue):
		
                if alphabeta_decision.head == False:
                
                    r5 = open('traverse_log.txt','w')
                    r5.seek(0)
                    r5.truncate()
                    r5.write("Node,Depth,Value,Alpha,Beta\n")
                    r5.close()
                    alphabeta_decision.head=True
                self.value=value
                self.occupied_positions=occupied_positions
		self.alpha = alphaValue
		self.beta = betaValue
		self.parentNode = None
		
		
		self.playMax = True
		self.childNodes = []
		
		self.currentPosition = None
		self.bestChild = None
		self.bestGridBox = []
		self.cutOffDepth = cutoffdepth
		self.pm = False
		
		if(parentNodeObject != None):
			self.parentNode = parentNodeObject
		
		
		self.player = player
		self.oplayer = oplayer
		self.eval_value = currentEvalFunctionValue
                # self.eval_value,"RV RV RV" 
		self.currentDepthOfNode = currentDepthOfNodeValue
		self.playMax = playMaxValue
		for i in range(0, len(childNodesValues)):
			childNodes.append(childNodesValues[i])

		self.currentValue = currentValueValue

		
		if currentPositionValue != None:
			self.currentPosition = currentPositionValue
                        #print self.currentPosition
			self.currentValue = self.value[self.currentPosition.rowIndex][self.currentPosition.columnIndex]
			parentModified = False
			if self.playMax == True and self.parentNode != None:
				
                                i=currentPositionValue.rowIndex
                                j=currentPositionValue.columnIndex
                                self.occupied_positions[i][j]=self.player
                
                                if((i!=0 and self.occupied_positions[i-1][j]==self.oplayer) and ((i!=4 and self.occupied_positions[i+1][j]==self.player) or (j!=0 and self.occupied_positions[i][j-1]==self.player) or (j!=4 and self.occupied_positions[i][j+1]==self.player))):
                                    self.occupied_positions[i-1][j]=self.player
                    #print occupied_positions[i-1][j]
                                if((i!=4 and self.occupied_positions[i+1][j]==self.oplayer) and ((i!=0 and self.occupied_positions[i-1][j]==self.player) or (j!=0 and self.occupied_positions[i][j-1]==self.player) or (j!=4 and self.occupied_positions[i][j+1]==self.player))):
                                    self.occupied_positions[i+1][j]=self.player
                    #print occupied_positions[i+1][j]
                                if((j!=4 and self.occupied_positions[i][j+1]==self.oplayer) and ((i!=4 and self.occupied_positions[i+1][j]==self.player) or (i!=0 and self.occupied_positions[i-1][j]==self.player) or (j!=0 and self.occupied_positions[i][j-1]==self.player) )):
                                    self.occupied_positions[i][j+1]=self.player
                    #print occupied_positions[i][j-1]
                                if((j!=0 and self.occupied_positions[i][j-1]==self.oplayer) and ((i!=4 and self.occupied_positions[i+1][j]==self.player)or (i!=0 and self.occupied_positions[i-1][j]==self.player) or (j!=4 and self.occupied_positions[i][j+1]==self.player))):
                                    self.occupied_positions[i][j-1]=self.player
		
				if self.currentDepthOfNode == self.cutOffDepth :
					
                                        zaaa=evaluation(self.value,self.occupied_positions,self.player,self.oplayer)
                                        self.eval_value=zaaa.eval()
                                        
					self.parentNode.eval_value = max(self.eval_value, self.parentNode.eval_value)

					if self.parentNode.alpha < self.eval_value :
						
						self.parentNode.bestChild = currentPositionValue
						self.parentNode.bestGridBox = deepcopy(self.occupied_positions)
						alphabeta_decision.bestGridBoxOutput = deepcopy(self.occupied_positions)
						parentModified = True
						self.pm = True
						if self.eval_value < self.parentNode.beta:
							self.parentNode.alpha = self.eval_value
						
                                else:
                                    parentModified = False
                                    self.pm = False		
 			elif self.playMax == False and self.parentNode != None:
				i=currentPositionValue.rowIndex
                                j=currentPositionValue.columnIndex
                                self.occupied_positions[i][j]=self.oplayer
                
                                if((i!=0 and self.occupied_positions[i-1][j]==self.player) and ((i!=4 and self.occupied_positions[i+1][j]==self.oplayer) or (j!=0 and self.occupied_positions[i][j-1]==self.oplayer) or (j!=4 and self.occupied_positions[i][j+1]==self.oplayer))):
                                    self.occupied_positions[i-1][j]=self.oplayer
                    #print occupied_positions[i-1][j]
                                if((i!=4 and self.occupied_positions[i+1][j]==self.player) and ((i!=0 and self.occupied_positions[i-1][j]==self.oplayer) or (j!=0 and self.occupied_positions[i][j-1]==self.oplayer) or (j!=4 and self.occupied_positions[i][j+1]==self.oplayer))):
                                    self.occupied_positions[i+1][j]=self.oplayer
                    #print occupied_positions[i+1][j]
                                if((j!=4 and self.occupied_positions[i][j+1]==self.player) and ((i!=4 and self.occupied_positions[i+1][j]==self.oplayer) or (i!=0 and self.occupied_positions[i-1][j]==self.oplayer) or (j!=0 and self.occupied_positions[i][j-1]==self.oplayer) )):
                                    self.occupied_positions[i][j+1]=self.oplayer
                    #print occupied_positions[i][j-1]
                                if((j!=0 and self.occupied_positions[i][j-1]==self.player) and ((i!=4 and self.occupied_positions[i+1][j]==self.oplayer)or (i!=0 and self.occupied_positions[i-1][j]==self.oplayer) or (j!=4 and self.occupied_positions[i][j+1]==self.oplayer))):
                                    self.occupied_positions[i][j-1]=self.oplayer
				# For leaf nodes calculate the E(S) and propogate to parent as necessary
				
                                if self.currentDepthOfNode == self.cutOffDepth:
                                        #print occupied_positions
					zzaaa=evaluation(self.value,self.occupied_positions,self.player,self.oplayer)
                                        self.eval_value=zzaaa.eval()
                                        #print self.eval_value
                                        self.parentNode.eval_value = min(self.eval_value, self.parentNode.eval_value)
					if self.parentNode.beta >= self.eval_value:
						
						self.parentNode.bestChild = currentPositionValue
						self.parentNode.bestGridBox = deepcopy(self.occupied_positions)
						alphabeta_decision.bestGridBoxOutput = deepcopy(self.occupied_positions)
						parentModified = True
						self.pm = True
						if self.eval_value > self.parentNode.alpha:
							self.parentNode.beta = self.eval_value
						
				else:
					parentModified = False
					self.pm = False

				
				
			

	def __str__(self):
		
		columnDict = {0:'A', 1:'B', 2:'C', 3:'D', 4:'E'}
		rowDict = {0:1, 1:2, 2:3, 3:4, 4:5}

		str = ""
		if self.parentNode == None:
			str += "root,"
		else:
			if self.currentPosition != None:
				str += "%s%d," %(columnDict[self.currentPosition.columnIndex], rowDict[self.currentPosition.rowIndex])
		
		opstring = ""
		if (self.eval_value == alphabeta_decision.negativeInfinity) or (self.bestChild == None and self.playMax == False and self.currentDepthOfNode != self.cutOffDepth):
			opstring = "-Infinity"
		elif self.eval_value == alphabeta_decision.positiveInfinity or (self.bestChild == None and self.playMax == True and self.currentDepthOfNode != self.cutOffDepth):
			opstring = "Infinity"
		else:
			opstring = "%s" %(self.eval_value)

		alpha = "-Infinity"
		beta = "Infinity"
		if self.alpha == alphabeta_decision.negativeInfinity:
			alpha = "-Infinity"
		elif self.alpha == alphabeta_decision.positiveInfinity:
			alpha = "Infinity"
		else:
			alpha = "%d" %(self.alpha)

		if self.beta == alphabeta_decision.negativeInfinity:
			beta = "-Infinity"
		elif self.beta == alphabeta_decision.positiveInfinity:
			beta = "Infinity"
		else:
			beta = "%d" %(self.beta)

		str += "%d,%s,%s,%s" %(self.currentDepthOfNode, opstring, alpha, beta)
		
		return str

	def __repr__(self):
		return self.__str__()

	def travFile(self):
		columnDict = {0:'A', 1:'B', 2:'C', 3:'D', 4:'E'}
		rowDict = {0:1, 1:2, 2:3, 3:4, 4:5}

		str = ""
		if self.parentNode == None:
			str += "root,"
		else:
			if self.currentPosition != None:
				str += "%s%d," %(columnDict[self.currentPosition.columnIndex], rowDict[self.currentPosition.rowIndex])
		
		opstring = ""
		if (self.eval_value == alphabeta_decision.negativeInfinity) or (self.bestChild == None and self.playMax == False and self.currentDepthOfNode != self.cutOffDepth):
			opstring = "-Infinity"
		elif self.eval_value == alphabeta_decision.positiveInfinity or (self.bestChild == None and self.playMax == True and self.currentDepthOfNode != self.cutOffDepth):
			opstring = "Infinity"
		else:
			opstring = "%s" %(self.eval_value)

		alpha = "-Infinity"
		beta = "Infinity"
		if self.alpha == alphabeta_decision.negativeInfinity:
			alpha = "-Infinity"
		elif self.alpha == alphabeta_decision.positiveInfinity:
			alpha = "Infinity"
		else:
			alpha = "%d" %(self.alpha)

		if self.beta == alphabeta_decision.negativeInfinity:
			beta = "-Infinity"
		elif self.beta == alphabeta_decision.positiveInfinity:
			beta = "Infinity"
		else:
			beta = "%d" %(self.beta)

		str += "%d,%s,%s,%s" %(self.currentDepthOfNode, opstring, alpha, beta)
		r5 = open('traverse_log.txt','a+')
		if str != alphabeta_decision.sempty:
			r5.write(str+"\n")
			alphabeta_decision.sempty = str
			
			
			
		r5.close()