year=int(input("Введите год: "))
sum = 0

def numSum(num: int)-> int:
  s = 0
  string = ""
  for i in range(num+1):
    string += str(i)
  for item in string:
    s+=int(item)
  return s

if(year%4==0 and year%100!=0 or year%400==0):
  daysInMonth= [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
else: 
  daysInMonth= [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i in daysInMonth:
  sum+=numSum(i)

print(sum)