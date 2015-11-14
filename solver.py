'''
Program for automatic solving the experience
'''
import subprocess
from collections import defaultdict

COMBINATIONS = [2, 5, 10]

def main():
    '''
    Main of the program
    '''
    max_medians = []
    values = []
    medians = defaultdict(list)
    for i in range(1, 5): #number of test and train fold (1..4)
        for k in COMBINATIONS: #numbers of combinations (3 types)
            for j in range(0, 5): #number of the same command to repeate (5)
                bash_command = "./nnet" + " trainFold" + str(i) + ".txt" + \
                       " testFold" + str(i) + ".txt" + " -hl " +  str(1) \
                       + " "  + str(COMBINATIONS[k]) + " | grep Accuracy"
                exit_command = subprocess.check_output(bash_command, \
                                                shell=True)
                #parsing the exit command
                exit_command = exit_command.replace('Accuracy:', '')
                exit_command = exit_command.replace('.000%', '')
                exit_command = exit_command.replace(' ', '')#if a space occur
                values.append(int(exit_command))
                print exit_command #verify if the exit matching with our idea
                #end of j for
            values.sort()
            medians[k].append(values[2]) #add the medians of all configuration

    for combinations in medians:
        max_medians.append(max(combinations))
    best_configuration = max_medians.index(max(max_medians))
    print 'best combination is ' + str(1) + ' ' \
        + str(COMBINATIONS[best_configuration])
    print 'remove old log.txt'
    subprocess.check_output('rm log.txt', shell=True)
    print 'launching final training'
    subprocess.check_output('./nnet train.txt test.txt -hl ' + str(1) \
        + str(COMBINATIONS[best_configuration]) + ' -va validation.txt', shell=True) 
    print 'now check the log.txt baby ;)'
if __name__ == '__main__':
    main()
