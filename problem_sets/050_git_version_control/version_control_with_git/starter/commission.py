"""Work out what a day's trades cost us in commission."""
import csv

COMMISSION_PER_SHARE = 0.005
MINIMUM_COMMISSION = 1.00


def commission(shares):
    return max(shares * COMMISSION_PER_SHARE, MINIMUM_COMMISSION)


total = 0.0
with open("trades.csv") as f:
    for row in csv.DictReader(f):
        total += commission(int(row["shares"]))

print(f"Total commission: ${total:.2f}")
