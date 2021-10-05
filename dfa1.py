# Python3 program to implement DFA that accepts
# all Stringing which follow the language
# L = {(a+b)*ab }

# This function is for the dfa = starting
# dfa = state (zeroth) of DFA
def start(c):
        if (c == 'a'):
                dfa = 1
        elif (c == 'b'):
                dfa = 0

        # -1 is used to check for any
        # invalid symbol
        else:
                dfa = -1
        return dfa

# This function is for the first
# dfa = state of DFA
def state1(c):
        if (c == 'a'):
                dfa = 1
        elif (c == 'b'):
                dfa = 2
        else:
                dfa = -1
        return dfa

# This function is for the second
# dfa = state of DFA
def state2(c):
        if (c == 'b'):
                dfa = 0
        elif (c == 'a'):
                dfa = 1
        else:
                dfa = -1
        return dfa



def isAccepted(String):

        # store length of Stringing
        l = len(String)

        # dfa tells the number associated
        # with the present dfa = state
        dfa = 0
        for i in range(l):
                if (dfa == 0):
                        dfa = start(String[i])

                elif (dfa == 1):
                        dfa = state1(String[i])

                elif (dfa == 2) :
                        dfa = state2(String[i])


                else:
                        return 0
        if(dfa == 2) :
                return 1
        else:
                return 0

# Driver code
if __name__ == "__main__" :
        String = "aaba"
        if (isAccepted(String)) :
                print("ACCEPTED")
        else:
                print("NOT ACCEPTED")
        
