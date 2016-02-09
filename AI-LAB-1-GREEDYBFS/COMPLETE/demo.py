from BoxCell import BoxCell
from GreedyBestFirstSearch_HW1 import GreedyBestFirstSearch
from MiniMax import MiniMax
import sys
from AlphaBetaPruning import AlphaBeta
from copy import deepcopy

# Variable declarations
algoToBeUsed = 0
player = ""
opponentPlayer = ""
player1 = "X"
player2 = "O"
cutOffDepth = 0

stateBox = []
values = []
occupiedList = []

firstPlayer = ""
firstPlayerAlgoToBeUsed = 0
firstPlayerCutOffDepth = 0
secondPlayer = ""
secondPlayerAlgoToBeUsed = 0
secondPlayerCutOffDepth = 0


# Methods
def readFile(fileName):
	global algoToBeUsed
	global player
	global cutOffDepth
	global opponentPlayer

	global firstPlayer, firstPlayerAlgoToBeUsed, firstPlayerCutOffDepth
	global secondPlayer, secondPlayerAlgoToBeUsed, secondPlayerCutOffDepth
	global values
	global occupiedList

	with open(fileName,'r') as f:
		# while True:
	    	
    	# print i
		line = f.readline().rstrip()
		# print "Line read in the for loop is : ", line
    	# print line
    	if (int(line)) == 4:
	    	algoToBeUsed = 4
	    	# print "Work for full bettle simulation"
	    	inputFile = open(fileName, 'r')
    		line = inputFile.readline().rstrip()
    		algoToBeUsed = int(line)
    		occupiedList = []
    		# print occupiedList, " before for loop"
    		for i in range(1, 17):
    			line = inputFile.readline().rstrip()
    			# print "Line read is ", line, " i is, ", i
    			if i == 1:
    				firstPlayer = line
    			elif i == 2:
    				firstPlayerAlgoToBeUsed = int(line)
    			elif i == 3:
    				firstPlayerCutOffDepth = int(line)
    			if i == 4:
    				secondPlayer = line
    			elif i == 5:
    				secondPlayerAlgoToBeUsed = int(line)
    			elif i == 6:
    				secondPlayerCutOffDepth = int(line)
    			elif i <= 11 and i >= 7:
    				inputList = list(map(int, line.split()))
		    		values.append(inputList)
		    	elif i >= 12 and i <= 17:
		    		occupiedByList = []
		    		for c in line:
		    			occupiedByList.append(c)
		    		occupiedList.append(occupiedByList)
		    		print "appended ", occupiedByList, " to the occupiedList\nSize of occupiedList is ", len(occupiedList)


    	elif (int(line)) < 4 : 
    		inputFile = open(fileName, 'r')
    		line = inputFile.readline().rstrip()
    		algoToBeUsed = int(line)
    		# print "We will use ", algoToBeUsed
    		for i in range(1, 13):
    			line = inputFile.readline().rstrip()
    			# print "Line read in the for loop is : ", line
		    	if i == 1:
		    		player = line
		    		# print "Our player is ", player
		    	elif i == 2:
		    		cutOffDepth = int(line)
		    		# print "Our cutOffDepth is ", cutOffDepth
		    	elif i <= 7:
		    		inputList = list(map(int, line.split()))
		    		values.append(inputList)
		    		# print "appended ", inputList, " to the values"
		    	else:
		    		occupiedByList = []
		    		for c in line:
		    			occupiedByList.append(c)
		    		occupiedList.append(occupiedByList)
		    		
    	else:
	    	print "Invalid Input"
		f.close()

def canWeContinuePlaying():
	continueGame = False
	for i in range(0, len(stateBox)):
		for j in range(0, len(stateBox)):
			if stateBox[i][j].occupiedBy == "*":
				continueGame = True
				break
	return continueGame

def printTraceLog():
	global traceLogOutputFile
	traceLogOutputFile = open("trace_state.txt", 'a+')
	str = ""
	for i in range(0, len(stateBox)):
		for j in range(0, len(stateBox)):
			str += stateBox[i][j].occupiedBy
		str += "\n"
	# print str
	traceLogOutputFile.write(str)
	traceLogOutputFile.close()

	

# Main section
fileName = ""
# Read File Name
for a in range(len(sys.argv)):
	if sys.argv[a] == "-i":
		fileName = sys.argv[a+1]
		break;

# Read file and initialize the input parameters
readFile(fileName)

print "After reading file"
print values
print occupiedList
print "Now processing input"
for i in range(0, len(values)):
	stateBox.append([])
	for j in range(0, len(values)):
		b = BoxCell(values[i][j], occupiedList[i][j])
		stateBox[i].append(b)


# for i in range(0,5):
# 	print stateBox[i]
# print len(stateBox)
if player == player1:
	opponentPlayer = player2
else:
	opponentPlayer = player1

if algoToBeUsed == 1:
	g = GreedyBestFirstSearch()

	for i in range(0, 5):
		g.inputStateBoxForClass.append([])
		for j in range(0, 5):
			b = BoxCell(values[i][j], occupiedList[i][j])
			g.inputStateBoxForClass[i].append(b)

	stateBox = g.greedyBestFirstSearchNextState(stateBox, player, opponentPlayer)
	outputFile = open('next_state.txt','w+')
	for i in range(0,5):
		str = ""
		for j in range(0,5):
			str += GreedyBestFirstSearch.bestNewStateToSelect[i][j].occupiedBy
		outputFile.write(str)
		outputFile.write("\n")


	# storeNextStateToFile("next_state.txt")
elif algoToBeUsed == 2:
	# print "Go for Minimax"
	miniMax = MiniMax(stateBox, player, opponentPlayer, cutOffDepth)
	# print miniMax
	miniMax.getBestRootNodeForMiniMax()

elif algoToBeUsed == 3:
	# print "AlphaBeta"
	alphabeta = AlphaBeta(stateBox, player, opponentPlayer, cutOffDepth)
	alphabeta.getBestRootNodeForAlphaBeta()

elif algoToBeUsed == 4:
	outputFile = open("trace_state.txt", 'w')
	outputFile.seek(0)
	outputFile.truncate()
	print "first player details ", firstPlayer, firstPlayerAlgoToBeUsed, firstPlayerCutOffDepth
	print "second player details ", secondPlayer, secondPlayerAlgoToBeUsed, secondPlayerCutOffDepth

	whoseTurnIsIt = 1
	while(canWeContinuePlaying() == True):
		if whoseTurnIsIt == 1:
			if firstPlayerAlgoToBeUsed == 1:
				# Greedy
				g = GreedyBestFirstSearch()
				g.inputStateBoxForClass = deepcopy(stateBox)
				stateBox = g.greedyBestFirstSearchNextState(stateBox, firstPlayer, secondPlayer)
				print "Greedy O/P ", firstPlayer, " VS ", secondPlayer				
				for i in range(0, len(stateBox)):
					print stateBox[i]
				print "************"
			elif firstPlayerAlgoToBeUsed == 2:
				print "Minimax"
				miniMax = MiniMax(stateBox, firstPlayer, secondPlayer, firstPlayerCutOffDepth)
				stateBox = miniMax.getBestRootNodeForMiniMax()
				print "MiniMax O/P ", firstPlayer, " VS ", secondPlayer
				for i in range(0, len(stateBox)):
					print stateBox[i]
				print "************"
			elif firstPlayerAlgoToBeUsed == 3:
				print "# AlphaBeta"
				alphabeta = AlphaBeta(stateBox, firstPlayer, secondPlayer, firstPlayerCutOffDepth)
				stateBox = alphabeta.getBestRootNodeForAlphaBeta()
				print "AlphaBeta O/P ", firstPlayer, " VS ", secondPlayer
				for i in range(0, len(stateBox)):
					print stateBox[i]
				print "************"
			whoseTurnIsIt = 2
		elif whoseTurnIsIt == 2:
			if secondPlayerAlgoToBeUsed == 1:
				# Greedy
				g = GreedyBestFirstSearch()
				g.inputStateBoxForClass = deepcopy(stateBox)
				stateBox = g.greedyBestFirstSearchNextState(stateBox, secondPlayer, firstPlayer)
				print "Greedy O/P ", secondPlayer, " VS ", firstPlayer
				for i in range(0, len(stateBox)):
					print stateBox[i]
				print "************"
			elif secondPlayerAlgoToBeUsed == 2:
				print "# Minimax"
				miniMax = MiniMax(stateBox, secondPlayer, firstPlayer, secondPlayerCutOffDepth)
				stateBox = miniMax.getBestRootNodeForMiniMax()
				print "MiniMax O/P ", secondPlayer, " VS ", firstPlayer
				for i in range(0, len(stateBox)):
					print stateBox[i]
				print "************"
			elif secondPlayerAlgoToBeUsed == 3:
				print "# AlphaBeta"
				alphabeta = AlphaBeta(stateBox, secondPlayer, firstPlayer, secondPlayerCutOffDepth)
				stateBox = alphabeta.getBestRootNodeForAlphaBeta()
				print "AlphaBeta O/P ", secondPlayer, " VS ", firstPlayer
				for i in range(0, len(stateBox)):
					print stateBox[i]
				print "************"
				
			whoseTurnIsIt = 1
		printTraceLog()

	print "Final O/P ", secondPlayer, " VS ", firstPlayer
	str = ""
	for i in range(0, len(stateBox)):
		for j in range(0, len(stateBox)):
			str += stateBox[i][j].occupiedBy
		str += "\n"
	print str
	print "************"
	# traceLogOutputFile.close()