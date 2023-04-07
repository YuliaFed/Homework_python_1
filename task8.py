# Задача 8: Требуется определить, можно ли от шоколадки размером n
# × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no

m = int (input('Введите размер шоколадки m: '))
n = int (input('Введите размер шоколадки n: '))
k = int (input('сколько долек вы хотите отломить: '))

if (k%m==0 and k%m<=n) or (k%n==0 and k%n<=m):
    print(f"Yes: Вы можете отломить {k} долек от шоколадки {m} x {n} с одним разломом по прямой")
else:
    print(f"NO: Вы НЕ можете отломить {k} долек от шоколадки {m} x {n} с одним разломом по прямой")