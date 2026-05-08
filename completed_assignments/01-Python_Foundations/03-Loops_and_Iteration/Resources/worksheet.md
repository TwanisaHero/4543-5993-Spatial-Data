# 📝 Worksheet: 04 - Loops and Iteration

Practice and reflect on how loops work in Python.

---

## 🔁 Section 1: For Loops

1. What does `range(5)` produce?

`Answer:` It produces the numbers `0, 1, 2, 3, 4`.

2. Write a `for` loop that prints numbers 1 to 10, but skips 5.

```python
for number in range(1, 11):
    if number == 5:
        continue
    print(number)
```

---

## 🔁 Section 2: While Loops

3. What’s the difference between a `for` loop and a `while` loop?

`Answer:` A `for` loop is best when you know what sequence to loop over. A `while` loop keeps running until its condition becomes `False`.

4. What happens if a `while` loop's condition never becomes `False`?

`Answer:` It becomes an infinite loop and keeps running until the program is interrupted or the condition changes.

---

### ✏️ Task: Countdown with While

```python
count = 5
while count >= 1:
    print(count)
    count -= 1
```

---

## 📁 Section 3: File Reading and `with`

5. What does the `with` statement do when opening a file?

`Answer:` It opens the file and automatically closes it when the block finishes, even if an error happens.

6. How do you loop over each line in a file?

`Answer:` Open the file with `with open(...) as f:` and then use `for line in f:`.

---

### ✏️ Task: File Filter

Write code that prints only the lines in a file that contain the word `"error"`.

```python
with open("log.txt") as f:
    for line in f:
        if "error" in line.lower():
            print(line.rstrip())
```
