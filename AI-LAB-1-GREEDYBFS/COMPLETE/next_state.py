from evaluation_function import evaluation
class next_state:
    def __init__(self,value,occupied_positions,player,oplayer,evaluation_function):
        self.value=value
        self.occupied_positions=occupied_positions
        self.player=player
        self.oplayer=oplayer
        self.evaluation_function=evaluation_function
        
    def state(self):
        #GreedyBFS
        max_evaluation=self.evaluation_function
        temp=self.evaluation_function
        pos_i=0
        pos_j=0
        t=0
        for i in range(5):
            for j in range(5):
                #t=temp
                if(self.occupied_positions[i][j]=='*'):
                    t=self.value[i][j]
                #print t
                    if((i!=0 and self.occupied_positions[i-1][j]==self.oplayer) and ((i!=4 and self.occupied_positions[i+1][j]==self.player) or (j!=0 and self.occupied_positions[i][j-1]==self.player) or (j!=4 and self.occupied_positions[i][j+1]==self.player))):
                        t+=self.value[i-1][j]
                        #y=evaluation(self.value,self.occupied_positions,self.player,self.oplayer)
                        #evaluation_function=y.eval()
                        #evaluation_function-=t
                    # occupied_positions[i-1][j]='X'
                    if((i!=4 and self.occupied_positions[i+1][j]==self.oplayer) and ((i!=0 and self.occupied_positions[i-1][j]==self.player) or (j!=0 and self.occupied_positions[i][j-1]==self.player) or (j!=4 and self.occupied_positions[i][j+1]==self.player))):
                        t+=self.value[i+1][j]
                    #occupied_positions[i+1][j]='X'
                    if((j!=4 and self.occupied_positions[i][j+1]==self.oplayer) and ((i!=4 and self.occupied_positions[i+1][j]==self.player) or (i!=0 and self.occupied_positions[i-1][j]==self.player) or (j!=0 and self.occupied_positions[i][j-1]==self.player) )):
                        t+=self.value[i][j+1]
                    #occupied_positions[i][j+1]='X'
                    if((j!=0 and self.occupied_positions[i][j-1]==self.oplayer) and ((i!=4 and self.occupied_positions[i+1][j]==self.player)or (i!=0 and self.occupied_positions[i-1][j]==self.player) or (j!=4 and self.occupied_positions[i][j+1]==self.player))):
                        #occupied_positions[i][j-1]='X'
                        t+=self.value[i][j-1]
                    if(t>max_evaluation):
                        max_evaluation=t
                        pos_i=i
                        pos_j=j
                
                    
#        print pos_i,pos_j
    
        i=pos_i
        j=pos_j
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
           
                        
            
#        print pos_i,pos_j,self.value[pos_i][pos_j],max_evaluation    
        self.evaluation_function += max_evaluation
        #print self.evaluation_function
        self.occupied_positions[pos_i][pos_j]=self.player
        return self.occupied_positions
        