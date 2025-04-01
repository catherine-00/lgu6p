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
1. find_duplicate
Problem: Given a list of numbers, return a list having only duplicate elements from the given list in ascending order. 
Sample Input : [2, 3, 1, 1, 2, 4, 5, 1]
Sample Output: [1, 2]
"""
def find_duplicate(lst):
    # +++your code here+++
    lst1 = []
    lst_com=[]
    for i in range(len(lst)):
        lst1.append(lst[i])
        if lst[i] in lst1:
            lst_com.append(lst[i])









    pass

''' 
2. calc_at_content
Problem : Given a dna sequence, return AT content of the dna sequence
Sample Input : 'atTggGcCcc'
Sample Output: 0.3
'''
def calc_at_content(dna):
    # +++your code here+++
    dna = dna.upper()
    AT_count=dna.count("A") + dna.count("T")
    AT_content = AT_count/len(dna)
    return AT_content
    pass

"""
3. calc_restrict_fragment_size_v3
Problem: Given a dna sequence file and a restriction enzyme recognition site, 
         return the multiplication of sizes of the fragments that will be produced 
         when the dna is digested with the restriction enzyme.
         (the position of the cut is indicated by an asterisk)         
Sample Input1 : "aggatcctgaggatccggaattc", "g*gatcc" 
Sample Output1: 216      # Fragments are "ag", "gatcctgag", "gatccggaattc"), thus 2*9*12 = 216

Sample Input2 : "aggatcctgaggatccggaattc", "gga*tcc"
Sample Output2: 360         # Fragments are "agga", "tcctgagga", "tccggaattc"), thus 4*9*10 = 360  
"""
def calc_restrict_fragment_size_v3(dna, enz):
    # +++your code here+++
    delet=enz.replace("*","")
    all=dna.replace(delet,enz)
    frag=all.split("*")
    size=[]
    i=0
    multi=1
    for i in range(len(frag)):
        size.append(len(frag[i]))
        multi = multi * size[i]
    return multi

    pass

"""
4. kmer_counting_v1
Problem : Given a dna sequence and a list of two numbers (kmer_size, count_cutoff), 
          return the list of kmers that occur greater than or equal to the count_cutoff 
          (i.e., count >= count_cutoff), in alphabetical order.
Sample Input1: "cctgcattcgcccaaat", [2, 3]
Sample Output1: ['cc']   

Sample Input2: "cctgcattcgcccaaat", [2, 2]
Sample Output2: ['aa', 'at', 'ca', 'cc', 'gc']  
"""
def kmer_counting_v1 (dna, lst):
    # +++your code here+++
    pass

"""
5. get_data_from_file_v4
Problem : Given a tsv file (tab-delimited text file) and a list of two numbers (a and b), 
          return the list of 'Name_alt' of orf(s) whose genomic locations are between a and b 
          (i.e., a < location < b) in alphabetical order.
"""
def get_data_from_file_v4 (file, lst):
    # +++your code here+++
    pass

"""
6. find_consensus_peptide
Problem: Given DNA strings, return the peptide encoded by 
         their longest substring shared by all the DNA strings.
         stop codon is denoted as "*"
Sample Input 1 : ["ACGTACGT", "AACCGGTATAA"]
Sample Output 2: 'V'  # Common DNA string is "GTA" encoding valine (V)

Sample Input 2 : ["AGATCCATAG", "CCCCATAGATT", "ACCATAGCC"]
Sample Output 2: "P*"  # # Common DNA string is "CCATAG": "CCA" encodes proline (P) and "TAG" encodes stop codon (*)
"""
def find_consensus_peptide(lst):
    # +++your code here+++

    pass

"""
7. find_orfs_one_strand
Problem : Given a dna sequence, return the list of all ORF candidates of the dna in alphabetical order.  
Sample Input1 : "CCATGAGTTACTAACCC"
Sample Output1:  ['ATGAGTTAC']

Sample Input1 : "CATGAGTTAACCATGCCCTAGC"
Sample Output1: ['ATGAGT', 'ATGCCC']

Hint : 
An ORF is the longest from the start codon (ATG) just before the stop codon (TAG or TGA or TAA).
The length of ORF is a multiple of 3. 
"""
def find_orfs_one_strand (dna):
    # +++your code here+++
    import re
    start = dna.find("ATG")

    print(dna)


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

    print("1. find_duplicate")
    test(find_duplicate([2, 3, 1, 1, 2, 4, 5, 1]), [1, 2])
    test(find_duplicate([10, 2, -3, -1, -2, -4, 5, -1, 10]), [-1, 10])
    
    print("2. calc_at_content")
    test(calc_at_content('attgggcccc'), 0.3)
    test(calc_at_content('ATGCTGATTCTTATTTCACC'), 0.65)

    print("3. calc_restrict_fragment_size_v3")
    test(calc_restrict_fragment_size_v3("aggatcctgaggatccggaattc", "g*gatcc"), 216)
    test(calc_restrict_fragment_size_v3("aggatcctgaggatccggaattc", "gga*tcc"), 360)
    test(calc_restrict_fragment_size_v3("aaaagcttgatcctttaagcttgatccaagcttc", "a*agctt"), 2772)
    test(calc_restrict_fragment_size_v3("actgatcgattacgtatagtagaattctatcatacatatatatcgatgcgttcat", "g*aattc"), 726)

    print("4. kmer_counting_v1")
    test(kmer_counting_v1("cctgcattcgcccaaat", [2, 3]), ['cc'])
    test(kmer_counting_v1("cctgcattcgcccaaat", [2, 2]), ['aa', 'at', 'ca', 'cc', 'gc'])
    dna1 = "cctgcattcgccaaatacccactcgttgatgtgcaaagaagctagcaggttcataaggtttacgggacagttatccgttgccgagacgtccttcgttgcattgtct"
    test(kmer_counting_v1(dna1, [3, 5]), ['gtt'])
    test(kmer_counting_v1(dna1, [4, 3]), ['cgtt', 'gttg', 'tgca'])

    print("5. get_data_from_file_v4")
    test(get_data_from_file_v4("NC_017637.orf.mod.txt", [1, 2000]),  ['ECW_P1m0001', 'ECW_P1m0002'])
    test(get_data_from_file_v4("NC_017637.orf.mod.txt", [15000, 20000]), ['ECW_P1m0020', 'ECW_P1m0021'])
    test(get_data_from_file_v4("NC_017637.orf.mod.txt", [80000, 85000]), ['ECW_P1m0089', 'ECW_P1m0090', 'ECW_P1m0091', 'ECW_P1m0092'])
    test(get_data_from_file_v4("NC_012971.orf.mod.txt", [10000, 15000]), ['ECD_00011', 'ECD_00013', 'ECD_00014'])
    test(get_data_from_file_v4("NC_012971.orf.mod.txt", [100000, 104000]), ['ECD_00090', 'ECD_00091'])
    test(get_data_from_file_v4("NC_012971.orf.mod.txt", [204000, 208000]), ['ECD_00178', 'ECD_00179', 'ECD_00180', 'ECD_00181'])

    print("6. find_consensus_peptide")
    test(find_consensus_peptide(["ACGTACGT", "AACCGGTATAA"]), 'V')
    test(find_consensus_peptide(["AGATCCATAG", "CCCCATAGATT", "ACCATAGCC"]), 'P*')
    test(find_consensus_peptide(["ACGTACGTC", "AAACGTACGTC"]), "TYV")
    test(find_consensus_peptide(["ACGTACGTC", "AAACGTACGTC", "AACCGGTATAA"]), "V")
    test(find_consensus_peptide(["AACCGGTACTTTTAA", "ATACTTTGCACCC", "ACGTAGATTACTTTCAATACA"]), 'YF')
    test(find_consensus_peptide(["AACCGGTACTTTTAA", "ATACTTTGCACCC", "ACGTAGATTACTTTCAATACA", "ATACGCACCC"]), 'Y')

    print("7. find_orfs_one_strand")
    test(find_orfs_one_strand("CCATGAGTTACTAACCC"), ['ATGAGTTAC'])
    test(find_orfs_one_strand("CATGAGTTAACCATGCCCTAGC"), ['ATGAGT', 'ATGCCC'])
    test(find_orfs_one_strand("CATGAATGGACTAACCTAA"), ['ATGAATGGACTAACC', 'ATGGAC'])
    test(find_orfs_one_strand("CATGAGTTACTAACCCATGCCCTAG"), ['ATGAGTTAC', 'ATGCCC'])
    dna1 = "AGCCATGCTAACTCAGGTTACATGGGGATGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG"
    test(find_orfs_one_strand(dna1), ['ATGGAT', 'ATGGGGATGGAT'])
    dna2 = "AGCCATGCTAACATGGGGATGGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCG"
    test(find_orfs_one_strand(dna2),
         ['ATGCTAACATGGGGATGGGAT', 'ATGGGATTAGAGTCTCTTTTGGAA', 'ATGGGGATGGGATTAGAGTCTCTTTTGGAA'])

    print()
    print(" [%s test_passed / %s test_total]" % (repr(no_passed), repr(no_test)))

if __name__ == '__main__':
    main()
