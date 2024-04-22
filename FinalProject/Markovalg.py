# Written by Hayden

import random as rm


#states and values
states = ["State1","State2","State3"]
statenum=[1,0,0]
pristnm = [0,0,0]
i=0

#transitions
#matrix
trix =[[.5,.2,.3],[.1,.7,.2],[.6,.3,.1]]


#Matrix check each matrix should add up to one else it aborts
def macheck():
    
    if sum(trix[0])+sum(trix[1])+sum(trix[2]) != 3:
       print("ABORT! not adding to 1")
       exit(0) 

#checks each new version of statenum and compares it with the prior version
#if 3 repeates are found (4 in a row) it will be considered the steady state vector
def encheck(i,k):
    
    same=0
    if("%.4f" %pristnm[0] == "%.4f" %statenum[0]):
        same= same+1
        if("%.4f" %pristnm[1] == "%.4f" %statenum[1]):
            same=same+1
            if("%.4f" %pristnm[2] == "%.4f" %statenum[2]):
               
                if(k==3):
                    print("Steady State Vector:")
                    if(i-3 < 10):
                        cyclnum = str(i+-3) +"     |"
                    elif(i-3< 100):
                        cyclnum = str(i-3) +"    |"
                    elif(i+1 == 1000):
                        cyclnum = str(i-3) +"  |"
                    else:
                        cyclnum = str(i-3) +"   |"
                
                    print(cyclnum+"%.4f" %statenum[0] +"  |  "+"%.4f" %statenum[1]+"  |  "+"%.4f" %statenum[2])
                    exit(0)
                else:
                    return k+1
    if (same<3):
        pristnm[0]= statenum[0]
        pristnm[1]= statenum[1]
        pristnm[2]= statenum[2]
        if(i+1 < 10):
            cyclenum = str(i+1) +"     |"
        elif(i+1< 100):
            cyclenum = str(i+1) +"    |"
        elif(i+1 == 1000):
            cyclenum = str(i+1) +"  |"
        else:
            cyclenum = str(i+1) +"   |"
        print(cyclenum+"%.4f" %statenum[0] +"  |  "+"%.4f" %statenum[1]+"  |  "+"%.4f" %statenum[2])
        return 0

#the big boy, our markov chain calculations 
#multiplies each column by the 1st, 2nd,and 3rd statenum depending on height and adds it together
#then takes result and places it into statenum 0,1,2 depending on column
def chains():
    k=0

    for i in range (1000):
        
        ansa= statenum[0] *trix[0][0]
        ansb= statenum[1]* trix[1][0]
        ansc= statenum[2]* trix[2][0]
        resa= ansa+ ansb +ansc
        

        ansa= statenum[0] *trix[0][1]
        ansb= statenum[1]* trix[1][1]
        ansc= statenum[2]* trix[2][1]
        resb= ansa+ ansb +ansc

        ansa= statenum[0] *trix[0][2]
        ansb= statenum[1]* trix[1][2]
        ansc= statenum[2]* trix[2][2]
        resc= ansa+ ansb +ansc
        statenum[0]=resa
        statenum[1]=resb
        statenum[2]=resc
        macheck()
        k = encheck(i,k)

    
        
        

    

#driver
def main():
    macheck()
    print("Starting algorithm")
    print("cycle |"+states[0] +"  |  "+states[1]+"  |  "+states[2])
    print("0     |"+"%.4f" %statenum[0] +"  |  "+"%.4f" %statenum[1]+"  |  "+"%.4f" %statenum[2])
    chains()


if __name__== "__main__":
    main()