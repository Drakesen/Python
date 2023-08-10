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

#Вложенные циклы
A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
for i in range(len(A)):
    for j in range(i+1, len(A)):
        A[i][j], A[j][i] = A[j][i], A[i][j]

for r in A:
    for x in r:
        print(x, end='\t')
    print()

# Код для авторизации
pass_true = "password"
ps = ""
while ps != pass_true:
    ps = input("Введите пароль")
print("Вход в систему")