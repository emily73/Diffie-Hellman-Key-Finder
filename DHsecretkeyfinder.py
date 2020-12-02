def Input_Numbers():
  g = int(input("Enter the Generator Number: "))
  n = int(input("Enter the Prime Number:"))
  priv_a = int(input("Enter the Alice's private key: "))
  priv_b = int(input("Enter the Bob's private key: "))
  pub_a = g**priv_a % n
  pub_b = g**priv_b % n
  k = pow(g,priv_a*priv_b,n)
  print("------------------------------------")
  print("Alice's public key is: ",pub_a)
  print("Bob's public key is: ", pub_b)
  print("The Secret Key is: ",k)

InputNumbers()
