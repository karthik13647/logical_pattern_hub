# Inverted Number Triangle Pattern

## Easy

---

**Problem:** Create a program that prints an inverted number triangle pattern based on user input for the number of rows.

**Description:** Given an integer `n` representing the number of rows, print an inverted triangular pattern where each row contains consecutive numbers starting from 1. The first row contains `n` numbers, and each subsequent row decreases by 1 number until the last row has 0 numbers.

### Examples:

**Example 1:**
```
Input: enter the no of rows: 4
Output:
1 2 3 4 
1 2 3 
1 2 
1 

```

**Example 2:**
```
Input: enter the no of rows: 5
Output:
1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1 

```

**Example 3:**
```
Input: enter the no of rows: 3
Output:
1 2 3 
1 2 
1 

```

### Constraints:
- `1 <= n <= 100`
- Program should handle positive integers only

### Time Complexity: O(n²)
### Space Complexity: O(1)

### Pattern Analysis:
- Row 1: n numbers (1, 2, 3, ..., n)
- Row 2: (n-1) numbers (1, 2, 3, ..., n-1)
- Row 3: (n-2) numbers (1, 2, 3, ..., n-2)
- ...
- Row n: 1 number (1)
- Row n+1: 0 numbers (empty row)

---

## How to Run

```bash
python inverted_number_triangle_pattern.py
```

## Contributing

Feel free to contribute more pattern problems and solutions to this collection!