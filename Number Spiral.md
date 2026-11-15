### 1. The Core Bottleneck & Problem Analysis
* We are given $t$ queries ($1 \le t \le 10^5$), each with row $y$ and column $x$ ($1 \le y, x \le 10^9$).
* An explicit grid simulation would require up to $10^{18}$ cells, which is far too large in both time and memory.
* Instead, we compute the answer directly in $\mathcal{O}(1)$ time per query by decomposing the spiral into square layers.

---

### 2. Identifying the Layer and Base Offset
* **Layer index ($k$):** The cell $(y, x)$ belongs to the square shell of size:
  $$k = \max(y, x)$$
* **Inner cells ($b$):** The complete inner square of size $(k - 1) \times (k - 1)$ already contains:
  $$b = (k - 1)^2 \text{ numbers}$$
* The numbers in layer $k$ range from $b + 1$ to $k^2$, so the final answer is:
  $$\text{Answer} = b + \text{position along the border}$$

---

### 3. Layer Direction and Parity
The direction of traversal alternates depending on whether $k$ is even or odd:
* **Even layer ($k$ is even):** Runs **down** the right column ($x = k$), then **left** across the bottom row ($y = k$).
* **Odd layer ($k$ is odd):** Runs **right** along the bottom row ($y = k$), then **up** the right column ($x = k$).

---

### 4. Direct Closed-Form Calculation

* **Case 1: Even Layer ($k \pmod 2 = 0$)**
  * **On the right column ($x \ge y$):** Traversal moves downward from row $1$ to row $y$:
    $$\text{Answer} = b + y$$
  * **On the bottom row ($y > x$):** Traversal moves all the way down $k$ units, then left by $k - x$ units:
    $$\text{Answer} = b + k + (k - x) = b + 2k - x$$

* **Case 2: Odd Layer ($k \pmod 2 = 1$)**
  * **On the bottom row ($y \ge x$):** Traversal moves rightward across columns from $1$ to $x$:
    $$\text{Answer} = b + x$$
  * **On the right column ($x > y$):** Traversal moves all the way right $k$ units, then up by $k - y$ units:
    $$\text{Answer} = b + k + (k - y) = b + 2k - y$$

*(Note: At the corner where $y = x = k$, both formulas simplify to $b + k$.)*

---

### 5. Summary Table

| Location | Odd Layer ($k \pmod 2 = 1$) | Even Layer ($k \pmod 2 = 0$) |
| :--- | :--- | :--- |
| **Bottom row** ($y > x$) | $b + x$ | $b + 2k - x$ |
| **Right column** ($x \ge y$) | $b + 2k - y$ | $b + y$ |

---

### 6. Worked Example: $(y, x) = (4, 2)$
1. $k = \max(4, 2) = 4$ (an **even** layer).
2. $b = (4 - 1)^2 = 9$.
3. Since $y > x$ ($4 > 2$), the cell is on the **bottom row**:
   $$\text{position} = 2k - x = 2(4) - 2 = 6$$
   $$\text{Answer} = b + \text{position} = 9 + 6 = 15$$

```python
"""CSES Number Spiral / lecture 2: find the value at row y, column x."""

def number_spiral(y, x):
    if y > x:
        base = (y - 1) ** 2
        if y % 2 == 1:
            return base + x
        return base + 2 * y - x

    base = (x - 1) ** 2
    if x % 2 == 1:
        return base + 2 * x - y
    return base + y

def main():
    t = int(input())
    for _ in range(t):
        y, x = map(int, input().split())
        print(number_spiral(y, x))

if __name__ == "__main__":
    main()
```