# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе
# они сделали S журавликов. Сколько журавликов сделал каждый
# ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?

s = int (input('Введите количество сделанных журавликов: '))
if s%6 == 0:
    a = s/6
    x = s/6*4
    print(f'Петя и Сережа сделали по {a} журавликов, а Катя сделала {x}')
else:
    print('Такое количество журавликов Петя, Сережа и Катя сделать не могли')