"""Check that every problem set still matches a lecture.

    python problems/check_names.py        (run from anywhere)

The rule: problems/<topic folder>/<name>/ belongs to the lecture file
lectures/<topic folder>/<name>.<anything> (a notebook, a markdown file, a deck).
If a lecture is renamed or moved, its problem set must be renamed or moved the
same way. This prints every problem set that no longer has a lecture, with the
closest lecture names, and exits with status 1 if there are any.
"""

import difflib
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
LECTURES = REPO / "lectures"
PROBLEMS = REPO / "problems"


def lecture_names(topic):
    """Names of the lecture files in one topic folder, without their extensions."""
    folder = LECTURES / topic
    if not folder.is_dir():
        return None
    return sorted({path.stem for path in folder.iterdir() if path.is_file() and not path.name.startswith(".")})


def main():
    mismatches = 0
    checked = 0
    for topic_folder in sorted(p for p in PROBLEMS.iterdir() if p.is_dir()):
        names = lecture_names(topic_folder.name)
        for problem_set in sorted(p for p in topic_folder.iterdir() if p.is_dir()):
            checked += 1
            where = f"problems/{topic_folder.name}/{problem_set.name}"
            if names is None:
                topics = [p.name for p in LECTURES.iterdir() if p.is_dir()]
                close = difflib.get_close_matches(topic_folder.name, topics, n=3)
                print(f"NO MATCH  {where}\n          there is no folder lectures/{topic_folder.name}/. Closest: {close or 'none'}")
                mismatches += 1
            elif problem_set.name not in names:
                close = difflib.get_close_matches(problem_set.name, names, n=3)
                print(f"NO MATCH  {where}\n          no lecture file named {problem_set.name}.* in lectures/{topic_folder.name}/. Closest: {close or 'none'}")
                mismatches += 1
    print(f"{checked} problem set(s) checked, {mismatches} without a lecture")
    sys.exit(1 if mismatches else 0)


if __name__ == "__main__":
    main()
