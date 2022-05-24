def max():
  a = int(input('Введите первое число: '))
  b = int(input('Введите второе число: '))
  max = (a + b + abs(a - b)) // 2
  return max

max = max()
c = int(input('Введите третье число: '))

if c >= max:
  print('Наибольшее число:', c)
else:
  print('Наибольшее число:', max)