# Equilateral Triangle Star Pattern

## Easy

---

**Problem:** Create a program that prints an equilateral triangle pattern of stars with spaces between each star, based on user input for the number of rows.

**Description:** Given an integer `n` representing the number of rows, print an equilateral triangular pattern where each star is followed by a space, the first row has 1 star centered with (n-1) leading spaces, the second row has 2 stars with (n-2) leading spaces, and so on, until the nth row has n stars with no leading spaces.

### Examples:

**Example 1:**
```
Input: enter the rows: 4
Output:
   * 
  * * 
 * * * 
* * * * 
```

**Example 2:**
```
Input: enter the rows: 5
Output:
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
```

**Example 3:**
```
Input: enter the rows: 3
Output:
  * 
 * * 
* * * 
```

### Constraints:
- `1 <= n <= 100`
- Program should handle positive integers only

### Time Complexity: O(n²)
### Space Complexity: O(1)

### Pattern Analysis:
- Row 1: (n-1) spaces + 1 star + 1 space
- Row 2: (n-2) spaces + 2 stars (each followed by a space)
- Row 3: (n-3) spaces + 3 stars (each followed by a space)
- ...
- Row n: 0 spaces + n stars (each followed by a space)

---

## How to Run

```bash
python equilateral_triangle.py
```

## Contributing

Feel free to contribute more pattern problems and solutions to this collection!