import clean_CCC
from time import sleep
errs = []
"""for i in range(55521,1114110): #if the range lands on 55000-5900 it will throw a surrogate error so future versions will hav the need to be adjusted
    try:
        a = clean_CCC.CCC(inputfile='input.txt', outputfile='one.txt', shift=i)
        a.cypher()
        x = i * -1
        b = clean_CCC.CCC(inputfile='one.txt', outputfile='two.txt', shift=x)
        b.cypher()
    except: 
        print('error {}'.format(str(i)))
        errs.append(i)
"""