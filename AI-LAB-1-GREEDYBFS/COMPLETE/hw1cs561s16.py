from evaluation_function import evaluation
from next_state import next_state
from minimax_decisions import nextmin
from minimax_algos import minimax_algos
from playcontinue import playcontinue
from alphabeta_algo import AlphaBeta
from alphabeta_decision import alphabeta_decision
import sys
#def playcon(occupied_positions):
#    playcon=False
#    occupied_positions=occupied_positions
#    for i in range(5):
#        for j in range(5):
#            if occupied_positions=='*':
#                playcon=True
#                break
#    return playcon
def main():
    count=0
    playcon=True
    global firstplayer
    global secondplayer
    global firstplayer_algo
    global firstplayer_depth
    global secondplayer_algo
    global secondplayer_depth
    player=""
    oplayer=""
    cutt_off_depth=0
    firstplayer=""
    secondplayer=""
    firstplayer_algo=0
    firstplayer_depth=0
    secondplayer_algo=0
    secondplayer_depth=0
    turn1=1
    zaza=0
    fileName = ""
# Read File Name
    for a in range(len(sys.argv)):
	if sys.argv[a] == "-i":
		fileName = sys.argv[a+1]
		break;
    f = open(fileName,'r')   
    value=[]
    occupied_positions=[]
    with open(fileName, 'r') as f:
        line=f.readline().rstrip()
        if(int(line)<4):
            task=int(line)
            for i in range(1,13):
                line=f.readline().rstrip()
                if(i==1):
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
        else:
            task=int(line)
            
            # print occupiedList, " before for loop"
            for i in range(1, 17):
                line = f.readline().rstrip()
                # print "Line read is ", line, " i is, ", i
                if i == 1:
                        firstplayer = line
                elif i == 2:
                        firstplayer_algo = int(line)
                elif i == 3:
                        firstplayer_depth = int(line)
                if i == 4:
                        secondplayer = line
                elif i == 5:
                        secondplayer_algo = int(line)
                elif i == 6:
                        secondplayer_depth = int(line)
                elif i <= 11 and i >= 7:
                        ls=[]
                        ls=map(int,line.split())
                        value.append(ls)
                elif i >= 12 and i <= 17:
                        occ=[]
                        for c in line:
                            occ.append(c)
                        occupied_positions.append(occ)
    playerX='X'
    PlayerO='O'
    #print occupied_positions
    
    #print player,oplayer    
    if(task==1):
        if(player==playerX):
            oplayer='O'
        else:
            oplayer='X'
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
        if(player==playerX):
            oplayer='O'
        else:
            oplayer='X'
        nx=minimax_algos(value,occupied_positions,player,oplayer,cutt_off_depth)
        nx.NodeForMiniMax()    
                    
            
        
        
        
        
    elif(task==3):
        if(player==playerX):
            oplayer='O'
        else:
            oplayer='X'
        nxx=AlphaBeta(value,occupied_positions,player,oplayer,cutt_off_depth)
        nxx.getBestRootNodeForAlphaBeta()
#        print "alphabeta"
    elif(task==4):
        i=0
        for i in range(5):
            for j in range(5):
                if occupied_positions[i][j]=='*':
                    count+=1
        while(i<=count):
            i+=1
            if turn1 == 1:
                if firstplayer_algo == 1:
                    y1=evaluation(value,occupied_positions,firstplayer,secondplayer)
                    evaluation_function=y1.eval()
                    z1=next_state(value,occupied_positions,firstplayer,secondplayer,evaluation_function)
                    occupied_positions=z1.state()
                    y2=evaluation(value,occupied_positions,firstplayer,secondplayer)
                    evaluation_function=y2.eval()
                    rz = open('trace_state.txt','a+')
                    for i in range(5):
                        for j in range(5):
                            rz.write(occupied_positions[i][j])
                       
                        rz.write("\n")
                       
                    
                elif firstplayer_algo == 2:
                    nx=minimax_algos(value,occupied_positions,firstplayer,secondplayer,firstplayer_depth)
                    nx.NodeForMiniMax()
                    rz = open('trace_state.txt','a+')
                    for i in range(5):
                        for j in range(5):
                            rz.write(occupied_positions[i][j])
                       
                        rz.write("\n")
                       
                elif firstplayer_algo == 3:
                    nxx=AlphaBeta(value,occupied_positions,firstplayer,secondplayer,firstplayer_depth)
                    nxx.getBestRootNodeForAlphaBeta()
                    rz = open('trace_state.txt','a+')
                    for i in range(5):
                        for j in range(5):
                            rz.write(occupied_positions[i][j])
                            
                        rz.write("\n")
                       
                turn1=2
            elif turn1==2:
                if secondplayer_algo == 1:
                    y3=evaluation(value,occupied_positions,secondplayer,firstplayer)
                    evaluation_function=y4.eval()
                    z3=next_state(value,occupied_positions,secondplayer,firstplayer,evaluation_function)
                    occupied_positions=z3.state()
                    y4=evaluation(value,occupied_positions,secondplayer,firstplayer)
                    evaluation_function=y4.eval()
                    for i in range(5):
                        for j in range(5):
                            rz.write(occupied_positions[i][j])
                        rz.write("\n")

                elif secondplayer_algo == 2:
                    nx=minimax_algos(value,occupied_positions,secondplayer,firstplayer,secondplayer_depth)
                    nx.NodeForMiniMax()
                    rz = open('trace_state.txt','a+')
                    for i in range(5):
                        for j in range(5):
                            rz.write(occupied_positions[i][j])
                        rz.write("\n")
                        
                    
                elif secondplayer_algo == 3:
                    nxx=AlphaBeta(value,occupied_positions,secondplayer,firstplayer,secondplayer_depth)
                    nxx.getBestRootNodeForAlphaBeta()
                    rz = open('trace_state.txt','a+')
                    for i in range(5):
                        for j in range(5):
                            rz.write(occupied_positions[i][j])
                        rz.write("\n")
                        
                turn1=1
            
            
            
                             
                
                    
    
    r1 = open('next_state.txt','w+')
    for i in range(5):
        for j in range(5):
            r1.write(occupied_positions[i][j])
        r1.write("\n")    
    r1.close()
    rz.close()
    f.close()

if __name__ == "__main__":
    main()