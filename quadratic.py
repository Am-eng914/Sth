import math

def addLines():
	print('-' * 63)

def checkQuit(num, running):
	currentState = running
	
	if num == 'done':
		currentState = False
	
	return currentState
	

def returnLoop():
	addLines()
	return quadraticEq()


def quadraticEq():
	running = True
	negPosMsgs = [' ', ' + ', ' + ']
	neg = '-'
	negVal1 = 0
	negVal2 = 0
	strSign1 = ' '
	strSign2 = ' '
	
	num = []
	for i in range(0, 1001):
		num.append(i)
	
	numerator1 = [1] * len(num)
	numerator2 = [1] * len(num)
	denominator = [1] * len(num)
	divisibles = []
	isNotFloat = None
	
	try:
		while running:
			a = str(input('Enter a: '))
			running = checkQuit(a, running)
			if not running:
				break
				
			b = str(input('Enter b: '))
			running = checkQuit(b, running)
			if not running:
				break
				
			c = str(input('Enter c: '))
			running = checkQuit(c, running)
			if not running:
				break
			
			val_a = float(a)
			val_b = float(b)
			val_c = float(c)
			
			D = val_b ** 2 - 4 * val_a * val_c
			sqrtOfD = math.sqrt(D)
			
			val1 = (- val_b + math.sqrt(D))/(2 * val_a)
			val2 = (- val_b - math.sqrt(D))/(2 * val_a)
			if val1 == int(val1):
			    val1 = int(val1)
			if val2 == int(val2):
			    val2 = int(val2)
			
			if val1 > 0:
			    negVal1 = str(val1)
			    strSign1 = ' - '
			if val2 > 0:
			    negVal2 = str(val2)
			    strSign2 = ' - '
			if val1 < 0:
			    negVal1 = str(val1)
			    strSign1 = ' + '
			if val2 < 0:
			    negVal2 = str(val2)
			    strSign2 = ' + '
			if neg in negVal1:
			    negVal1 = negVal1.replace(neg, '')
			if neg in negVal2:
			    negVal2 = negVal2.replace(neg, '')
			    
			if sqrtOfD != int(sqrtOfD):
				isNotFloat = False
			else:
				isNotFloat = True
			
			for n in range(1, 1001):
				numerator1[n] = ((- val_b + math.sqrt(D))/num[n])
				numerator2[n] = ((- val_b - math.sqrt(D))/num[n])
				denominator[n] = ((2 * val_a)/num[n])
				
				if numerator1[n] == int((- val_b + math.sqrt(D))/num[n]):
					numerator1[n] = int(numerator1[n])
				if numerator2[n] == int((- val_b - math.sqrt(D))/num[n]):
					numerator2[n] = int(numerator2[n])
				if denominator[n] == int((2 * val_a)/num[n]):
					denominator[n] = int(denominator[n])
				
				if (- val_b + math.sqrt(D))/n == int((- val_b + math.sqrt(D))/n) and (- val_b - math.sqrt(D))/n == int((- val_b - math.sqrt(D))/n) and (2 * val_a)/n == int((2 * val_a)/n):
					divisibles.append(n)
					
			if val_a < 0:
				negPosMsgs[0] = ' - '
			if val_b < 0:
				negPosMsgs[1] = ' - '
			if val_c < 0:
				negPosMsgs[2] = ' - '
			
			if neg in a:
				a = a.replace(neg, '')
			if neg in b:
				b = b.replace(neg, '')
			if neg in c:
				c = c.replace(neg, '')
				
			print('The quadratic equation is: ' + negPosMsgs[0] + a + 'x²' + negPosMsgs[1] + b + 'x' + negPosMsgs[2] + c + ' = 0')
			
			if negPosMsgs[0] == ' ':
			     print(a + 'x²'  + strSign1 + str(negVal1)  + 'x' + strSign2 + str(negVal2) + 'x' + negPosMsgs[2] + c +' = 0')
			else:
			     print(negPosMsgs[0] + a + 'x²'  + strSign1 + str(negVal1)  + 'x' + strSign2 + str(negVal2) + 'x' + negPosMsgs[2] + c +' = 0')
			
			
			if isNotFloat:
				if denominator[max(divisibles)] == 1:
					print('value1 = ' + str(numerator1[max(divisibles)]))
				if denominator[max(divisibles)] == 1:
					print('value2 = ' + str(numerator2[max(divisibles)]))
				
				if denominator[max(divisibles)] != 1:
					print('value1 = ' + str(numerator1[max(divisibles)]) + '/' + str(denominator[max(divisibles)]))
				if denominator[max(divisibles)] != 1:
					print('value2 = ' + str(numerator2[max(divisibles)]) + '/' + str(denominator[max(divisibles)]))
			
			print('The values are', val1, 'and', val2)
			
			returnLoop()
	

	except:
		mathError = False
		blankSpaceLeft = False
		ErrorMsg = ''
		allNum = []
		blank = []
		tab = ''
		
		for all in range(-100001, 100001):
			allNum.append(all)
			
		for i in range(10000):
			blank.append(tab)
			tab += ' '
			
		for i in range(len(allNum)):
			if a == str(allNum[i]) or b == str(allNum[i]) or c == str(allNum[i]):
				mathError = True
				ErrorMsg = ' >>> Math Error'
		
		for i in range(len(blank)):
			if a == blank[i] or b == blank[i] or c == blank[i]:
				blankSpaceLeft = True
				ErrorMsg = ' >>> Cannot leave a, b or c blank'
			
		if not mathError and not blankSpaceLeft:
			ErrorMsg = ' >>> Must be a number'
		
		print(newLine + 'Error' + ErrorMsg)
		
		returnLoop()
	

newLine = '\n'

print('A Quadratic Calculator')
addLines()
print(newLine + "NOTE: Enter 'done' to exit the program."+ newLine)
print('A quadratic equation is given in the expression:' + newLine + ' ax² + bx + c = 0' + newLine)

addLines()
quadraticEq()