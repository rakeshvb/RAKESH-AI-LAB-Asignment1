class alphabeta:
    def __init__(self,rootnode, value,occupied_positions, playerValue, opponentPlayerValue, cutt_off_depth,alpha,beta,playmax):
        self.value=value
        self.occupied_positions=occupied_positions
        self.player=playerValue
        self.opponentPlayer=opponentPlayer
        self.cutt_of_depth=cutt_depth_depth
        self.alpha=alpha
        self.beta=beta
        self.playmax=playmax
        self.rootnode=rootnode
        if playmax==True:
            self.v=-100000
            for child in childnodes:
                self.v=max(self.v,alphabeta(child,rootnode, value,occupied_positions, playerValue, opponentPlayerValue, cutt_off_depth-1,alpha,beta,False))
                self.alpha=max(self.alpha,self.v)
                if self.beta<=self.alpha :
                    break
                return self.v
        else:
            self.v=100000
            for child in childnodes:
                self.v=min(self.v,alphabeta(child,rootnode, value,occupied_positions, playerValue, opponentPlayerValue, cutt_off_depth-1,alpha,beta,True))
                self.alpha=min(self.beta,self.v)
                if self.beta<=self.alpha :
                    break
                return self.v