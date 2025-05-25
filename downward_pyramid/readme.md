# Inverted Full Equilateral Triangle Star Pattern

## Easy

---

**Problem:** Create a program that prints an inverted full equilateral triangle pattern of stars with spaces between each star, based on user input for the number of rows.

**Description:** Given an integer `n` representing the number of rows, print an inverted equilateral triangular pattern where each star is followed by a space. The first row has the maximum number of stars (2n-1) with 1 double leading space, and each subsequent row decreases by 2 stars while increasing the leading spaces, until the last row has 1 star.

### Examples:

**Example 1:**
```
Input: enter the rows: 4
Output:
  * * * * * * * 
    * * * * * 
      * * * 
        * 
```

**Example 2:**
```
Input: enter the rows: 5
Output:
  * * * * * * * * * 
    * * * * * * * 
      * * * * * 
        * * * 
          * 
```

**Example 3:**
```
Input: enter the rows: 3
Output:
  * * * * * 
    * * * 
      * 
```

### Constraints:
- `1 <= n <= 100`
- Program should handle positive integers only

### Time Complexity: O(n²)
### Space Complexity: O(1)

### Pattern Analysis:
- Row 1: 1 double space + (2n-1) stars
- Row 2: 2 double spaces + (2n-3) stars
- Row 3: 3 double spaces + (2n-5) stars
- ...
- Row n: n double spaces + 1 star

---

## How to Run

```bash
python inverted_full_equilateral_triangle.py
```

## Contributing

Feel free to contribute more pattern problems and solutions to this collection!