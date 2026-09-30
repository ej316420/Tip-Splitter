# 🍽️ Tip Splitter

A tiny Python program that splits a restaurant bill, including tip, evenly between friends.

## Features
- Enter the bill, tip %, and number of people
- Friendly error messages for bad input
- No libraries needed, just Python 3

## How to run
```bash
python tip_splitter.py
```

## Example
```
=== Tip Splitter ===
Bill total: 2400
Tip % (e.g. 10): 10
Number of people: 4
Each person pays: 660.00
```

## Run the tests
```bash
python -m unittest
```

## Use it in your own code
```python
from tip_splitter import split_bill
print(split_bill(100, 15, 3))  # 38.33
```

## License
MIT
