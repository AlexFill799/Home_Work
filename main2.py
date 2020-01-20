i = []
print ('введите число 1')
i.append (int (input ('введите первое число:')))
i.append (int (input ('введите второе число')))
i.append (int (input ('введите третье число')))
print (i)
print (type (i))
f = 0
for e in i:
	f += e
print (f)
if f > 100:
	print ('в яблочко')
elif f < 100:
	print ('не в яблочко')
else:
	print ('ну капец')		