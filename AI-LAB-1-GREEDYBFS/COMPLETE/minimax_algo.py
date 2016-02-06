from evaluation_function import evaluation
from next_state import next_state
from minimax_decision import nextmin
from copy import deepcopy
class minimax_algo:
    pos=[]
    def __init__(self,value,occupied_positions,player,oplayer,cutt_off_depth):
        self.value=value
        self.occupied_positions=occupied_positions
        self.player=player
        self.oplayer=oplayer
        self.cutt_off_depth=cutt_off_depth
        
#        y=evaluation(self.value,self.occupied_positions,self.player,self.oplayer)
#        self.root_evaluation_function=y.eval()
        player11=0
        player22=0
        for i in range(5):
            for j in range(5):
                if(self.occupied_positions[i][j]==self.oplayer):
                    player11 += self.value[i][j]
                elif(self.occupied_positions[i][j]==self.player):
                    player22 += self.value[i][j]
        self.root_evaluation_function = (player11-player22)
        print "Calculated e(S) is %d" %(self.root_evaluation_function)
        self.negative = -100000
	self.positive = 100000
	self.bestRootNode = None
	print "Node,Depth,Value"
	self.rootNode = nextmin(None, self.value,self.occupied_positions, self.player, self.oplayer, self.negative, 0, False, [], self.negative, None, self.cutt_off_depth)
        #print "xxxxxxxxx in minimax_algo"
    
    def __str__(self):
        #print "xxxxxxxxx in minimax_algo"
	str = "---------------------------------------------------------\n"
	str += "Player = %s, Opponent = %s, E(s) = %d, cutOffDepth = %d\n" %(self.player, self.oplayer, self.root_evaluation_function, self.cutt_off_depth)
	print self.value
        print self.occupied_positions
	str += "\n"
	str += "%s" %(self.rootNode)+"\n"
	str += "---------------------------------------------------------"
	return str
            
    def __repr__(self):
	return self.__str__()
                
    
    def MiniMax(self, rootNodeObject=None):
	originalNode = deepcopy(rootNodeObject)
	if rootNodeObject.currentDepthOfNode < self.cutt_off_depth:
			# print "Main Process starts from the root game node"
            childNode = None
            #print rootNodeObject.currentDepthOfNode,"ssss"
            #print self.cutt_off_depth
            for i in range(0, 5):
                for j in range(0,5):
                    if rootNodeObject.occupied_positions[i][j] == "*":
                        pos=[i,j]
                        #print pos[0],pos[1],"i love you"
			if rootNodeObject.playMax == True:
                            rootNodeObject.occupied_positions = deepcopy(originalNode.occupied_positions)
                            childNode = nextmin(rootNodeObject, rootNodeObject.value, rootNodeObject.occupied_positions, rootNodeObject.player, rootNodeObject.oplayer, self.negative, rootNodeObject.currentDepthOfNode+1, False, [], rootNodeObject.value[i][j], pos, self.cutt_off_depth)
			else:
                            rootNodeObject.occupied_positions = deepcopy(originalNode.occupied_positions)
                            childNode = nextmin(rootNodeObject, rootNodeObject.value, rootNodeObject.occupied_positions,rootNodeObject.player, rootNodeObject.oplayer, self.positive, rootNodeObject.currentDepthOfNode+1, True, [], rootNodeObject.value[i][j], pos, self.cutt_off_depth)
						
						
			rootNodeObject.childNodes.append(childNode)
			self.MiniMax(childNode)
			print rootNodeObject
                        #print rootNodeObject.childNodes,"HELOOOOOOO"

            
            if (rootNodeObject.playMax == True):
		if rootNodeObject.parentNode != None:
                    if rootNodeObject.parentNode.evaluation_function < rootNodeObject.evaluation_function:
			rootNodeObject.parentNode.evaluation_function = rootNodeObject.evaluation_function
			rootNodeObject.parentNode.bestChild = rootNodeObject.currentPosition
            else:
		if rootNodeObject.parentNode != None:
                    if rootNodeObject.parentNode.evaluation_function >= rootNodeObject.evaluation_function:
			rootNodeObject.parentNode.evaluation_function = rootNodeObject.evaluation_function
			rootNodeObject.parentNode.bestChild = rootNodeObject.currentPosition
	#print rootNodeObject.parentNode.bestChild,"rakesh"					
        return rootNodeObject

    def RootNodeForMiniMax(self):
		
        self.bestRootNode = self.MiniMax(self.rootNode)
        #print self.bestRootNode.bestChild[0],self.bestRootNode.bestChild[1],"i love you tooo"
        #print self.bestRootNode,"heloooooooooooooooooo"
        self.occupied_positions[self.bestRootNode.bestChild[0]][self.bestRootNode.bestChild[1]] = self.player
        i=self.bestRootNode.bestChild[0]
        j=self.bestRootNode.bestChild[1]
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

        str = ""
        for i in range(0, 5):
                for j in range(0, 5):
                        str += self.occupied_positions[i][j]
                        #print "RRRRRRR"
                str += "\n"
        print str



        return "DONE"
                