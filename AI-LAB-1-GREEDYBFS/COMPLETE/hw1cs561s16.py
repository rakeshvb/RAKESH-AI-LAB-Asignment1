from evaluation_function import evaluation
from next_state import next_state
from minimax_decision import nextmin
from minimax_algo import minimax_algo
import sys
#from minimaxalgo import minimaxalgo
#from decisionmin import nextmin
def main():
    
    fileName = ""
# Read File Name
    for a in range(len(sys.argv)):
	if sys.argv[a] == "-i":
		fileName = sys.argv[a+1]
		break;
#    f = open('testcase1.txt','r')   
    value=[]
    occupied_positions=[]
    with open(fileName, 'r') as f:
        for i in range(0,13):
            line=f.readline().rstrip()
            if(i==0):
                task=int(line)
            elif(i==1):
                player=line
            elif(i==2):
                cutt_off_depth=int(line)
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
        #print "minimax"
        #for cut in range(cutt_off_depth):
            #for i in range(5):
             #   for j in range(5):
              #      print y
               #     if(occupied_positions[i][j]=='*'):
                #        occupied_postions[i][j]=player
            
                 #       nextmin=nextmin(value,occupied_positions,player,oplayer,evaluation_function,cutt_off_depth)
#        for i in range(5):
#            for j in range(5):
#                print value[i][j],
#            print     
        nx=minimax_algo(value,occupied_positions,player,oplayer,cutt_off_depth)
        nx.RootNodeForMiniMax()    
        '''
        parentNodeObject,value,occupied_positions,player,oplayer,evaluation_function,cutt_off_depth, 
        currentDepthOfNode, playMaxValue, childNodes, currentValue, currentPosition
            function MINIMAX-DECISION(state) returns an action
return argmax
a ? ACTIONS(s) MIN-VALUE(RESULT(state, a))
function MAX-VALUE(state) returns a utility value
if TERMINAL-TEST(state) then return UTILITY(state)
v ???
for each a in ACTIONS(state) do
v ?MAX(v, MIN-VALUE(RESULT(s, a)))
return v
function MIN-VALUE(state) returns a utility value
if TERMINAL-TEST(state) then return UTILITY(state)
v??
for each a in ACTIONS(state) do
v ?MIN(v, MAX-VALUE(RESULT(s, a)))
return v
            '''            
                    
            
        
        
        
        
    elif(task==3):
#        print "alphabeta"
        '''
        function ALPHA-BETA-SEARCH(state) returns an action
v ?MAX-VALUE(state,??,+?)
return the action in ACTIONS(state) with value v
function MAX-VALUE(state,?, ?) returns a utility value
if TERMINAL-TEST(state) then return UTILITY(state)
v ???
for each a in ACTIONS(state) do
v ?MAX(v, MIN-VALUE(RESULT(s,a),?, ?))
if v ? ? then return v
??MAX(?, v)
return v
function MIN-VALUE(state,?, ?) returns a utility value
if TERMINAL-TEST(state) then return UTILITY(state)
v ?+?
for each a in ACTIONS(state) do
v ?MIN(v, MAX-VALUE(RESULT(s,a) ,?, ?))
if v ? ? then return v
??MIN(?, v)
return v
        '''
    
    r1 = open('next_state.txt','w+')
    for i in range(5):
        for j in range(5):
            r1.write(occupied_positions[i][j])
        r1.write("\n")    
    r1.close()
    
    f.close()

if __name__ == "__main__":
    main()