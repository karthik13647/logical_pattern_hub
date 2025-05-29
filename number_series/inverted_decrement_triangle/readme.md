# Left-Aligned Inverted Number Triangle Pattern

## Easy

---

**Problem:** Create a program that prints a left-aligned inverted number triangle pattern based on user input for the number of rows.

**Description:** Given an integer `n` representing the number of rows, print an inverted triangular pattern where each row contains consecutive numbers starting from 1, with increasing leading spaces to create a left-aligned inverted triangle. Row `i` has `i` leading spaces and `(n-i)` numbers.

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
- Row 0: 0 spaces + n numbers (1, 2, 3, ..., n)
- Row 1: 1 space + (n-1) numbers (1, 2, 3, ..., n-1)
- Row 2: 2 spaces + (n-2) numbers (1, 2, 3, ..., n-2)
- Row 3: 3 spaces + (n-3) numbers (1, 2, 3, ..., n-3)
- ...
- Row n: n spaces + 0 numbers (empty row with spaces)

---

## How to Run

```bash
python left_aligned_inverted_number_triangle.py
```

## Contributing

Feel free to contribute more pattern problems and solutions to this collection!