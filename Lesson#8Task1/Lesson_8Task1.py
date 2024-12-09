N = int(input("Введите число: "))
res = []
for i in range(N):
    number = int(input('Введите число: '))
    if (number <= 10**5 and number >= 1):
        res.append(number)
res.reverse()
print(res)