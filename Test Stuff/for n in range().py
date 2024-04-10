for n in range(1,101):
 w=""
 if n%3==0:w+="Fizz"
 if n%5==0:w+="Buzz"
 elif n%3!=0:w=n
 print(w)


#More space efficient FizzBuzz implementation
""" 
for i in range(1,101):print("Fizz"*(i%3==0)+"Buzz"*(i%5==0)or i)
"""