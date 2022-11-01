class Node:
  
    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null
        self.time_counter = []
        self.last_count = -1
  
  
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







samples = 1
array=[]
last_parrent_index = 0
current_count = -1


connections = {}

for count in range(samples):
    
    with open('perf'+str(count)+'.txt') as f:
        while True:

            line = f.readline().strip()
            if not line:
                break
            
            #print("\nNew Loop: "+ str(count)+ "\n")
            if line != None and line != "":


                if line.count('%') > 1:
                    #if "libxul.so" in line or "libc-2.31.so " in line:
                    parent = line.split("] ")[-1]

                    #check if parent already exist
                    found = False
                    counter = -1
                    for k in array:
                        counter = counter + 1
                        if k.getData() == parent:
                            found = True
                            
                            if k.head.last_count <= count-2:
                                k.head.time_counter.append(1)
                            else:
                                if k.head.last_count != count:
                                    k.head.time_counter[-1] = k.head.time_counter[-1] + 1

                            k.head.last_count = count
                            last_parrent_index = counter
                            break
                    if not found:
                        llist = LinkedList()
                        llist.head = Node(parent)
                        llist.head.last_count = count
                        llist.head.time_counter.append(1)
                       
                        array.append(llist)
                        last_parrent_index = len(array) - 1



                else:
                    if len(array) > 0:
                        children = line.split("% ",1)[1].split(";")
                        parent = array[last_parrent_index].getData()

                        for i in children:
                            connection = parent + "---" + i
                            if connection in connections:
                                connections[connection] += 1
                            else:
                                connections[connection] = 1

                            parent = i


                            found = False
                            counter = -1
                            for k in array:
                                counter = counter + 1
                                if k.getData() == i:
                                    found = True
                                    
                                    if k.head.last_count <= count-2:
                                        k.head.time_counter.append(1)
                                    else:
                                        if k.head.last_count != count:
                                            k.head.time_counter[-1] = k.head.time_counter[-1] + 1

                                    k.head.last_count = count
                                    last_parrent_index = counter
                                    break
                            if not found:
                                llist = LinkedList()
                                llist.head = Node(i)
                                llist.head.last_count = count
                                llist.head.time_counter.append(1)
                               
                                array.append(llist)
                                last_parrent_index = len(array) - 1



                   

        
           
f = open("output1.txt", "w")



for k in array:
    print(str(k.head.time_counter))
    f.write(str(k.head.time_counter)+"\n")

    k.printList()

    temp = k.head
    while (temp):
        f.write(temp.data+"\n")
        temp = temp.next

    f.write("\n")
    print("\n")

f.close()

connections = sorted(connections.items(), key=lambda x: x[1], reverse=True)

f = open("output2.txt", "w")
for item in connections:
    f.write(item+"\n")
    print(item) # gives a tuple

f.close()
