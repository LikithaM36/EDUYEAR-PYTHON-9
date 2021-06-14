#occurrence of y's in given word'
print("This will print number of y's in a given word ")
st=str(input('Enter a word:'))
print("Number of y's:",st.count('y'))


#Printing even indexed characters in a given word
print("This will print all even indexed characters in given word")
st2=str(input('Enter a word:'))
ss = st2[2::2]
print("even indexed characters in",st2,"are:",ss)
#st='hello'

#swap case program
print('Swapcase Program')
st3=str("EdUyEaR")
print(st3)
sc=st3.swapcase()
print(sc)