def question1(compare_string, ana_string, string_builder=""):
    """
    Given a string s, this function returns true if an anagram of t is a substring of s.
    Returns false otherwise.
    """
    #If compare string is empty, always return false
    if compare_string == "":
        return False
    
    #If no more characters to mutate
    if ana_string == "":
        #Always return false if string_builder is empty string, since "" in some_string
        #is true for all strings
        if string_builder == "":
            return False
        
        #Default case
        return string_builder in compare_string
    
    #Append chars recursively
    for i in range(len(ana_string)):
        #Get current char
        ch = ana_string[i]
        
        #Attempt recursive permutations
        curr_bool = question1(
            compare_string,
            ana_string[:i] + ana_string[i+1:],
            string_builder + ch
        )
        
        #Anagram found criteria
        if curr_bool:
            return True
    
    #No anagram found
    return False

q1_tests = [
    ("a", "a"),#True
    ("b", "a"),#False
    ("abcdefg", "ba"),#True
    ("abcdefg", "bad"),#False
    ("cinema", "iceman"),#True
    ("iceman52", "cinema")#True
]

for i in range(len(q1_tests)):
    print("Test {}: {}".format(i, question1(q1_tests[i][0], q1_tests[i][1])))