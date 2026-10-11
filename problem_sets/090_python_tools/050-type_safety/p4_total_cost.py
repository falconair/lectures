"""
PROBLEM 4
Practises: reading mypy's report and repairing the annotations it points to.

Task: repair the type annotations of cost_with_commission and total_cost.
Two of them are wrong. The code itself is correct: change only annotations.

To check your work, type these two commands:
    mypy --strict p4_total_cost.py
    python p4_total_cost.py

They should print:
    Success: no issues found in 1 source file
    708.68
"""


def cost_with_commission(price: float, commission_rate: int) -> float:
    """Return what it costs to buy one share at price, with the broker's commission added.

    commission_rate is a fraction of the price: 0.001 means 0.1%.
    """
    return price * (1 + commission_rate)


def total_cost(prices: list[float], broker: str, commission_rates: dict[str, float]) -> str:
    """Return what it costs to buy one share at each of prices through broker.

    commission_rates gives each broker's commission rate.
    """
    total = 0.0
    for price in prices:
        total += cost_with_commission(price, commission_rates[broker])
    return total


# ---- do not change anything below this line --------------------------------
if __name__ == "__main__":
    commission_rates = {"FAST": 0.001, "CHEAP": 0.0005}
    closes = [229.72, 238.47, 239.78]  # AAPL's first three closes of September 2025
    print(f"{total_cost(closes, 'FAST', commission_rates):.2f}")
