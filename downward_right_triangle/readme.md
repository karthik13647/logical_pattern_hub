# Right-Aligned Inverted Triangle Star Pattern

## Easy

---

**Problem:** Create a program that prints a right-aligned inverted triangle pattern of stars based on user input for the number of rows.

**Description:** Given an integer `n` representing the number of rows, print an inverted triangular pattern where the first row has n stars aligned to the right, the second row has (n-1) stars with one leading space, and so on, until the nth row has 1 star with n leading spaces.

### Examples:

**Example 1:**
```
Input: enter the rows: 4
Output:
 ****
  ***
   **
    *
```

**Example 2:**
```
Input: enter the rows: 5
Output:
 *****
  ****
   ***
    **
     *
```

**Example 3:**
```
Input: enter the rows: 3
Output:
 ***
  **
   *
```

### Constraints:
- `1 <= n <= 100`
- Program should handle positive integers only

### Time Complexity: O(n²)
### Space Complexity: O(1)

### Pattern Analysis:
- Row 1: 1 space + n stars
- Row 2: 2 spaces + (n-1) stars
- Row 3: 3 spaces + (n-2) stars
- ...
- Row n: n spaces + 1 star

---

## How to Run

```bash
python right_aligned_inverted_triangle.py
```

## Contributing

Feel free to contribute more pattern problems and solutions to this collection!