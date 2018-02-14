def question4(ll, root, n1, n2):
    """
    Returns the least common ancestor for the specified tree in ll rooted by the root indexed
    node in ll for child nodes n1 and n2.
    """
    n3 = root
    #Iterate until parent is found
    while True:
        
        left = -1
        right = -1
        #Get left and right child of n3
        for i in range(len(ll[n3])):
            if ll[n3][i] == 1:
                if ll[n3][i] < n3:
                    left = i
                elif n3 < ll[n3][i]:
                    right = i
                    break
        
        #Compare and set next node to left or right
        if n1 < n3 and n2 < n3:
            n3 = left
        elif n1 > n3 and n2 > n3:
            n3 = right
        #LCA found
        else:
            return n3
    #Bad
    return -1

tests = [
    (
        [
            [0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [1, 0, 0, 0, 1],
            [0, 0, 0, 0, 0]
        ],
        3,
        1,
        4
    ),
    (
        [
            [0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0],
            [0, 1, 0, 1, 0],
            [0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0]
        ],
        2,
        1,
        4
    ),
    (
        [
            [0, 1, 0],
            [0, 0, 1],
            [0, 0, 0]
        ],
        0,
        1,
        2
    )
]

solutions = [3, 2, 1]
for i in range(len(tests)):
    print("Test {} passed: {}".format(
        i,
        question4(tests[i][0], tests[i][1], tests[i][2], tests[i][3]) == solutions[i]
    ))