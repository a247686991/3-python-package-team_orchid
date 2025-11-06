from __future__ import annotations
import random
from typing import Iterable, List


ASCII_ART = r"""
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&%%%##(##&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%#%%%%%%%%%#######%@&@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@%%#%%&%%%###%%####(#%&&&%%%%&&@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@%&&&&&#((///((((////**////(#&&&&&&%@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@&&&&&&%#(////***************////(#@@&&&@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@&&&@&#(///***************,*****///(&@&&&@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@&&&&&#(///********,,,,,,,,,,,****///(&&&&&@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@&&&&%(////*****,*,*,,,,,,,,,,,,****//#&&@&@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@&&&&&%(////*******,,,,,,,,,,********//(&&&&&@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@&@&&&%////**********,,,,,,,,,,******//(%&&&&@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@&@@&&%(///*******,,,,,,,,,,,,,,******//#&@&&@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@&&@@&%(///(#(####(/****,**//(%%%%##(///(&&&@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@&&&&(//%###%##%%###(/***/(((%&&&&%###((&@&//@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@(((#&&(//(#%#(*##,/(/(/***///(**#*/(((///&%#((/@@@@@@@@@@@@@@@@
"""


def compute_avg(*grades: float) -> float:
    """
    Pure function: returns the numeric average.
    Raises:
      - ValueError if no grades are provided.
      - TypeError if a non-numeric is passed.
    """
    if len(grades) == 0:
        raise ValueError("at least one grade is required")
    total = 0.0
    for g in grades:
        total += float(g)  # will raise if not convertible to float
    return total / len(grades)


DEFAULT_QUOTES = [
    "everything is due at class time",
    "ask Bloombot",
    "Quizzes: 25%",
    "Exercises & Projects: 75%",
    "Discord is our main source of communication",
]


def pick_quotes(n: int = 1, pool: Iterable[str] | None = None) -> List[str]:
    if n < 1:
        raise ValueError("n must be >= 1")
    src = list(pool) if pool is not None else DEFAULT_QUOTES
    return [random.choice(src) for _ in range(n)]




def _bubble_block(lines: List[str]) -> str:
    max_len = max((len(line) for line in lines), default=0)
    border = "-" * (max_len + 2)
    out = [f"  {border}"]
    for line in lines:
        out.append(f"< {line.ljust(max_len)} >")
    out.append(f"  {border}")
    return "\n".join(out)


def avg_print(*grades: float) -> None:
    avg = compute_avg(*grades)
    msg = f"Your average grade is {avg:.2f}"
    print(_bubble_block([msg]))
    print(ASCII_ART)


def random_quote_print(n: int = 1) -> None:
    lines = pick_quotes(n)
    print(_bubble_block(lines))
    print(ASCII_ART)
