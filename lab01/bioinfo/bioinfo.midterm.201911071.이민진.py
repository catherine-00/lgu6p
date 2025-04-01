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
1. dna2rna
Problem: Given a DNA string, return its transcribed RNA string.
Sample Input : GATGGAACTTGACTACGTAAATT
Sample Output: GAUGGAACUUGACUACGUAAAUU  # T -> U
 print("1. dna2rna")
    test(dna2rna("GATGGAACTTGACTACGTAAATT"), "GAUGGAACUUGACUACGUAAAUU")
    test(dna2rna("cgTAaCAAggTttCC"), "CGUAACAAGGUUUCC")
"""
def dna2rna (dna):
    # +++your code here+++
    dna=dna.upper()
    RNA=dna.replace("T","U")
    return RNA
    pass

"""
2. sum_multiples
Problem: Given numbers of a & b, return the summation of all multiples of 3 from a to b.
Sample Input : (4,10)
Sample Output: 15  # 6 + 9 = 18 
print("2. sum_multiples")
    test(sum_multiples(4,10), 15)
    test(sum_multiples(10,100), 1665)
    test(sum_multiples(1, 1000), 166833)
"""
def sum_multiples (a, b):
    # +++your code here+++
    sum=0
    for i in range(a,b+1):
        if i %3 ==0:
            sum += i
    return sum
    pass
	
"""
3. find_common_characters
Problem: Given a list of strings, return the list of characters present in all the strings in alphabetical order.
Sample Input : ["dac", "dea", "abd"]
Sample Output: ["a", "d"] 
 print("3. find_common_characters")
    test(find_common_characters(["dac", "dea", "abd"]), ["a", "d"])
    test(find_common_characters(["bella", "barrow", "baba"]), ["a", "b"])
    test(find_common_characters(["transciptome", "proteome", "metabolome"]), ["e", "m", "o", "t"])     
"""
def find_common_characters(lst):
    # +++your code here+++
    set1=set(lst[0])
    set2=set(lst[1])
    set3=set(lst[2])
    coset=set1&set2&set3
    coset=sorted(coset)
    return coset
    pass

"""
4. calc_restrict_fragment_size_v2
Problem: Given a dna and a restriction enzyme recognition site, 
         return a list of all the sizes of the fragments that will be produced 
         when the dna is digested with the restriction enzyme.
         (the position of the cut is indicated by an asterisk)         
Sample Input1 : "aggatcctgaggatccggaattc", "g*gatcc" 
Sample Output1: [2, 9, 12]  # Fragments are "ag", "gatcctgag", "gatccggaattc")

Sample Input1 : "aggatcctgaggatccggaattc", "gga*tcc" 
Sample Output1: [4, 9, 10]  # Fragments are "agga", "tcctgagga", "tccggaattc") 
print("4. calc_restrict_fragment_size_v2")
    test(calc_restrict_fragment_size_v2("aggatcctgaggatccggaattc", "g*gatcc"), [2, 9, 12])
    test(calc_restrict_fragment_size_v2("aggatcctgaggatccggaattc", "gga*tcc"), [4, 9, 10])
    test(calc_restrict_fragment_size_v2("aaaagcttgatcctttaagcttgatccaagcttc", "a*agctt"), [3, 14, 11, 6])
    test(calc_restrict_fragment_size_v2("aaaagcttgatcctttaagcttgatccaagcttc", "aagct*t"), [7, 14, 11, 2])
    test(calc_restrict_fragment_size_v2("actgatcgattacgtatagtagaattctatcatacatatatatcgatgcgttcat", "g*aattc"), [22, 33])
    test(calc_restrict_fragment_size_v2("actgatcgattacgtatagtagaattctatcatacatatatatcgatgcgttcat", "gaat*tc"), [25, 30])
 
"""
def calc_restrict_fragment_size_v2(dna, enz):
    # +++your code here+++
    delet=enz.replace("*","")
    all=dna.replace(delet,enz)
    frag=all.split("*")
    size=[]
    i=0
    for i in range(len(frag)):
        size.append(len(frag[i]))
    return size



    pass
"""
5. count_g_in_exons_from_file
Problem : Given a dna sequence file and a list of start/stop positions of exons, return the number of 'G's in the exons. 
Sample Input1 : "genomic_dna.ch4.txt", [[5,15]]
Sample Output1: 3    # the exon is "CGTACCGTCG", and there is 3 "G"s in it.

Sample Input2 : "genomic_dna.ch4.txt", [(][5,15], [30,40]]
Sample Output2: 6    # the exon is "CGTACCGTCGTCGATCGTAG", and there is 3 "G"s in it.
print("5. count_g_in_exons_from_file")
    test(count_g_in_exons_from_file("genomic_dna.ch4.txt", [[5,15]]), 3)
    test(count_g_in_exons_from_file("genomic_dna.ch4.txt", [[5, 15], [30,40]]), 6)
    test(count_g_in_exons_from_file("genomic_dna.ch4.txt", [[41, 58], [72, 133], [340, 390]]), 30)
    test(count_g_in_exons_from_file("genomic_dna.ch3.txt", [[50, 80]]), 7)
    test(count_g_in_exons_from_file("genomic_dna.ch3.txt", [[32, 60], [70, 99]]), 11)
    test(count_g_in_exons_from_file("genomic_dna.ch3.txt", [[11, 34], [64, 79], [100, 111]]), 12)
"""
def count_g_in_exons_from_file(file, exon_locations):
    # +++your code here+++
    dna_file=open("C:/Users/user/Downloads/%s"%file,"r")
    dna=dna_file.read()
    i=0
    content=""
    for i in range(len(exon_locations)):
        start=exon_locations[i][0]
        stop=exon_locations[i][1]
        content += dna[int(start):int(stop)]
    G_count=content.count("G")
    return G_count
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

    print("1. dna2rna")
    test(dna2rna("GATGGAACTTGACTACGTAAATT"), "GAUGGAACUUGACUACGUAAAUU")
    test(dna2rna("cgTAaCAAggTttCC"), "CGUAACAAGGUUUCC")

    print("2. sum_multiples")
    test(sum_multiples(4,10), 15)
    test(sum_multiples(10,100), 1665)
    test(sum_multiples(1, 1000), 166833)

    print("3. find_common_characters")
    test(find_common_characters(["dac", "dea", "abd"]), ["a", "d"])
    test(find_common_characters(["bella", "barrow", "baba"]), ["a", "b"])
    test(find_common_characters(["transciptome", "proteome", "metabolome"]), ["e", "m", "o", "t"])

    print("4. calc_restrict_fragment_size_v2")
    test(calc_restrict_fragment_size_v2("aggatcctgaggatccggaattc", "g*gatcc"), [2, 9, 12])
    test(calc_restrict_fragment_size_v2("aggatcctgaggatccggaattc", "gga*tcc"), [4, 9, 10])
    test(calc_restrict_fragment_size_v2("aaaagcttgatcctttaagcttgatccaagcttc", "a*agctt"), [3, 14, 11, 6])
    test(calc_restrict_fragment_size_v2("aaaagcttgatcctttaagcttgatccaagcttc", "aagct*t"), [7, 14, 11, 2])
    test(calc_restrict_fragment_size_v2("actgatcgattacgtatagtagaattctatcatacatatatatcgatgcgttcat", "g*aattc"), [22, 33])
    test(calc_restrict_fragment_size_v2("actgatcgattacgtatagtagaattctatcatacatatatatcgatgcgttcat", "gaat*tc"), [25, 30])

    print("5. count_g_in_exons_from_file")
    test(count_g_in_exons_from_file("genomic_dna.ch4.txt", [[5,15]]), 3)
    test(count_g_in_exons_from_file("genomic_dna.ch4.txt", [[5, 15], [30,40]]), 6)
    test(count_g_in_exons_from_file("genomic_dna.ch4.txt", [[41, 58], [72, 133], [340, 390]]), 30)
    test(count_g_in_exons_from_file("genomic_dna.ch3.txt", [[50, 80]]), 7)
    test(count_g_in_exons_from_file("genomic_dna.ch3.txt", [[32, 60], [70, 99]]), 11)
    test(count_g_in_exons_from_file("genomic_dna.ch3.txt", [[11, 34], [64, 79], [100, 111]]), 12)


    print()
    print(" [%s test_passed / %s test_total]" % (repr(no_passed), repr(no_test)))

if __name__ == '__main__':
    main()
