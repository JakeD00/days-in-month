import os

def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(selected_year, selected_month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if selected_year < 1:
      return "That year doesn't exist!"
  if selected_month < 1 or selected_month > 12:
      return "You chose month that doesn't exist!"
  if is_leap(selected_year) and selected_month == 2:
      return month_days[selected_month-1]+1
  return month_days[selected_month-1]
  
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
os.system('pause')






