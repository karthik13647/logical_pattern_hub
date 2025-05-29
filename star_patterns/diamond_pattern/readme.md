# Diamond Star Pattern

## Medium

---

**Problem:** Create a program that prints a diamond-shaped pattern of stars with spaces between each star, based on user input for the number of rows.

**Description:** Given an integer `n` representing the number of rows for each half, print a diamond pattern where each star is followed by a space. The pattern consists of two parts: an upper triangle that grows from 1 star to (2n-1) stars, followed by a lower inverted triangle that shrinks from (2n-1) stars back to 1 star.

### Examples:

**Example 1:**
```
Input: enter the rows: 3
Output:
  *
 * *
* * *
 * *
  *
```

**Example 2:**
```
Input: enter the rows: 4
Output:
   *
  * *
 * * *
* * * *
 * * *
  * *
   *
```

**Example 3:**
```
Input: enter the rows: 2
Output:
 *
* *
 *
```

### Constraints:
- `1 <= n <= 100`
- Program should handle positive integers only

### Time Complexity: O(n²)
### Space Complexity: O(1)

### Pattern Analysis:
**Upper Triangle (n-1 rows):**
- Row 1: (n-1) double spaces + 1 star
- Row 2: (n-2) double spaces + 3 stars
- ...
- Row (n-1): 1 double space + (2n-3) stars

**Lower Triangle (n rows):**
- Row 1: 1 double space + (2n-1) stars
- Row 2: 2 double spaces + (2n-3) stars
- ...
- Row n: n double spaces + 1 star

---

## How to Run

```bash
python diamond_star_pattern.py
```

## Contributing

Feel free to contribute more pattern problems and solutions to this collection!