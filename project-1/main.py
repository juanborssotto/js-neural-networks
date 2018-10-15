from random import uniform
from math import exp

x = 0.5
y = 0.6
team = 0

weightx0 = uniform(-1, 1)
weightx1 = uniform(-1, 1)
weighty0 = uniform(-1, 1)
weighty1 = uniform(-1, 1)

bias0 = uniform(-1, 1)
bias1 = uniform(-1, 1)

output0_margin = 0.05
output1_margin = 0.95

def calculate_output(x, y, weightx, weighty, bias):
  sum = (x * weightx + y * weighty - bias)
  return sigmoid(sum)

def sigmoid(number):
  try:
    ans = 1 / (1 + exp(-number))
  except OverflowError:
    ans = float('inf')
  return ans

def calculate_team(output0, output1):
  if(output0 < output0_margin):
    return 0
  elif(output1 > output1_margin):
    return 1
  return -1

def calculate_error(output0, output1, guessed_team, team):
  if guessed_team == 0 or (guessed_team == -1 and team == 0):
    error = team - output0
  elif guessed_team == 1 or (guessed_team == -1 and team == 1):
    error = team - output1
  return error

output0 = calculate_output(x, y, weightx0, weighty0, bias0)
output1 = calculate_output(x, y, weightx1, weighty1, bias1)
guessed_team = calculate_team(output0, output1)

iterations = 0
while team != guessed_team or team == -1:
  print(output0)
  error = calculate_error(output0, output1, guessed_team, team)
  weightx0+= error * x
  weightx1+= error * x
  weighty0+= error * y
  weighty1+= error * y
  output0 = calculate_output(x, y, weightx0, weighty0, bias0)
  output1 = calculate_output(x, y, weightx1, weighty1, bias1)
  guessed_team = calculate_team(output0, output1)
  iterations+= 1

print('Number of iterations %d', iterations)