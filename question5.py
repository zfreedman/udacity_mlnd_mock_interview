class Node:
    """
    Implementation of a singly linked list node.
    """
    def __init__(self, data):
        self.data = data
        self.next = None
        
#Note there's no need to implement a linked list class if I just need to iterate through
#a list of nodes. This problem is trivial
def make_fake_ll(data_list):
    """
    Given a list of the form [type1, type1, type1, ..., type1], this method returns a linked
    list of Node classes with the ith Node holding the ith type1 data and the ith Node's next
    points to a node holding the (i+1)th type1 data.
    """
    head = None
    #If list not empty, allocate head
    if 0 < len(data_list):
        head = Node(data_list[0])
    
    #Create nodes
    curr_node = head
    for i in range(1, len(data_list)):
        curr_node.next = Node(data_list[i])
        curr_node = curr_node.next
        
    #Return linked list
    return head

def question5(ll, m):
    """
    Given a linked list, referencable by a head node ll, this function returns the mth node
    from the end of the list. This method handles overflow for large m values s.t. they're
    bounded to the left by index 0. The element 17th-to-last in a 10 element list is therefore
    at index 0.
    """
    
    #Iterate once through to get length
    curr_node = ll
    length = 0
    while curr_node:
        length += 1
        curr_node = curr_node.next
    
    #Iterate until desired is found
    curr_node = ll
    diff = length - m
    while 0 < diff:
        diff -= 1
        curr_node = curr_node.next
    
    return curr_node

#Tuples of the form (test linked list, test m, solution)
tests_and_solutions = [
    (make_fake_ll([0,1,2,3,4]), 4, 1),
    (make_fake_ll([]), 17, None),
    (make_fake_ll([i for i in range(27)]), 28, 0),
    (make_fake_ll([i-2 for i in range(27)]), 15, 10)
]

for i in range(len(tests_and_solutions)):
    tup = tests_and_solutions[i]
    answer = question5(tup[0], tup[1])
    if answer != None:
        answer = answer.data
    print("Test {} passed: {}".format(i, answer == tup[2]))