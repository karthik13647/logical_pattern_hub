# Right-Aligned Number Triangle Pattern

## Easy

---

**Problem:** Create a program that prints a right-aligned number triangle pattern based on user input for the number of rows.

**Description:** Given an integer `n` representing the number of rows, print a triangular pattern where each row contains consecutive numbers starting from 1, with appropriate leading spaces to create a right-aligned triangle. Row `i` contains `i` numbers with `(n-i)` leading spaces.

### Examples:

**Example 1:**
```
Input: enter the no of rows: 4
Output:
        
      1 
    1 2 
  1 2 3 
1 2 3 4 
```

**Example 2:**
```
Input: enter the no of rows: 5
Output:
          
        1 
      1 2 
    1 2 3 
  1 2 3 4 
1 2 3 4 5 
```

**Example 3:**
```
Input: enter the no of rows: 3
Output:
      
    1 
  1 2 
1 2 3 
```

### Constraints:
- `1 <= n <= 100`
- Program should handle positive integers only

### Time Complexity: O(n²)
### Space Complexity: O(1)

### Pattern Analysis:
- Row 0: n spaces + 0 numbers (empty row with spaces)
- Row 1: (n-1) spaces + 1 number (1)
- Row 2: (n-2) spaces + 2 numbers (1, 2)
- Row 3: (n-3) spaces + 3 numbers (1, 2, 3)
- ...
- Row n: 0 spaces + n numbers (1, 2, 3, ..., n)

---

## How to Run

```bash
python right_aligned_number_triangle.py
```

## Contributing

Feel free to contribute more pattern problems and solutions to this collection!