
from minimax_decisions import nextmin
from Position import Position
from copy import deepcopy
from evaluation_function import evaluation
class minimax_algos:

	
	bestGridBoxOutput = []

	def __init__(self, value,occupied_positions, playerValue, opponentPlayerValue, cutOffDepthValue):
		self.gridBoxCell = []
		self.value=value
                self.occupied_positions=occupied_positions
		self.player = playerValue
		self.opponentPlayer = opponentPlayerValue
		self.cutOffDepth = cutOffDepthValue
		
                aaa=evaluation(self.value,self.occupied_positions,self.player,self.opponentPlayer)
                self.rootEvalFunction=aaa.eval()
                  
		
		self.negative = -100000
		self.positive = 100000
		self.bestRootNode = None
		print "Node,Depth,Value"
		self.rootNode = nextmin(None,value,occupied_positions, playerValue, opponentPlayerValue, self.negative, 0, False, [], self.negative, None, cutOffDepthValue)
        
	def recursiveMiniMax(self, rootNodeObject=None):
                originalNode = deepcopy(rootNodeObject)
		
		if rootNodeObject.currentDepthOfNode < self.cutOffDepth:
			
			childNode = None
			for i in range(5):
				for j in range(5):
					if rootNodeObject.occupied_positions[i][j] == "*":
						
						pos = Position(i, j)
						#print pos,"RAKESH"
						if rootNodeObject.playMax == True:
							
                                                        rootNodeObject.occupied_positions = deepcopy(originalNode.occupied_positions)
							childNode = nextmin(rootNodeObject, rootNodeObject.value,rootNodeObject.occupied_positions, rootNodeObject.player, rootNodeObject.opponentPlayer, self.negative, rootNodeObject.currentDepthOfNode+1, False, [], rootNodeObject.value[i][j], pos, self.cutOffDepth)
						else:
							
                                                        rootNodeObject.occupied_positions = deepcopy(originalNode.occupied_positions)
							childNode = nextmin(rootNodeObject, rootNodeObject.value,rootNodeObject.occupied_positions, rootNodeObject.player, rootNodeObject.opponentPlayer, self.positive, rootNodeObject.currentDepthOfNode+1, True, [], rootNodeObject.value[i][j], pos, self.cutOffDepth)
						
						rootNodeObject.childNodes.append(childNode)
						self.recursiveMiniMax(childNode)
						print rootNodeObject

			
			if rootNodeObject.playMax == True:
				if rootNodeObject.parentNode != None:
					if rootNodeObject.parentNode.currentEvalFunction < rootNodeObject.currentEvalFunction:
						rootNodeObject.parentNode.currentEvalFunction = rootNodeObject.currentEvalFunction
						rootNodeObject.parentNode.bestChild = rootNodeObject.currentPosition
						
			else:
				
				if rootNodeObject.parentNode != None:
					if rootNodeObject.parentNode.currentEvalFunction >= rootNodeObject.currentEvalFunction:
						rootNodeObject.parentNode.currentEvalFunction = rootNodeObject.currentEvalFunction
						rootNodeObject.parentNode.bestChild = rootNodeObject.currentPosition
						
		return rootNodeObject

	def NodeForMiniMax(self):
		
		self.bestRootNode = self.recursiveMiniMax(self.rootNode)
		
                i=self.bestRootNode.bestChild.rowIndex
                j=self.bestRootNode.bestChild.columnIndex
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

		return "DONE"
        