class Node():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.bottom = None

class Graph():
    def __init__(self):
        self.head = None

    def add_vertex(self,data):
        newnode = Node(data)
        if(self.head == None):
            self.head = newnode
        else:
            current = self.head
            while(current.bottom!=None):
                current = current.bottom
            current.bottom = newnode
            
    def connect_vertex(self,vertex1, vertex2):
        checking = self.head
        cheking_count = 0
        while(checking != None):
            if(checking.data ==vertex1 or checking.data == vertex2):
               cheking_count +=1 
            checking = checking.bottom
        if(cheking_count !=2):
            print("sorry you are tring to connect to already unexsist pair of from {} to {}".format(vertex1, vertex2))
        else:
            adding_helper_bottom= self.head
            while(adding_helper_bottom.data != vertex1):
                adding_helper_bottom = adding_helper_bottom.bottom 
            adding_helper_cross =  adding_helper_bottom
            while(adding_helper_cross.left != None):
                adding_helper_cross = adding_helper_cross.left
            adding_helper_cross.left = Node(vertex2)
            


    def show(self):
        printing_helper_bottom = self.head
        while(printing_helper_bottom != None):
            printing_helper_cross = printing_helper_bottom
            while(printing_helper_cross!=None):
                print(printing_helper_cross.data,end = " ")
                if(printing_helper_cross.left != None):
                   print("-->",end = " ") 
                printing_helper_cross = printing_helper_cross.left
            print(" ")
            printing_helper_bottom = printing_helper_bottom.bottom

    def delete(self,number):
        delete_down = self.head
        while True:
            #to delete the connected nodes
            
            DLETELEFT = delete_down
            
            #for traverse the left and find the what nodes are connected
            while True:
                #last node
                if(DLETELEFT.left== None):
                    break
                if(DLETELEFT.left.data == number and DLETELEFT.left.left != None):
                    DLETELEFT.left = DLETELEFT.left.left
                    break
                if(DLETELEFT.left.data == number and DLETELEFT.left.left == None):
                    DLETELEFT.left = None
                    break
                
                DLETELEFT = DLETELEFT.left
                
                if(DLETELEFT.left== None):
                    
                    break
                
              
            #delete the first node
            
            if(self.head.data == number):
                self.head = self.head.bottom
            #to delete the middle node
            if(delete_down.bottom ==None):
                break
            
            

            if(delete_down.bottom.data == number and delete_down.bottom.bottom!=None):
                delete_down.bottom = delete_down.bottom.bottom
                
            #to delete the last node
            if(delete_down.bottom.data == number and delete_down.bottom.bottom==None):
                delete_down.bottom = None
                break
            

            delete_down = delete_down.bottom 

            
            
                
        
            
        
graph = Graph()        

graph.add_vertex(10)
graph.add_vertex(20)
graph.add_vertex(30)
graph.add_vertex(40)
graph.add_vertex(50)
graph.add_vertex(60)
graph.add_vertex(70)
graph.add_vertex(80)
graph.connect_vertex(10,70)
graph.connect_vertex(30,10)
graph.connect_vertex(10,30)
graph.connect_vertex(50,20)
graph.connect_vertex(30,20)
graph.connect_vertex(10,40)
graph.connect_vertex(60,20)
graph.connect_vertex(70,40)
graph.connect_vertex(70,20)
graph.connect_vertex(70,50)
graph.connect_vertex(30,10)
graph.connect_vertex(30,40)
#graph.delete(20)
graph.show()

























            
            
        
        
        
