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

    def getData(self):
        temp = self.head
        return temp.data

    def searchValue(self, val):
        temp = self.head
        while (temp):
            if temp.data == val:
                return True
            temp = temp.next
        return False







samples = 5
array=[]
last_parrent_index = 0

for count in range(samples):
    with open('perf'+str(count)+'.txt') as f:
        while True:

            line = f.readline().strip()
            if not line:
                break
            

            if line != None:
                if "[.]" in line:
                    parent = line.split("%  ")[2].split(" ",1)[0]
                    child = line.split("[.] ",1)[1]

                    #check if parent already exist
                    found = False
                    counter = -1
                    for k in array:
                        counter = counter + 1
                        if k.getData() == parent:
                            k.head.headcounter = k.head.headcounter + 1
                            last_parrent_index = counter
                            found = True
                            break
                    if not found:
                        llist = LinkedList()
                        llist.head = Node(parent)
                        llist.head.next = Node(child)
                        array.append(llist)
                        last_parrent_index = len(array) - 1

                elif "[k]" in line:
                    parent = line.split("%  ")[2].split(" ",1)[0]
                    child = line.split("[k] ",1)[1]

                    #check if parent already exist
                    found = False
                    counter = -1
                    for k in array:
                        counter = counter + 1
                        if k.getData() == parent:
                            k.head.headcounter = k.head.headcounter + 1
                            last_parrent_index = counter
                            found = True
                            break

                    if not found:
                        llist = LinkedList()
                        llist.head = Node(parent)
                        llist.head.next = Node(child)
                        array.append(llist)
                        last_parrent_index = len(array) - 1

                else:
                    children = line.split("% ",1)[1].split(";") 
                    temp = array[last_parrent_index].getLast()

                    for k in children:
                        if array[last_parrent_index].searchValue(k):
                            continue
                        child = Node(k)
                        temp.next = child
                        temp = child

        
           
            
for k in array:
    print(str(k.head.headcounter))
    k.printList()
    print("\n")
