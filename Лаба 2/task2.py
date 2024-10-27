#vvod
salary = 5000  
spend = 6000  
months = 10 
increase = 1.03  
total_spend = 0

#solution
for _ in range(months): 
    total_spend += spend
    spend *= increase

money_capital = -int(salary * months - total_spend)

#vivod
print(months, money_capital)
