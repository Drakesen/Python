print("Hello my friend!")

# Треугольник Паскаля
N = 7
P = []

for i in range(N):
    row = [1] * (i+1)
    for j in range(i+1):
        if j != 0 and j != i:
            row[j] = P[i-1][j-1] + P[i-1][j]
    P.append(row)
for r in P:
    print(r)

# Код для авторизации
pass_true = "password"
ps = ""
while ps != pass_true:
    ps = input("Введите пароль")
print("Вход в систему")