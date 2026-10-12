"""
PROBLEM 1
Practises: tidying code with a linter and a formatter, and choosing names.

Task: tidy the program below, without changing what it prints. Rename
anything whose name does not say what it holds.

To check your work, type these three commands:
    ruff check --select E,W,F,I,N p1_month_summary.py
    ruff format --check p1_month_summary.py
    python p1_month_summary.py AAPL

They should print:
    All checks passed!
    1 file already formatted
    AAPL first 229.72 last 254.63 return 10.84% up days 11 of 20
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

# NOTES
#   The letters after --select choose ruff's rules. E, W: layout. F: imports and
#   unused names. I: the order of the imports. N: Python's naming conventions.
#   "ruff check --fix" and "ruff format" make the changes that are safe for ruff
#   to make. No tool can choose a good name for you.
