'''           WELCOME TO THE RUWANLIYANAGE GRAPHS SYSTEM
                   ruwanliyanagegalle1994@gmail.com
                           0772308519/0774201133           
                     * command 1 for:addnode:
                     * command 2 for:count:
                     * command 3 for:connectnode:
                     * command 4 for:printnodes:                                    '''



class Node():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.bottom =None

class graph():
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def addnode(self, value):
        newnode = Node(value)
        if(self.head == None):
            self.head = newnode
        else:
            cmd = self.head
            while(cmd.bottom != None):
                cmd = cmd.bottom
            cmd.bottom = newnode

    def count(self):
        if(self.head == None):
            return 0
        else:
            count = 0
            tmp = self.head
            while(tmp!= None):
                count +=1
                tmp = tmp.bottom
            print("THE NUMBER OF VERTECES ARE:- {}".format(count))

    def connect(self, valueA, valueB):
        benz = self.head
        
        while(benz.data !=valueA):
            
            benz = benz.bottom
        #print(benz.data)
        bmw  = benz
        while(bmw.left!= None):
            bmw = bmw.left
        bmw.left = Node(valueB)
        #print(bmw.data)

    def delet(self,value):
        if(self.head.data == value):
            self.head.bottom = self.head
        else:
            honda = self.head
            while(honda !=None):
                if(honda.bottom.data == value):
                    honda.bottom = honda.bottom.bottom
                








    def showing(self):
        audi   = self.head
        while(audi !=None):
            if(audi.left== None):
                print(audi.data)
                if(audi.bottom !=None):
                    print("|")
            else:
                jaguar = audi
                print(audi.data,end ="")
                while(jaguar.left!= None):
                    if(jaguar.left.left!= None):
                        print("-->{}".format(jaguar.left.data),end = "")
                    else:
                        print("-->{}".format(jaguar.left.data))
                        print("|")
                    jaguar = jaguar.left
            audi = audi.bottom
                
                



g = graph()
'''g.addnode(10)
g.addnode(20)
g.addnode(30)
g.addnode(40)
g.addnode(50)
g.addnode(60)
g.connect(10,20)
g.connect(10,30)
g.connect(10,40)
g.connect(20,50)
g.connect(30,20)
g.delet(30)
g.showing()'''


print("            WELCOME TO THE RUWANLIYANAGE GRAPHS SYSTEM")
print( "                ruwanliyanagegalle1994@gmail.com" )
print("                           0772308519           ")
print("                  * command 1 for:addnode:")
print("                  * command 2 for:count:")
print("                  * command 3 for:connectnode:")
print("                  * command 4 for:printnodes:")
while(1>0):
    command = int(input("             ENTER YOUR COMMAND:-"))
    if(command == 1):
        vertex = int(input("enter your vertex number"))
        g.addnode(vertex)
        vote = input("if you want to exit this programme please enter y ")
        if(vote == "y"):
            break
    if(command == 2):
        g.count()
        vote = input("if you want to exit this programme please enter y ")
        if(vote == "y"):
            break
    if(command == 3):
        print("what do you want to connect as A and B")
        vertex1 = int(input("enter A"))
        vertex2 = int(input("enter B"))
        g.connect(vertex1,vertex2)
        vote = input("if you want to exit this programme please enter y ")
        if(vote == "y"):
            break
    if(command == 4):
        g.showing()
        vote = input("if you want to exit this programme please enter y ")
        if(vote == "y"):
            break
        


