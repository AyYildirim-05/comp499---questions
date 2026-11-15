# Problem Statement
The problem asks you to find the maximum number from a given set of integers, or detect if the set has no numbers.

### Input
* **Line 1:** An integer $k$, representing how many numbers are in the set.
* **Line 2:** The $k$ space-separated integers (this line is empty if $k = 0$).

### Output
* If $k = 0$, print the word `empty`.
* If $k > 0$, print the largest (maximum) integer from the set on a separate line.

```python
# read two integers separated by space and output their product
line = input()
strVals = line.split(' ')
n = int(strVals[0])

if n==0:
    print("empty")
    exit()


line = input()
strVals = line.split(' ')

v=[]

for i in range(0, n):
    v.append(int(strVals[i]))

m = v[0]

for i in range(1, n):
    if m<v[i]:
        m = v[i]

print(m)
```


```java
// Solution 1: Tokens
import java.util.*;
import java.util.Vector;

public class Main {	
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        
        if(n==0) {
            System.out.print("empty");
            return;
        }
        
        Vector<Integer> v = new Vector<>();
        
        for(int i=0;i<n;i=i+1){
            int l = scan.nextInt();
            v.add(l);
        }
		scan.close();
		
        int m = v.get(0);
        
        for(int i=1;i<n;i++){
            if(m<v.get(i))
                m = v.get(i);
        }
        
		System.out.print(m);
    }
}
```

```java
//Solution 2
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int k = Integer.parseInt(scan.next());

        if (k == 0) {
            System.out.println("empty");
            return;
        }

        int maxVal = Integer.parseInt(scan.next());

        for (int i = 1; i < k; i++) {
            int current = Integer.parseInt(scan.next());
            if (current > maxVal) {
                maxVal = current;
            }
        }

        System.out.println(maxVal);
    }
}
```