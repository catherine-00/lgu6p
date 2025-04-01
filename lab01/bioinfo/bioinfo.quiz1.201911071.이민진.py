#!/usr/bin/python -tt
"""
Written by Sung Ho Yoon @konkuk university
This script is for python class at Dept. Systems Biotechnology, Konkuk University
http://www.apache.org/licenses/LICENSE-2.0

Instruction:
Fill in the code for the functions below.
main() is already set up to call the functions with a few different inputs,
printing 'Passed!' when each function is correct.
printing 'Humm...' when each function is incorrect.
"""

"""
[Warning!!!]
While coding, never write a constant value (number or string) as a return value, in order to pass the related test function.
If you do that, you will get zero score for the whole test.
단지 test function을 통과하기 위해, 절대로 각 function의 상수값을 return 하지 말것.
하나라도 발각시 시험 자체를 무효로 하고 0점 처리함.
"""

"""
1. get_unique_string (string)
Problem: Given a string, return a list with unique values in their given order
Sample Input : 'baacbd'
Sample Output: 'bacd' 
"""
def get_unique_string (string):
    # +++your code here+++
    l = []
    if i not in string:
        l.append(i)
    s = "".join(l)



    """중복 지우는 """

    pass

"""
2. contains(big_string, small_string)
Problem: Return True if big_string contains small_string (case insensitive). The function should return False otherwise. 
Sample Input : "watermelon", "Melon"
Sample Output: True
"""
def contains(big_string, small_string):
    # +++your code here+++
    a=[]
    a.append(big_string)
    b=[]
    b.append(small_string)
    if small_string in a:
        return True



    pass

"""
3. modify_string (string)
Problem: Given a string, return a modified string. 
(shift all of the letters by one to the right, & the last letter of input string becomes to be the first letter.)
Sample Input : 'luffy'
Sample Output: 'yluff'
"""
def modify_string (string):
    # +++your code here+++
    a= "%s" (string)
    b="%s"+a (string[-1])
    b.remove[-1]

    return b
    pass

"""
4. get_common_chars (string1, string2)
Problem: Given string1 and string2, return a list with all of the characters (in ascending order) that the two lists have in common.
Sample Input : "apple", "pie"
Sample Output: ['e', 'p']
"""
def get_common_chars (string1, string2):
    # +++your code here+++
    a={apple}
    b={pie}
    """중복 찾기"""
    pass

#########################################################################################
# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
# def test(got, expected):
#     if got == expected:
#         prefix = '    Passed! '
#     else:
#         prefix = '    Humm... '
#     print('%s yours: %s vs. expected: %s' % (prefix, repr(got), repr(expected)))
#########################################################################################

no_test   = 0
no_passed = 0

def test(got, expected):
    global no_test, no_passed
    no_test += 1

    if got == expected:
        prefix = '   Passed! '
        no_passed += 1
    else:
        prefix = '   Humm... '
    print("%s yours: %s vs. expected: %s" % (prefix, repr(got), repr(expected)))

##############################################################
# Calls the above functions with interesting inputs.
##############################################################
def main():
    print("1. get_unique_string")
    test(get_unique_string('baacbd'), 'bacd')
    test(get_unique_string('veglolajlej'), 'vegloaj')
    test(get_unique_string('acttag'), 'actg')
    test(get_unique_string('university'), 'universty')

    print("2. contains")
    test(contains("watermelon", "Melon"), True)
    test(contains("summer vacation", "sum"), True)
    test(contains("TTCAGGA", "cga"), False)
    test(contains("summer vacation", "winter"), False)

    print("3. modify_string")
    test(modify_string('luffy'), 'yluff')
    test(modify_string('zoro'), 'ozor')
    test(modify_string('sangdi'), 'isangd')
    test(modify_string('Usopp'), 'pUsop')
    test(modify_string('choppa'), 'achopp')
    test(modify_string('nami'), 'inam')

    print("4. get_common_chars")
    test(get_common_chars("apple", "pie"), ['e', 'p'])
    test(get_common_chars("zoro", "Usopp"), ['o'])
    test(get_common_chars("TATC", "CTACG"), ['A', 'C', 'T'])
    test(get_common_chars("djaskljfn1jflkjaerew3adfa", "bmerktmqn"), ['e', 'k', 'n', 'r'])
    test(get_common_chars("gnronobg", "jfdoafihejorwqnewngf"), ['g', 'n', 'o', 'r'])
    test(get_common_chars("bmraekhmnronge", "etjraenjmrf"), ['a', 'e', 'm', 'n', 'r'])

    print()
    print(" [%s test_passed / %s test_total]" % (repr(no_passed), repr(no_test)))

if __name__ == '__main__':
    main()
