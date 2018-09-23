import re
import os
import sys
import concurrent.futures
from collections import defaultdict


def main(argv):
    input_commands = ['mkdir', 'cd', 'cd /', 'pwd', 'help', 'rm', 'ls', 'rmdir', 'clear', 'session clear']
    d = defaultdict(list)
    l = []
    # for root
    cur = '/'
    temp = cur
    if argv:

        #for printing current working directory.
        if argv[0] == 'pwd':
            print('PATH: {}'.format(cur), end='\n')


        #for creating new directory.
        elif argv[0] == 'mkdir':
            if argv[1] is None:
                print('PLEASE ENTER NAME OF DIRECTORY !', end='\n')
            elif argv[1] in d.values():
                print('ERR : DIR ALREADY EXIST ', end='\n')
            else:
                d[cur] = l.extend(argv[1:])


        #for entering in direrctory.
        elif argv[0] == 'cd':
            print(argv[1])
            if argv[1] in d.values():
                #updating the directory path
                cur = str(cur)+str(argv[1:])
                print("SUCCESSFULLY REACHED!", end='\n')

            elif argv[1] not in d.values():
                print("ERR: INVALID PATH", end='\n')


        #for coming out from directory.
        elif argv[0] == 'cd /':
            cur_dirs = os.getcwd()
            new_dirs = cur_dirs.split('\\')
            dirs = new_dirs[-1]
            if dirs:
                cur = '\\'.join(map(str, new_dirs[:len(new_dirs)-1]))
                cur = str(cur)
                print("SUCCESSFULLY REACHED", end='\n')
            else:
                print("ERR: INVALID DIRECTORY", end='\n')


        #for printing list under directories.
        elif argv[0] == 'ls':
            print(d[cur], end=' ')


        #for clear the session.
        elif argv[0] == "clear" or "session clear":
            cur = temp
            print('SUCC: CLEARED: RESET TO ROOT')
            print("\n")


        #removing the current directory from list.
        elif argv[0] == 'rm':
            cur = list(cur.split('\\'))
            cur = '\\'.join(map(str, cur[:len(cur)-1]))
            print("SUCCESSFULL: DELETED", end='\n')

        #other input or INVALID INPUT.
        elif argv[0] not in input_commands:
            print("ERR. CANNOT RECOGNIZE INPUT", end='\n')


    elif argv is None:
        print("provide command line arguments ! please.")


#driber code.
if __name__ == '__main__':

    while True:
        cmd_input = input().split()
        if cmd_input[0] == 'exit':
            break
        else:
            main(cmd_input)
