# -*- coding: utf-8 -*-
"""Weekly_PayLK

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1EETvIdIhRDo5AAa-lNLFm9VZtJl8l6T0
"""

def get_input():
  wage = int(input("Please enter wage : $"))
  hours = int(input("Please enter hours worked :"))
  return wage, hours

def weekly_pay():
  weekly_pay = 0
  wage,hours = get_input()
  if hours > 40:
    weekly_pay = (wage*40) + (wage*(hours-40)*1.5)
  else:
    weekly_pay = wage*hours
  print("Weekly pay : $", weekly_pay)

weekly_pay()