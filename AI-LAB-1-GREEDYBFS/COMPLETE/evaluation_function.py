class evaluation:
    
    
    def __init__(self,value,occupied_positions,player,oplayer):
        self.value1=value
        self.occupied_positions1=occupied_positions
        self.player1=player
        self.oplayer1=oplayer
        
    def eval(self):
        
        player11=0
        player22=0
        for i in range(0,5):
            for j in range(0,5):
                if(self.occupied_positions1[i][j]==self.player1):
                    player11 += self.value1[i][j]
                elif(self.occupied_positions1[i][j]==self.oplayer1):
                    player22 += self.value1[i][j]
        return(player11-player22)
        
        
        