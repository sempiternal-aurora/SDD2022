for n in range(1,101):
 w=""
 if n%3==0:w+="Fizz"
 if n%5==0:w+="Buzz"
 if n%5!=0 and n%3!=0:w=n
 print(w)