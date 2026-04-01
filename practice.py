# task1
n = int(input())

for i in range(1, n + 1):
    if (i % 3 == 0 or i % 5 == 0) and not (i % 3 == 0 and i % 5 == 0):
        print(i, end=" ")

# task2
num = input()
n = len(num)

sum = 0
for digit in num:
    sum += int(digit) ** n

if sum == int(num):
    print(True)
else:
    print(False)

# task3
s = input()

count = 1
result = ""

for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        count += 1
    else:
        result += s[i] + str(count)
        count = 1

result += s[-1] + str(count)

print(result)

# task4
s = input()

s = s.lower()
s = s.replace(" ", "")

if s == s[::-1]:
    print(True)
else:
    print(False)

# task5

s = input()
k = int(input())

k = k % len(s)

result = s[-k:] + s[:-k]

print(result)