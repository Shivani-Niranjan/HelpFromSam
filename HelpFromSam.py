'''
Alex and Sam are good friends. Alex is doing a lot of programming these days. He has set a target score of A for himself.
Initially, Alex's score was zero. Alex can double his score by doing a question, or Alex can seek help from Sam for doing questions that will contribute 1 to Alex's score. Alex wants his score to be precisely A. Also, he does not want to take much help from Sam.

Find and return the minimum number of times Alex needs to take help from Sam to achieve a score of A..

Input 1:
A = 5

Input 2:
A = 3

Output 1:
2

Output 2:
2
'''

def HelpFromSam_1(target):
    help = 1

    while (target > 1):
        if target % 2 == 1:
            help += 1
            target -= 1
        target = target / 2
    return (help)

target = int(input())
print(HelpFromSam_1(target))    

