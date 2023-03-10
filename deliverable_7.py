# -*- coding: utf-8 -*-
"""Deliverable 7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jaS9BZNGzlkPfPsXIho3zQNDdORlOxEY
"""

import pandas as pd

n = int(input("Enter a non-negative integer number: ")) #asks user for their input

if n <= 0:
  print("Invalid input, please enter a non-negative integer number.")
else:
  even = []
  odd = []
  fibo = [0,1]

  for i in range(n):
    even.append(2*i)
    odd.append(2*i+1)
    if i > 1: fibo.append(fibo[i-2]+fibo[i-1])

data = {"Even": even,
        "Odd": odd,
        "Fibonacci": fibo}
df = pd.DataFrame(data)

df