i = []
print ('введите число 1')
i.append (int (input ('введите первое число:')))
i.append (int (input ('введите второе число')))
i.append (int (input ('введите третье число')))
print (i)
f = (sum(i))
if f > 100:
	print ('в яблочко')
elif f < 100:
	print ('не в яблочко')
else:
	print ('ну капец')		
print (f)