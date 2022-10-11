class Node:
  
    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null
        self.headcounter = 0
  
  
# Linked List class contains a Node object
class LinkedList:
  
    # Function to initialize head
    def __init__(self):
        self.head = None
  
    # This function prints contents of linked list
    # starting from head
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next

    def getLast(self):
        temp = self.head
        lasttemp = None
        while (temp):
            lasttemp = temp
            temp = temp.next

        return lasttemp






# Code execution starts here
if __name__ == '__main__':

    # array=[]
  
    # # Start with the empty list
    # llist = LinkedList()
  
    # llist.head = Node(1)
    # second = Node(2)
    # third = Node(3)
  
    # llist.head.next = second  # Link first node with second
    # second.next = third  # Link second node with the third node
  
    # llist.printList()


    #########################################

    array=[]

    with open('perf0.txt') as f:
        while True:
            line = f.readline().strip()
            if not line:
                break

            #print(line)

            

            if line != None:
                if "[.]" in line:
                    parent = line.split("%  ")[2].split(" ",1)[0]
                    child = line.split("[.] ",1)[1]

                    #check if parent already exist
                    for k in array:
                        if k.data = parent:
                            k.headcounter = k.headcounter + 1
                            break

                    llist = LinkedList()
                    llist.head = Node(parent)
                    llist.head.next = Node(child)
                    array.append(llist)

                elif "[k]" in line:
                    parent = line.split("%  ")[2].split(" ",1)[0]
                    child = line.split("[k] ",1)[1]

                     #check if parent already exist
                    for k in array:
                        if k.data = parent:
                            k.headcounter = k.headcounter + 1
                            break

                    llist = LinkedList()
                    llist.head = Node(parent)
                    llist.head.next = Node(child)
                    array.append(llist)
                else:
                    children = line.split("% ",1)[1].split(";") 
                    temp = array[-1].getLast()
                    for k in children:
                        child = Node(k)
                        temp.next = child
                        temp = child
               
                
    for k in array:



                #head
                #next line
                #split ";"
                #add them all into nodes and list
