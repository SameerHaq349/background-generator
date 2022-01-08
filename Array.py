#GithubSecond
numbers = [8,2,4,6,2,7,9,1]

def selectionSort(array):
    index_array = range(0,len(array)-1)

    for i in index_array:
        min = array[i]
        for j in range(i+1, len(array)):
            if array[j] < min:
                min = array[j]
                array[j], array[i] = array[i], array[j]
    print(array)


selectionSort(numbers)

#Merge Sort (Two things to note 1. understand the recursion aspect 2. understand why it is o(nlog(n))

def mergeSort(array):
    if len(array) > 1:
        
        left_array = array[:len(array)//2]
        right_array = array[len(array)//2:]

        mergeSort(left_array)
        mergeSort(right_array)

        i = 0
        j = 0
        k = 0

        while i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]:
                array[k] = left_array[i]
                i += 1
                k += 1
            
            else:
                array[k] = right_array[j]
                j += 1
                k += 1
        
        while i < len(left_array):
            array[k] = left_array[i]
            i += 1
            k += 1
        
        while j < len(right_array):
            array[k] = right_array[j]
            j += 1
            k += 1
    
    return array


print(mergeSort(numbers))

#Binary Search

def search(array, target):

    left_arr = array[:len(array)//2]
    right_arr = array[len(array)//2:]

    i = 0

    while array[i] != target:

        if target < array[len(array)//2]:
            right_arr = left_arr[len(left_arr)//2:]
            left_arr = left_arr[:len(left_arr)//2]
            i = array[len(left_arr)]
        
        elif target > array[len(array)//2]:
            left_arr = right_arr[:len(right_arr)//2]
            right_arr = right_arr[len(right_arr)//2:]
            i = array[len(right_arr)]

    return i





#Tren Black Binary Search. Be able to explain the time and space complexity and implement this yourself

def binary_search(arr, target):
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = (start+end)//2
        if target == arr[mid]:
            return mid
        elif target < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1

print(binary_search(numbers, 8))

# array https://www.guru99.com/array-data-structure.html#6



#linked list (flexible list size:you can insert, delete, and redirect nodes in constant time). Downside, you cant access elements in constant time via index. You have to traverse it
#appending to a list is a constant time operation. If node points to null, that's the end of the list.
#Other operations include get_size() and find(date)

class Node(object):
    def __init__(self, d, n = None):
        self.data = d
        self.next_node = n
        
    def get_next():
        return self.next_node

    def set_next():
        self.next_node = n

    def get_data():
        return self.data

    def set_data():
        self.data = d

class LinkedList(object):
    def __init__(self, r = None):
        self.root = r
        self.size = 0

    def get_size():
        return self.size

    def add(self, d):
        new_node = Node(d, self.root)
        self.root = new_node
        self.size += 1

    def remove(self, d):
        this_node = self.root
        prev_node = None
        while this_node:
            if this_node.get_data() ==d:
                if prev_node:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.root = this_node
                self.size -= 1
                return True
            else:
                prev_node = this_node
                this_node = this_node.get_next()
        return False

    def find(self, d):
        this_node = self.root
        while this_node:
            if this_node.get_data() == d:
                return d
            else:
                this_node = this_node.get_next()
        return None
    

#Induction and Recurison: http://www.cs.cornell.edu/courses/cs211/2004su/slides/Topic02.pdf

#print "hello world"

print("hello world")


print("this is not another message!")

