"""
PROBLEM 1: make ruff pass without changing what the program prints

YOUR TASK
    Change the lines below the line marked YOUR WORK (here, the whole program).
    Do not edit this comment. Your work is checked by running the commands under
    WHEN YOU ARE DONE; a person then reads your names and comments.
    - ruff check with the rules E,W,F,I,N reports nothing, without any "# noqa".
    - ruff format --check finds nothing to change.
    - The program prints exactly what it prints now, with the same exit status.
    - Names tell a stranger what each thing holds. No linter can judge this:
      "x" and "tkr" pass the linter as they are.
    - Comments that only repeat the code are deleted.
    - The lines that run the program stay at the bottom of the file, outside any
      function (you may rename what is in them). No "if __name__ == ..." is needed.
    Docstrings are not asked for here; that is problem 2.

THE PROGRAM
    It prints one stock's month: the first and last closing price, the return
    between them, and on how many days the price closed higher than the day before.
    Try it:  python p1_month_summary.py AAPL
    The lines with Path(__file__), csv.DictReader and "%s ..." % (...) read the
    data file and format the output. You can do the task without understanding them.

WHAT IS WRONG WITH IT (this is what you are fixing)
    The answers are right. The code is hard to read and so not safe to change.
    1. The linter reports about 20 problems. Try it:
           ruff check --select E,W,F,I,N p1_month_summary.py
       The letters choose the rules. E, W: layout, and comparisons such as == True.
       F: imports. I: the order of the imports. N: Python's naming conventions.
       Adding --fix lets ruff correct the few that are safe for it to correct.
    2. The formatter would lay out almost every line differently. Try it:
           ruff format --diff p1_month_summary.py
       (--diff only shows the changes; without it, ruff format makes them.)

WHEN YOU ARE DONE, these commands behave like this
    ruff check --select E,W,F,I,N p1_month_summary.py
        All checks passed!
    ruff format --check p1_month_summary.py
        1 file already formatted
    python p1_month_summary.py AAPL
        AAPL first 229.72 last 254.63 return 10.84% up days 11 of 20
    python p1_month_summary.py KO
        KO first 69.06 last 66.32 return -3.97% up days 6 of 20
    python p1_month_summary.py
        usage: python p1_month_summary.py TICKER
    python p1_month_summary.py ZZZ
        no data for ZZZ
    The last two end with exit status 1. (0 means a program worked.) To see the
    status of the program you just ran, type:  echo $?
"""

# ---- YOUR WORK: everything below this line ---------------------------------
import sys,os,csv
from pathlib import Path
from math import *
pricesFile=Path(__file__).parent/"prices.csv"
def GetCloses(T):
    # open the file
    l=[]
    with open(pricesFile,newline="") as F:
        # loop over the rows
        for Row in csv.DictReader(F):
            if (Row["ticker"]==T)==True: l.append(float(Row["close"]))
    return l
def countUp( l ):
    N=0
    for i in range(1,len(l)):
        if l[i]>l[i-1]: N=N+1
    return N
if len(sys.argv)!=2:
    print("usage: python p1_month_summary.py TICKER");sys.exit(1)
tkr=sys.argv[1]
x=GetCloses(tkr)
if x==[]:
    print("no data for",tkr);sys.exit(1)
Ret=(x[-1]/x[0]-1)*100
print("%s first %.2f last %.2f return %.2f%% up days %d of %d"%(tkr,x[0],x[-1],Ret,countUp(x),len(x)-1))
