# Uncommon Python Error Handling

This repository demonstrates some less frequently encountered errors in Python and how to handle them gracefully.  The examples showcase ZeroDivisionError, KeyError, and TypeError, focusing on exception handling best practices.

## Code Description:

The `bug.py` file contains a function that might raise one of the three exceptions mentioned above.  The `bugSolution.py` file presents the improved version with more robust exception handling.

## How to run
1. Clone this repo
2. Run the python script `bug.py` using python interpreter
3. Run the python script `bugSolution.py` using python interpreter

## Potential Improvements:
- More comprehensive exception handling (consider using `Exception` as a catch-all for unforeseen errors).
- Logging (using libraries such as `logging`) to record errors for debugging and analysis.