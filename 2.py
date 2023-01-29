year=int(input("Введите год: "))
sum = 0


def numSum(num: int)-> int:
  s = 0
  for item in str(num):
    s+=int(item)
  return s
 
if(year%4==0 and (year%100!=0 or year%400==0)):
  visocosny = True
else: 
  visocosny = False

for i in range(1,12):
  if(i == 2):
    if(visocosny):
      for j in range(1, 29):
        sum += numSum(j)
    else:
      for j in range(1, 28):
        sum += numSum(j)
  if(i % 2 != 0):
    for j in range(1, 31):
      sum += numSum(j)
  elif(i % 2 == 0):
    for j in range(1, 30):
      sum += numSum(j)
    
print(sum)