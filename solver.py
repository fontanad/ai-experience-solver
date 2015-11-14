'''
Program for automatic solving the experience
'''
import subprocess

COMBINATIONS = [2, 5, 10]

def main():
    '''
    Main of the program
    '''
    valori = []
    mediane = []
    for i in range(1, 5):
        for k in range(0, 3):
             for j in range(0, 5):
                print "./nnet" + " trainFold" + str(i) + ".txt" + \
                       " testFold" + str(i) + ".txt" + " -hl " +  str(1) \
                       + " "  + str(COMBINATIONS[k]) + " | grep Accuracy"
    return 0

if __name__ == '__main__':
    main()
