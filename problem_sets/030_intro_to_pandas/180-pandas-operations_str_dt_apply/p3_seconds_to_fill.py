"""
PROBLEM 3
Practises: turning two columns of FIX timestamps into dates, and the time
between them into seconds with .dt.

Task: fill in the function seconds_to_fill.

To check your work, type:
    python p3_seconds_to_fill.py

It should print the first five orders in executions.csv, with what seconds_to_fill
returned for them in the last column:
    order_id            order_time        execution_time  seconds
      ID8195 20250910-08:01:56.292 20250910-08:02:05.550    9.258
     ID14463 20250910-08:06:48.677 20250910-08:10:19.403  210.726
     ID29092 20250910-08:19:18.573 20250910-08:19:18.679    0.106
      ID3988 20250910-08:00:07.549 20250910-08:28:40.937 1713.388
      ID5529 20250910-08:00:14.171 20250910-08:28:40.949 1706.778
"""

from pathlib import Path

import pandas as pd

# executions.csv sits in the same folder as this file, wherever you run it from
EXECUTIONS = Path(__file__).parent / "executions.csv"


def seconds_to_fill(executions_df: pd.DataFrame) -> pd.Series:
    """Return how many seconds each order waited before it was filled.

    Args:
        executions_df: one row per order, with the columns order_time and
            execution_time. Both are text in the FIX format
            "YYYYMMDD-HH:MM:SS.sss", such as "20250910-08:01:56.292".

    Returns:
        A Series with one value per row of executions_df: the seconds from
        order_time to execution_time, with the fractions of a second.

    Example:
        executions_df = pd.DataFrame({"order_time": ["20250910-13:30:00.000", "20250910-13:30:59.500"],
                                      "execution_time": ["20250910-13:30:01.500", "20250910-13:31:00.000"]})
        seconds_to_fill(executions_df)
    returns
        0    1.5
        1    0.5
    """
    raise NotImplementedError  # YOUR WORK: replace this line


# ---- do not change anything below this line --------------------------------
if __name__ == "__main__":
    executions_df = pd.read_csv(EXECUTIONS)
    executions_df["seconds"] = seconds_to_fill(executions_df)
    columns = ["order_id", "order_time", "execution_time", "seconds"]
    print(executions_df[columns].head().to_string(index=False))

# NOTES
#   Subtracting one column of dates from another gives a column of durations.
#   Its .dt.total_seconds() gives each duration in seconds.
