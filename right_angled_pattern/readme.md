# Triangle Star Pattern

## Easy

---

**Problem:** Create a program that prints a left-aligned triangle pattern of stars based on user input for the number of rows.

**Description:** Given an integer `n` representing the number of rows, print a triangular pattern where the first row has 1 star, the second row has 2 stars, and so on, until the nth row has n stars.

### Examples:

**Example 1:**
```
Input: enter the rows: 4
Output:
*
**
***
****
```

**Example 2:**
```
Input: enter the rows: 6
Output:
*
**
***
****
*****
******
```

**Example 3:**
```
Input: enter the rows: 1
Output:
*
```

### Constraints:
- `1 <= n <= 100`
- Program should handle positive integers only

### Time Complexity: O(n²)
### Space Complexity: O(1)

### Pattern Analysis:
- Row 1: 1 star
- Row 2: 2 stars
- Row 3: 3 stars
- ...
- Row n: n stars

---

## How to Run

```bash
python triangle_pattern.py
```

## Contributing

Feel free to contribute more pattern problems and solutions to this collection!