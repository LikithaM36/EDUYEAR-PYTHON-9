#Type Conversions
a=3
print(type(a),a)#printing
#converting
b=(float(a))
print(type(b), b)
print(b)
print(3+b)
c=(str(a))
print(type(c), c)
print('hello', c)
d=bool(a)
print(type(d), d)
print(d)
e=0
f=print(bool(e))
print(type(f))

#formatting
name = 'Aparna'
age = 36
empoly = True
salary_package = 10.6
p='Hello! Is this {} and I am {} years old {} I am a empolyer and my package was {} lakhs per annum'.format(name,age,empoly,salary_package)
print(p)

intro = '''Hello all !
	The main moto of this meeting is get awarness on covid.
	Thankyou ! '''
print(intro)       
      

