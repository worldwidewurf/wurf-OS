from os import system, name
import random
import time
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
def guide():
    lett = 'abgfkpqlmhcdejinotu'
    # lst = lett.split(',')
    lst = [*lett]
    # print(lst)
    a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v = '',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '

    # print(maze)
        

    for z in range(len(lst)):
        go = lst[z]
        if go == 'a':
            a = '♛'
            
        if go == 'b':
            b = '♛'    
        if go == 'c':
            c = '♛'    
        if go == 'd':
            d = '♛'    
        if go == 'e':
            e = '♛'    
        if go == 'f':
            f = '♛'    
        if go == 'g':
            g = '♛'    
        if go == 'h':
            h = '♛'    
        if go == 'i':
            i =   '♛'  
        if go == 'j':
            j = '♛'    
        if go == 'k':
            k = '♛'    
        if go == 'l':
            l = '♛'    
        if go == 'm':
            m = '♛'    
        if go == 'n':
            n = '♛'    
        if go == 'o':
            o = '♛'    
        if go == 'p':
            p = '♛'    
        if go == 'q':
            q = '♛'    
        if go == 'r':
            r = '♛'    
        if go == 's':
            s = '♛'    
        if go == 't':
            t = '♛'    
        if go == 'u':
            u = '♛'    
        if go == 'v':
            v = '♛'
        clear()
        maze =f'''
                ┌ ─ ┐┌ ─ ┐┌ ─ ┐┌ ─ ┐┌ ─ ┐
            {a}      {a}    {b}|| {c}   {d}      {e}|
                └ ─ ┘└   ┘└   ┘└ ─ ┘└   ┘
                ┌ ─ ┐┌   ┐┌   ┐┌ ─ ┐┌   ┐
                | {f}     {g}||  {h}|| {i}    {j}|
                └   ┘└ ─ ┘└   ┘└   ┘└ ─ ┘
                ┌   ┐┌ ─ ┐┌   ┐┌   ┐┌ ─ ┐
                |  {k}|| {l}     {m}|| {n}     {o}|
                └   ┘└   ┘└ ─ ┘└ ─ ┘└   ┘
                ┌   ┐┌   ┐┌ ─ ┐┌ ─ ┐┌   ┐
                | {p}     {q}||  {r}||  {s}|| {t}      {u}⟰ 
                └ ─ ┘└ ─ ┘└ ─ ┘└ ─ ┘└ ─ ┘    Home
    '''
        print(maze)
        time.sleep(0.25)
    

if __name__ == "__main__":
    guide()