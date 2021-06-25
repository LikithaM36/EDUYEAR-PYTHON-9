#pattern programs
#Enter the no.of rows:5
#*****
#*****
#*****
#*****
#*****

num=int(input('Enter the no.of rows:'))
for i in range(num):
	for j in range(num):
		print('*',end='')
	print()


#Enter the no.of rows:5
#*****
#****
#***
#**
#*

num=int(input('Enter the no.of rows:'))
for i in range(num):
	for j in range(num):
		if(i+j<=num-1):
			print('*',end='')
	print()

#Enter the no.of rows:5
#*****
# ****
#  ***
#   **
#    *	
	
num=int(input('Enter the no.of rows:'))
for i in range(num):
	for j in range(num):
		if(i<=j):
			print('*',end='')
		else:
			print(end=' ')
	print()

#Enter the no.of rows:5
#    *
#   **
#  ***
# ****
#*****

	
num=int(input('Enter the no.of rows:'))
for i in range(num):
	for j in range(num):
		if(i+j>=num-1):
			print('*',end='')
		else:
			print(end=' ')
	print()
	
#Enter the no.of rows:5
#*
#**
#***
#****
#*****	
	
num=int(input('Enter the no.of rows:'))
for i in range(num):
	for j in range(num):
		if(i>=j):
			print('*',end='')
	print()
#Enter the no.of rows:4
#1 2 3 4
#1 2 3 4
#1 2 3 4
#1 2 3 4

num=int(input('Enter the no.of rows:'))
for i in range(num):
	for j in range(num):
		print(j+1,end=' ')
	print()