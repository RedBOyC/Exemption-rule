def ER(a, b, m):
  if type(m)!=int:
    return "m is not an integer!"
  #ensure a and b are coprime
  smallest=min(a, b)
  divisor=[]
  for d in range(1, a+1):
    if a%d==0 and b%d==0:
      divisor.append(d)
  if len(divisor)>1:
    return "a and b are not coprime!"
  
  A=[]
  B=[]
  primes=[]
  for n in range(m+1):
    if n not in B:
      p=a*n + b 
      A.append(n)
      primes.append(p)
      for k in range(m+1):
        exempted=(p*k)+((p-b)//a)
        if exempted<=m:
          B.append(exempted)
        else:
          break
  return A, B, primes

#Tested on Google Colab:

%%timeit
A, B, primes=ER(2, 3, 1000)

#11.5 ms ± 2.68 ms per loop (mean ± std. dev. of 7 runs, 100 loops each)
