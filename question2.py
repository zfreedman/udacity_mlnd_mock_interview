def question2(s):
    #Test base case
    if s == s[::-1]:
        return s
    
    best_pali = ""
    #Iterate over string
    for i in range(len(s)):
        #Attempt palindrome centering at current index
        curr_pali = s[i]
        left = i - 1
        right = i + 1
        
        #Iteratively build palindrome until broken
        while True:
            
            #Test both
            if -1 < left and right < len(s):
                both_pali = s[left] + curr_pali + s[right]
                if both_pali == both_pali[::-1]:
                    curr_pali = both_pali
                    left -= 1
                    right += 1
                    continue
                
            #Test left
            if -1 < left:
                left_pali = s[left] + curr_pali
                if left_pali == left_pali[::-1]:
                    curr_pali = left_pali
                    left -= 1
                    continue
                
            #Test right
            if right < len(s):
                right_pali = curr_pali + s[right]
                if right_pali == right_pali[::-1]:
                    curr_pali = right_pali
                    right += 1
                    continue
                
            #No better palindrome found
            break
                
        #Update if best pali has been beaten
        if len(best_pali) < len(curr_pali):
            best_pali = curr_pali
    return best_pali

q2_tests = [
    ("", ""),
    ("a", "a"),
    ("ab", "a"),
    ("aba", "aba"),
    ("abcb", "bcb"),
    ("eat tae", "eat tae"),
    ("2442", "2442"),
    ("2244664432", "446644")
]

for i in range(len(q2_tests)):
    answer = question2(q2_tests[i][0])
    print("Test {}: question2({}) = {} ... expected {}".format(
        i, q2_tests[i][0], answer, q2_tests[i][1]
    ))