
limit = int(input("Enter the limit of fibonacci numbers to generate :"))
a = 1
b = 1
total = 0
fibo_list = [a]
while b < limit:
    fibo_list.append(b)
    total = a + b
    a = b
    b = total
      
print("From 1 to {} fibonacci numbers are :".format(limit), (fibo_list))