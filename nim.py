#TwentyOne v1.2
#09/14

class Game21():

    def __init__(self,end,period):
        '''Create classifier using train, the name of an input
        training file.
        '''
        self.twentyOne()
        self.learn(train) # loads train data, fills prob. table
        self.n = end
        self.d = period

	#self.n = int(ask("Ready to start a game! What is the end number?"))
			#Game21(sys.argv[1])
	#self.d = int(ask("What is the maximum increment?"))

	def f():
	    x = self.n%(self.d+1)-1
	    if x == -1:
	        return self.d
	    else:
	        return x
	    
	def qAdds(pChoice):
	    return self.d+1 - pChoice
	    
	def twentyOne():
	    print("Whoever hits ", self.n, " or higher loses.")
	    print("We will now flip a coin to see who starts...")
	    if f() == 0:
	        print("Player goes first!")
	        print("Starting number is 0")
	        pTurn(0)
	    else:
	        print("Computer goes first!")
	        print("Starting number is 0")
	        qTurn(0, 0)
	    
	def qTurn(count, pChoice):
	    if pChoice == 0:
	        qChoice = f()
	    else:
	        qChoice = qAdds(pChoice)
	    count = qChoice + count
	    print("Computer adds ", qChoice, "to ", count - qChoice, " to make ", count)
	    if count >= self.n:
	        bust("Player")
	    else:
	        pTurn(count)
	        
	def pTurn(count):
	    pChoice = int(input("How much do you want to add?(1, 2, 3... up to d)"))
	    while pChoice > self.d or pChoice < 1:
	        pChoice = int(input("Choose a legal number you cheater!"))
	    count = pChoice + count
	    print("Player adds ", pChoice, "to ", count - pChoice, " to make ",count)
	    if count >= self.n:
	        bust("Computer")
	    else:
	        qTurn(count, pChoice)
	    
	def bust(string):
	    print("GameOver! ", string, " wins!!!")

def main():
       gamer = Game21(sys.argv[1],sys.argv[2])
    gamer.twentyOne()


if __name__ == "__main__":
    main()1

"""
EXPLANATION:
Variable definitions:
    n = final number, whoever chooses it or higher loses
    d = maximum increment, one can add x to count if
        0 < x < d +1
    pChoice = opponents last choice for x (reference above)
    

Each of the following rules decide the winner.
They are ordered in priority:

1. If n%(d+1)-1 is zero, winner goes second
    a.  else, winner goes first.
2. First choice is n%(d+1)-1 Unless
    a. the result is -1. In such case, the
        first choice d.
3. Following choices are d+1 - pChoice
    until the game ends.
"""