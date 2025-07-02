from sympy import isprime

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
  for n in range(1, m+1):
    if n not in B:
        p=abs(a*(-1*n) + b)
        A.append(-1*n)
        primes.append(p)
        for k in range(m+1):
            exempted=(p*k) + ((-1*p -b)//a)   
            if exempted<=m:
                B.append(exempted)
            else:
                break
  return A, B, primes

def evaluate_ER(a, b, m):
    A, B, sieve_primes = ER(a, b, m)

    # Generate all actual primes in the AP an + b for n in [0, m]
    actual_primes = []
    for n in range(m+1):
        val = a*n + b
        if isprime(val):
            actual_primes.append(val)
    
    sieve_primes_set = set(sieve_primes)
    actual_primes_set = set(actual_primes)

    true_positives = sieve_primes_set & actual_primes_set
    false_positives = sieve_primes_set - actual_primes_set
    false_negatives = actual_primes_set - sieve_primes_set

    TP = len(true_positives)
    FP = len(false_positives)
    FN = len(false_negatives)

    precision = TP / (TP + FP) if (TP + FP) > 0 else 0
    recall = TP / (TP + FN) if (TP + FN) > 0 else 0
    f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

    print(f"Evaluation of ER for a={a}, b={b}, m={m}")
    print(f"Total predicted primes: {len(sieve_primes)}")
    print(f"True positives: {TP}")
    print(f"False positives: {FP}")
    print(f"False negatives: {FN}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall:    {recall:.4f}")
    print(f"F1 Score:  {f1:.4f}")
    
    return {
        'a': a, 'b': b, 'm': m, 'TP': TP, 'FP': FP, 'FN': FN,
        'Precision': precision, 'Recall': recall, 'F1': f1
    }

result = evaluate_ER(2, 3, 10000)
print(result)
