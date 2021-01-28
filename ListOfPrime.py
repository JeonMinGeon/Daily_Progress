##This code print the list of prime number
## between 2 and N(user's input)

n = int(input("Input N:"))
num_to_n = list(range(2,n+1))
list_of_prime=[]
while True:
  if len(num_to_n) ==0:
    break
  now = num_to_n[0]
  list_of_prime.append(now)
  for i in num_to_n:
    if i%now==0:
      num_to_n.remove(i)
print(list_of_prime)