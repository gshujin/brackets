class Node:
    def __init__(self, data, before=None, after=None):
        self.data = data
        self.before = before
        self.after = after

class Stack:
    def __init__(self):
        self.head = None
    def isEmpty(self):
        return self.head == None
    def pop(self):
        output = self.head.data
        self.head = self.head.before
        return output
    def push(self, data):
        self.head = Node(data, self.head)
    def top(self):
        return self.head.data
    
def match(string):
    """given a string, checks that the brackets are
    correctly nested"""
    left, right, pairs = "({[", ")}]", ["()", "{}", "[]"]
    s = Stack()
    for char in string:
        if char in left:
            s.push(char)
        if char in right:
            if s.isEmpty() == True:
                print (char + " has no match")
                return False
            char2 = s.pop()
            if char2 + char not in pairs:
                print (char2 + " and " + char + " do not match")
                return False
    if s.isEmpty() == False:
        print (s.pop() + " has no match")
        return False
    print ("everything matches")
    return True

def brackets(string):
    """determine if string can be made into a sequence of properly nested brackets"""
    list_string = list(string)

    def indexes(myList, desiredElement):
        return [index for index, element in enumerate(myList) if element == desiredElement]

    indexList = indexes(list_string, '*')
    print(indexList)

    list_permutations = []

    def AllKLength(set, k):
        n = len(set)
        AllKLengthRec(set, "", n, k)

    def AllKLengthRec(set, prefix, n, k):
        if (k == 0) :
            list_permutations.append(prefix)
            return
        for i in range(n):
            newPrefix = prefix + set[i]
            AllKLengthRec(set, newPrefix, n, k - 1)

    set = ['(',')','[',']','{','}']
    k = len(indexList)

    AllKLength(set,k)
    print(list_permutations)

    for charac in list_permutations:
        for i in range(len(charac)):
            x = indexList[i]
            string = string[:x] + charac[i] + string[x+1:]
            print(string)
        if match(string):
            break

        if list_permutations.index(charac) + 1 == len(list_permutations):
            return False
        
    return True

if brackets('*()][{*]'):
    print("t")
else: 
    print('f')
        