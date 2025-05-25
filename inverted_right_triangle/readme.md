# Inverted Triangle Star Pattern

## Easy

---

**Problem:** Create a program that prints an inverted left-aligned triangle pattern of stars based on user input for the number of rows.

**Description:** Given an integer `n` representing the number of rows, print an inverted triangular pattern where the first row has n stars, the second row has (n-1) stars, and so on, until the nth row has 1 star.

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
Input: enter the rows: 6
Output:
******
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
- Row 1: n stars
- Row 2: (n-1) stars
- Row 3: (n-2) stars
- ...
- Row n: 1 star

---

## How to Run

```bash
python inverted_triangle_pattern.py
```

## Contributing

Feel free to contribute more pattern problems and solutions to this collection!
