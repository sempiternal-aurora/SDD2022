for l in range(1,10):
 for n in range(1,2*l):
  s=abs(9-n)*" "
  for i in range(1,2*l):s+=str(-abs(i-l)+n)
  print(s)
 print()