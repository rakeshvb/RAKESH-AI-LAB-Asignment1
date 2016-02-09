from evaluation_function import evaluation
from next_state import next_state
from minimax_decisions import nextmin
from minimax_algos import minimax_algos

from alphabeta_algo import AlphaBeta
from alphabeta_decision import alphabeta_decision
import sys

def main():
    
    fileName = ""
# Read File Name
    for a in range(len(sys.argv)):
	if sys.argv[a] == "-i":
		fileName = sys.argv[a+1]
		break;
    #f = open('testcase1.txt','r')   
    value=[]
    occupied_positions=[]
    with open(fileName, 'r') as f:
        for i in range(0,13):
            line=f.readline().rstrip()
            if(i==0):
                task=int(line)
                #print task
            elif(i==1):
                player=line
            elif(i==2):
                cutt_off_depth=int(line)
                if cutt_off_depth==0:
                    print "depth not accepted" 
                    sys.exit()
            elif(i>2 and i<=7):
                ls=[]
                ls=map(int,line.split())
                value.append(ls)
            elif(i>7):
                occ=[]
                for c in line:
                    occ.append(c)
                occupied_positions.append(occ)
    
    playerX='X'
    PlayerO='O'
    #print occupied_positions
    if(player==playerX):
        oplayer='O'
    else:
        oplayer='X'
    #print player,oplayer    
    if(task==1):
        evaluation_function=0
        maxi=0
        player1=0
        player2=0
        y=evaluation(value,occupied_positions,player,oplayer)
        evaluation_function=y.eval()
    
#        print evaluation_function
    
        z=next_state(value,occupied_positions,player,oplayer,evaluation_function)
        occupied_positions=z.state()
        y=evaluation(value,occupied_positions,player,oplayer)
        evaluation_function=y.eval()
        
#        print occupied_positions
#        print evaluation_function
#    
    #print content
    elif(task==2):

        nx=minimax_algos(value,occupied_positions,player,oplayer,cutt_off_depth)
        nx.NodeForMiniMax()    
                    
            
        
        
        
        
    elif(task==3):
        nxx=AlphaBeta(value,occupied_positions,player,oplayer,cutt_off_depth)
        nxx.getBestRootNodeForAlphaBeta()
#        print "alphabeta"

    r1 = open('next_state.txt','w+')
    for i in range(5):
        for j in range(5):
            r1.write(occupied_positions[i][j])
        r1.write("\n")    
    r1.close()
    
    f.close()

if __name__ == "__main__":
    main()