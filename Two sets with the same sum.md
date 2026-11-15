# Two sets with the same sum

**Input:** One integer $n$, with $1 \le n \le 10^6$.

**Task:** Divide $1, 2, \dots, n$ into two sets of equal sum.  
Every number must appear in exactly one set.

**Output:** Report whether it is possible. If so, give a partition.

For $n = 7$, what would you put in each set?

### 1. Feasibility Check (The Parity Condition)
* The total sum of numbers from $1$ to $n$ is given by:
  $$T = \frac{n(n+1)}{2}$$
* To divide the numbers into two subsets of equal sum, each subset must sum to $\frac{T}{2}$.
* Therefore, $T$ **must be an even integer**. If $T$ is odd, an equal partition is impossible, and the answer is `NO`.
* For $T = \frac{n(n+1)}{2}$ to be even, the product $n(n+1)$ must be divisible by $4$. This occurs if and only if:
  $$n \pmod 4 = 0 \quad \text{or} \quad n \pmod 4 = 3$$

---

### 2. The Four-Number Balancing Trick
* For any base value $a$, four consecutive integers $\{a, a+1, a+2, a+3\}$ can always be partitioned into two pairs with identical sums:
  $$a + (a+3) = (a+1) + (a+2) = 2a + 3$$
* Placing the outer values $\{a, a+3\}$ into set $A$ and the inner values $\{a+1, a+2\}$ into set $B$ adds the exact same amount to both sets.

---

### 3. The Construction Algorithm
* **Case 1: $n \pmod 4 = 0$**
  * Start with both sets empty: $A = \emptyset$, $B = \emptyset$.
  * Group the numbers into blocks of $4$ starting from $a = 1$ up to $n$:
    $$\{1, 2, 3, 4\}, \{5, 6, 7, 8\}, \dots$$
  * For each block:
    $$A \leftarrow A \cup \{a, a+3\}$$
    $$B \leftarrow B \cup \{a+1, a+2\}$$

* **Case 2: $n \pmod 4 = 3$**
  * Seed the sets using the first three numbers:
    $$A = \{1, 2\}, \quad B = \{3\} \quad (\text{both sum to } 3)$$
  * Process the remaining $n - 3$ elements in blocks of $4$ starting from $a = 4$:
    $$\{4, 5, 6, 7\}, \{8, 9, 10, 11\}, \dots$$
  * For each block:
    $$A \leftarrow A \cup \{a, a+3\}$$
    $$B \leftarrow B \cup \{a+1, a+2\}$$

---

### 4. Example ($n = 7$)
* Total sum:
  $$T = \frac{7(8)}{2} = 28 \implies \text{Target per set} = 14$$
* **Seed:**
  $$A = \{1, 2\}, \quad B = \{3\}$$
* **Block ($a = 4$):** $\{4, 5, 6, 7\}$
  $$A = \{1, 2, 4, 7\} \implies 1 + 2 + 4 + 7 = 14$$
  $$B = \{3, 5, 6\} \implies 3 + 5 + 6 = 14$$



```python
"""CSES Two Sets / lecture 1: partition 1..n into equal-sum sets."""

def partition(n):
    total = n * (n + 1) // 2
    if total % 2 != 0:
        return None
    A = []
    B = []
    start = 1
    if n % 4 == 3:
        A.extend([1, 2])
        B.append(3)
        start = 4

    for a in range(start, n + 1, 4):
        A.extend([a, a + 3])
        B.extend([a + 1, a + 2])
    return A, B


def main():
    n = int(input())
    result = partition(n)
    if result is None:
        print("NO")
        return

    A, B = result
    print("YES")
    print(len(A))
    print(" ".join(map(str, A)))
    print(len(B))
    print(" ".join(map(str, B)))

if __name__ == "__main__":
    main()

```