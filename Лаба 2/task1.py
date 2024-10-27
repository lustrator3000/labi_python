#vvod
money_capital = 20000
salary = 5000 
spend = 6000
increase = 0.05
count = 0
while money_capital + salary - spend >= 0:
    money_capital += salary - spend
    spend += spend * increase
    count += 1
    
#vivod
print(count)
