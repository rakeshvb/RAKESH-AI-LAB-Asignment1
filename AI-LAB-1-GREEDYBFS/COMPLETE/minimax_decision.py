from evaluation_function import evaluation
from copy import deepcopy
class nextmin:
    bestgrid=[]
    negativeInfinity = -100000
    positiveInfinity = 100000
    
    def __init__(self,parentNodeObject,value,occupied_positions,player,oplayer,evaluation_function,currentDepthOfNode, playMax, childNodesValue, currentValue, currentPosition,cutt_off_depth):
        #print "xxxxxxxxx"
        self.value=value
        self.occupied_positions = occupied_positions
        self.player=player
        self.oplayer=oplayer
        self.evaluation_function=evaluation_function
        self.cutt_off_depth=cutt_off_depth
        
        self.parentNode = None
	self.currentDepthOfNode = currentDepthOfNode
        #print self.currentDepthOfNode,"fuck minimax fuck minimax"
	self.playMax = playMax
	self.childNodes = []
	self.currentValue = currentValue
	self.currentPosition = currentPosition
        
        #print self.currentPosition
	self.bestChild = None
	self.bestBox = []
        #print "xxxxxxxxx"
        if(parentNodeObject != None):
            self.parentNode = parentNodeObject
            #print "Parent Node Object in constructor is "
            #print parentNodeObject.evaluation_function
            #print "xxxxxxxxx"
	for i in range(0, len(childNodesValue)):
            self.childNodes.append(childNodesValue[i])
        #print self.childNodes
        if currentPosition != None:
            self.currentPosition = currentPosition
            #print "xxxxxxxxx"
            #print self.currentPosition
            #print self.playMax,"$$$$$$$$$$$$$$$$$$$$",self.parentNode
            self.currentValue = self.value[self.currentPosition[0]][self.currentPosition[1]]
            #print self.currentValue,"rakesh bora ggggggggggggggggggggggg"
            if self.playMax == True and self.parentNode != None:
                
                i=self.currentPosition[0]
                j=self.currentPosition[1]
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
                    #print occupied_positions[i][j+1]
                    #                y=evaluation(value,occupied_positions,player,oplayer)
                
                    #                for i in range(5):
                    #                    for j in range(5):
                    #                        print self.occupied_positions[i][j],
                    #                    print
                #print self.currentDepthOfNode,"***** Current vs cut off *****",self.cutt_off_depth, "Play Max = ", self.playMax
                self.evaluation_function=0
                player1=0
                player2=0
                for i in range(5):
                    for j in range(5):
                        if(self.occupied_positions[i][j]==self.player):
                            player1 += self.value[i][j]
                        elif(self.occupied_positions[i][j]==self.oplayer):
                            player2 += self.value[i][j]
                self.evaluation_function = (player1-player2)
                #z=evaluation(self.parentNode.value,self.parentNode.occupied_positions,self.parentNode.player,self.parentNode.oplayer)
                #self.parentNode.evaluation_function=z.eval()
                #/print self.playMax,"hi hi hi hi hi",self.parentNode
                if ((self.parentNode.evaluation_function < self.evaluation_function) and 
                (self.currentDepthOfNode == self.cutt_off_depth)):
#                    print "maximizing parent %s " %(self.parentNode)
                    #print "to to to to  "
                    self.parentNode.evaluation_function = self.evaluation_function
                    self.parentNode.bestChild = currentPosition
                    #self.parentNode.bestBox = self.occupied_positions
                    self.parentNode.bestBox = deepcopy(self.occupied_positions)
                    nextmin.bestGrid = deepcopy(self.occupied_positions)
                    #print self.parentNode.bestChild,"rakesh vijay bora usc usc usc"

            elif self.playMax == False and self.parentNode != None:
                #print self.currentDepthOfNode,"***** Current vs cut off *****",self.cutt_off_depth
                i=self.currentPosition[0]
                j=self.currentPosition[1]
                self.occupied_positions[i][j]=self.oplayer
                
                if((i!=0 and self.occupied_positions[i-1][j]==self.player) and ((i!=4 and self.occupied_positions[i+1][j]==self.oplayer) or (j!=0 and self.occupied_positions[i][j-1]==self.oplayer) or (j!=4 and self.occupied_positions[i][j+1]==self.oplayer))):
                    self.occupied_positions[i-1][j]=self.oplayer
                    #print occupied_positions[i-1][j]
                if((i!=4 and self.occupied_positions[i+1][j]==self.player) and ((i!=0 and self.occupied_positions[i-1][j]==self.oplayer) or (j!=0 and self.occupied_positions[i][j-1]==self.oplayer) or (j!=4 and self.occupied_positions[i][j+1]==self.oplayer))):
                    self.occupied_positions[i+1][j]=self.oplayer
                    #print occupied_positions[i+1][j]
                if((j!=4 and self.occupied_positions[i][j+1]==self.player) and ((i!=4 and self.occupied_positions[i+1][j]==self.oplayer) or (i!=0 and self.occupied_positions[i-1][j]==self.oplayer) or (j!=0 and self.occupied_positions[i][j-1]==self.oplayer))):
                    self.occupied_positions[i][j+1]=self.oplayer
                    #print occupied_positions[i][j-1]
                if((j!=0 and self.occupied_positions[i][j-1]==self.player) and ((i!=4 and self.occupied_positions[i+1][j]==self.oplayer)or (i!=0 and self.occupied_positions[i-1][j]==self.oplayer) or (j!=4 and self.occupied_positions[i][j+1]==self.oplayer))):
                    self.occupied_positions[i][j-1]=self.oplayer
                    #print occupied_positions[i][j+1]
                    #y=evaluation(value,occupied_positions,player,oplayer)
                
                
                self.evaluation_function=0
                player11=0
                player22=0
                for i in range(5):
                    for j in range(5):
                        if(self.occupied_positions[i][j]==self.player):
                            player11 += self.value[i][j]
                        elif(self.occupied_positions[i][j]==self.oplayer):
                            player22 += self.value[i][j]
                self.evaluation_function = (player11-player22)
                print "Calculated e(S) is %d" %(self.evaluation_function)

                #z=evaluation(self.parentNode.value,self.parentNode.occupied_positions,self.parentNode.player,self.parentNode.oplayer)
                #self.parentNode.evaluation_function=z.eval()
#                print self.parentNode.evaluation_function,self.evaluation_function,self.currentDepthOfNode,"RAKESH BORA IS MY fucking NAME",self.cutt_off_depth
                if self.parentNode.evaluation_function >= self.evaluation_function and self.parentNode != None and self.currentDepthOfNode == self.cutt_off_depth:
#                    print "minimizing parent %s " %(self.parentNode)
                    self.parentNode.evaluation_function = self.evaluation_function
                    self.parentNo = currentPosition
                    #self.parentNode.bestBox = self.occupied_positions
                    self.parentNode.bestBox = deepcopy(self.occupied_positions)
                    nextmin.bestGrid = deepcopy(self.occupied_positions) 
                            #print self.parentNode.bestChild,"rakesh vijay bora USC USC USC"
					
	if(self.parentNode == None):
            print self
            #print "xxxxxxxxx1111111"
	else:
            print self.parentNode

	
	

    def __str__(self):
	
		columnDict = {0:'A', 1:'B', 2:'C', 3:'D', 4:'E'}
		rowDict = {0:1, 1:2, 2:3, 3:4, 4:5}

		str = ""
                #print "xxxxxxxxx0000000"
		if self.parentNode == None:
			str += "root,"
		else:
			# str += "%s," %(self.currentPosition)
			if self.currentPosition != None:
				str += "%s%d," %(columnDict[self.currentPosition[0]], rowDict[self.currentPosition[1]])
		#print "xxxxxxxxx0000000"
		currentEvalFunctionString = ""
		if (self.evaluation_function == nextmin.negativeInfinity) or (self.bestChild == None and self.playMax == False and self.currentDepthOfNode != self.cutt_off_depth):
			currentEvalFunctionString = "-Infinity"
		elif self.evaluation_function == nextmin.positiveInfinity or (self.bestChild == None and self.playMax == True and self.currentDepthOfNode != self.cutt_off_depth):
			currentEvalFunctionString = "Infinity"
		else:
			currentEvalFunctionString = "%s" %(self.evaluation_function)
                #print self.evaluation_function
		str += "%d,%s" %(self.currentDepthOfNode, currentEvalFunctionString)
		#print "xxxxxxxxx00000001111111111"
                return str

    def __repr__(self):
        return self.__str__()                
        
                    