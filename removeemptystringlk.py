# -*- coding: utf-8 -*-
"""RemoveEmptyStringLK

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1YDsuJ7D0KRvhkL10_BJUnHNFfoP59nRz
"""

def new_list(list):
  new_list = []
  for i in list:
    j = i.strip()
    if not j == '':
      new_list.append(i)
    else:
      new_list = new_list
  return new_list


list1 = ['', '  a  ', 'b', ' ', 'c  ']
list2 = ['d', '    ', ' efg', 'h i']
list3 = ['j k', 'lm', '        ', 'n o', '']

#new_list(list1)
#new_list(list2)
new_list(list3)