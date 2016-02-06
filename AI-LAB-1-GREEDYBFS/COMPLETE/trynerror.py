
def main():
    f = open('testcase1.txt','r')   
    value=[]
    occupied_positions=[]
    with open('testcase1.txt') as f:
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
    #print task
    #print player
    #print cutt_off_depth
    #print value
    #print occupied_positions
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
        
        for i in range(5):
            for j in range(5):
                
                if(occupied_positions[i][j]==player):
                    player1 += value[i][j]
                elif(occupied_positions[i][j]==oplayer):
                    player2 += value[i][j]
                
    
        evaluation_function=player1-player2
    
        print evaluation_function
    
    #GreedyBFS
        max_evaluation=evaluation_function
        temp=evaluation_function
        pos_i=0
        pos_j=0
        x=0
        for i in range(5):
            for j in range(5):
                if(occupied_positions[i][j]=='*'):
                    t=value[i][j]
                #print t
                    if(i!=0 and occupied_positions[i-1][j]==oplayer):                    
                        t+=value[i-1][j]
                    # occupied_positions[i-1][j]='X'
                    if(i!=4 and occupied_positions[i+1][j]==oplayer):
                        t+=value[i+1][j]
                    #occupied_positions[i+1][j]='X'
                    if(j!=4 and occupied_positions[i][j+1]==oplayer):
                        t+=value[i][j+1]
                    #occupied_positions[i][j+1]='X'
                    if(j!=0 and occupied_positions[i][j-1]==oplayer):
                        #occupied_positions[i][j-1]='X'
                        t+=value[i][j-1]
                    if(t>max_evaluation):
                        max_evaluation=t
                        pos_i=i
                        pos_j=j
                
                    
    #print pos_i,pos_j
    
        i=pos_i
        j=pos_j
        if(i!=0 and occupied_positions[i-1][j]==oplayer):
            occupied_positions[i-1][j]=player
        #print occupied_positions[i-1][j]
        if(i!=4 and occupied_positions[i+1][j]==oplayer):
            occupied_positions[i+1][j]=player
        #print occupied_positions[i+1][j]
        if(j!=0 and occupied_positions[i][j-1]==oplayer):
            occupied_positions[i][j-1]=player
        #print occupied_positions[i][j-1]
        if(j!=4 and occupied_positions[i][j+1]==oplayer):
            occupied_positions[i][j+1]=player
        #print occupied_positions[i][j+1]
           
                        
            
        print pos_i,pos_j,value[pos_i][pos_j],max_evaluation    
        evaluation_function += max_evaluation
        print evaluation_function
        occupied_positions[pos_i][pos_j]=player
        print occupied_positions
    
    
        
    
    #print content
    elif(task==2):
        print "minimax"
        
        
        
        
        
        
        
        
        
        
        
    elif(task==3):
        print "alphabeta"
    
    r1 = open('next_state.txt','w+')
    for i in range(5):
        for j in range(5):
            r1.write(occupied_positions[i][j])
        r1.write("\n")    
    r1.close()
    
    f.close()

if __name__ == "__main__":
  main()
  '''

  '''