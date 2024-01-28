#!/usr/bin/python3

import re
                
def calc(A, B):
    ai = str(A)
    bi = str(B)
    
    p = re.compile('[+-]?\d+')

    if p.fullmatch(ai) and p.fullmatch(bi):
        a = int(ai)
        b = int(bi)
        
        if 0 < a < 1000 and 0 < b < 1000:
            return a * b
    return -1
        
                
def main():
    matchstring = ''
    while matchstring != 'end':
        A = input('input A: ')
        B = input('input B: ')
        print('input A * input B = ', calc(A, B))

if __name__ == '__main__':
    main()
