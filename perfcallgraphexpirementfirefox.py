class Node:
  
    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null
        self.headcounter = 1
        self.last_head_index = -1
        self.sub_sample_counter = []
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







samples = 100
sub_samples = 10
array=[]
last_parrent_index = 0
current_count = -1

while True:
    if samples % sub_samples > 0:
        samples = samples - 1
    else:
        break


for count in range(samples):
    print(str(int(100*count/(samples-1)))+"% done")
    
    with open('perf'+str(count)+'.txt') as f:
        while True:

            line = f.readline().strip()
            if not line:
                break
            
            #print("\nNew Loop: "+ str(count)+ "\n")
            if line != None and line != "":


                if line.count('%') > 1:
                    if "libxul.so" in line or "libc-2.31.so " in line:
                        parent = line.split("] ")[-1]

                        #child = line.split("[.] ",1)[1]

                        #check if parent already exist
                        found = False
                        counter = -1
                        for k in array:
                            counter = counter + 1
                            if k.getData() == parent:
                                if k.head.last_head_index != count:
                                    k.head.headcounter = k.head.headcounter + 1
                                    k.head.last_head_index = count
                                last_parrent_index = counter
                                found = True
                                break
                        if not found:
                            llist = LinkedList()
                            llist.head = Node(parent)
                            #llist.head.next = Node(child)
                            array.append(llist)
                            last_parrent_index = len(array) - 1

                        if count % sub_samples == 0 and array[last_parrent_index].head.last_count != count:
                            array[last_parrent_index].head.sub_sample_counter.append(array[last_parrent_index].head.headcounter)
                            array[last_parrent_index].head.headcounter = 0
                            array[last_parrent_index].head.last_count = count

                else:
                    if len(array) > 0:
                        children = line.split("% ",1)[1].split(";")
                        temp = array[last_parrent_index].getLast()
                        for k in children:
                            if array[last_parrent_index].searchValue(k):
                                continue
                            child = Node(k)
                            temp.next = child
                            temp = child

                   

        
           
f = open("output.txt", "w")



for k in array:
    print(str(k.head.sub_sample_counter))
    f.write(str(k.head.sub_sample_counter)+"\n")

    k.printList()

    temp = k.head
    while (temp):
        f.write(temp.data+"\n")
        temp = temp.next

    f.write("\n")
    print("\n")

f.close()

print("All complete!")
