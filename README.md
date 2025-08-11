# python-debugging-questions
Use the following git command on cmd to reset changes.
```
git reset --hard

```
## Set A Answer keys
### easy1.py
```
# Expected: "Hello, Alice!"

name = "Alice"
print("Hello, " +name+ "!")

```
### easy2.py
# Expected output: 15
```
total = 0
for i in range(1, 6):
    total += i
print(total)
```
### easy3.py
```
# Expected output: "banana"

fruits = ["apple", "banana", "cherry"]
print(fruits[1])
```
### medium1.py
```
# Expected: 20

def multiply(a, b=5):
    return a * b

result = multiply(a=4)
print(result)
```
### medium2.py
```
# Expected: "blue"

colors = {"apple": "red", "banana": "yellow", "sky": "blue"}
print(colors["sky"])
```
### hard1.py
```
# Expected output: 120 for factorial(5)
def factorial(n):
    return n * factorial(n - 1)
print(factorial(5))   
```

## Set B Answer Keys
### easy1.py
```
text = "hello world"
print(" ".join(word.capitalize() for word in text.split()))
# or
text = "hello world"
print(text.title())  # Hello World
```
### easy2.py
```
# Expected: 3.0

numbers = [2, 3, 4]
average = sum(numbers[:]) / len(numbers)
print(average)

```
### easy3.py
```
nums = [1, 2, 3, 4, 5]
nums.reverse()  
print(nums)     
```
### medium1.py
```
# Expected: [2, 4, 6]

nums = [1, 2, 3, 4, 5, 6]
for n in nums:
    if n % 2 != 0:
        nums.remove(n)
print(nums)

```
### medium2.py
```
# Expected: ['2', '10', '25', '100']

nums = ['10', '2', '100', '25']
nums.sort(key=int)
print(nums)
```

### hard1.py
```
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n-1) + fib(n-2)

for i in range(7):
    print(fib(i))
```