from evaluation_function import evaluation
from alphabeta_decision import alphabeta_decision
from Position import Position
from copy import deepcopy


class AlphaBeta:

	bestGridBoxOutput = []

	def __init__(self, value,occupied_positions, player, oplayer, cutoffdepth):
		
		self.value=value
                self.occupied_positions=occupied_positions
		self.player = player
		self.oplayer = oplayer
		self.cutOffDepth = cutoffdepth
                self.zzz=evaluation(self.value,self.occupied_positions,self.player,self.oplayer)
		self.rootEvalFunction = self.zzz.eval()
                #print self.rootEvalFunction
		self.negativeInfiniti = -100000
		self.positiveInfiniti = 100000
		self.bestRootNode = None
                
		self.rootNode = alphabeta_decision(None, value,occupied_positions, player, oplayer, self.negativeInfiniti, 0, False, [], self.negativeInfiniti, None, cutoffdepth, self.negativeInfiniti, self.positiveInfiniti)
                self.rootNode.travFile()
                    
	def recursiveAlphaBeta(self, rootNodeObject):
                originalNode = deepcopy(rootNodeObject)
		if rootNodeObject.currentDepthOfNode < self.cutOffDepth:
			childNode = None
			prune = False
			flag1=False
			for i in range(0, 5):
				for j in range(0, 5):
					rootNodeObject.travFile()
					if rootNodeObject.occupied_positions[i][j] == "*" and prune == False:
						flag1=True
						if rootNodeObject.playMax == True:
							if rootNodeObject.parentNode != None:
								
								if rootNodeObject.eval_value <= rootNodeObject.parentNode.alpha:
									
									prune = True
								else:
								
									prune = False
						else:
							if rootNodeObject.parentNode != None:
								
								if rootNodeObject.eval_value >= rootNodeObject.parentNode.beta:
									
									prune = True
								else:
								
									prune = False

						if prune == True:
							
							break					
						else:
							
							pos = Position(i, j)
                                                          
							if rootNodeObject.playMax == True:
                                                                rootNodeObject.occupied_positions = deepcopy(originalNode.occupied_positions)
								childNode = alphabeta_decision(rootNodeObject, rootNodeObject.value,rootNodeObject.occupied_positions, rootNodeObject.player, rootNodeObject.oplayer, self.negativeInfiniti, rootNodeObject.currentDepthOfNode+1, False, [], rootNodeObject.value[i][j], pos, self.cutOffDepth, rootNodeObject.alpha, rootNodeObject.beta)
							else:
                                                                rootNodeObject.occupied_positions = deepcopy(originalNode.occupied_positions)
								childNode = alphabeta_decision(rootNodeObject, rootNodeObject.value,rootNodeObject.occupied_positions, rootNodeObject.player, rootNodeObject.oplayer, self.positiveInfiniti, rootNodeObject.currentDepthOfNode+1, True, [], rootNodeObject.value[i][j], pos, self.cutOffDepth, rootNodeObject.alpha, rootNodeObject.beta)
							
                                                        
                                                        childNode.travFile()
							if childNode.currentDepthOfNode == rootNodeObject.cutOffDepth:
								print rootNodeObject
								rootNodeObject.travFile()
                                                        
							rootNodeObject.childNodes.append(childNode)
							self.recursiveAlphaBeta(childNode)
			if flag1==False:
                            self.xyz=evaluation(self.value,self.occupied_positions,rootNodeObject.player,rootNodeObject.oplayer)
                            rootNodeObject.eval_value = self.xyz.eval()
			if rootNodeObject.playMax == True:
				if rootNodeObject.parentNode != None:
					if rootNodeObject.parentNode.alpha < rootNodeObject.eval_value:
                                            if rootNodeObject.parentNode.eval_value < rootNodeObject.eval_value:
						rootNodeObject.parentNode.eval_value = rootNodeObject.eval_value
                                            rootNodeObject.parentNode.eval_value = rootNodeObject.eval_value
                                            if rootNodeObject.eval_value < rootNodeObject.parentNode.beta:
						rootNodeObject.parentNode.alpha = max(rootNodeObject.eval_value, rootNodeObject.alpha)
						rootNodeObject.parentNode.bestChild = rootNodeObject.currentPosition
						#print rootNodeObject.parentNode
						

			else:
				
				if rootNodeObject.parentNode != None:
                                    if rootNodeObject.parentNode.beta >= rootNodeObject.eval_value:
					rootNodeObject.parentNode.eval_value = rootNodeObject.eval_value
                                        if rootNodeObject.parentNode.eval_value < rootNodeObject.eval_value:
                                            rootNodeObject.parentNode.eval_value = rootNodeObject.eval_value
					if rootNodeObject.eval_value > rootNodeObject.parentNode.alpha:
                                            rootNodeObject.parentNode.beta = min(rootNodeObject.eval_value, rootNodeObject.beta)
                                            rootNodeObject.parentNode.bestChild = rootNodeObject.currentPosition
		if rootNodeObject.parentNode != None:
                    rootNodeObject.parentNode.travFile()			
						
		return rootNodeObject

	def getBestRootNodeForAlphaBeta(self):
		
		
		self.bestRootNode = self.recursiveAlphaBeta(self.rootNode)
		self.rootNode.travFile()
		
		if self.bestRootNode.bestChild != None:
			i=self.bestRootNode.bestChild.rowIndex
                        j=self.bestRootNode.bestChild.columnIndex
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

			
			
		
