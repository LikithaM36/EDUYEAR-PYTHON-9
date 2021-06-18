#factorial program
num=1
value=int(input('Enter a value:'))
temp=value
while value!=0:
	num=value*num
	value-=1
print('The factorial of {} is {}'.format(temp,num))

#divisible program
num=1
n=int(input('Enter to number:'))
m=int(input('Enter from number:'))
for i in range(n,m):
	if i%5==0 and i%7==0:
		print(i)


st = 'python language is best programming language'

for i in range(len(st)):
	end_val = '-'
	if st[i] == ' ':
		end_val = ''
	if i == len(st)-1:
		end_val = ''
	elif st[i+1] == ' ':
		end_val = ''
	if i%2 == 0:
		print(st[i].upper(), end=end_val)
	else:
		print(st[i].lower(), end=end_val)
	