from math import ceil as ceiling
import sys

def reHeap(aray):
  curr_ind = len(aray)-1
  parent_ind = ceiling(curr_ind/2) - 1
  while True:
    if curr_ind < 1:
      break
    if aray[parent_ind] <= aray[curr_ind]:
      curr_ind = parent_ind
    elif aray[parent_ind] > aray[curr_ind]:
      tmp=aray[parent_ind]
      aray[parent_ind] = aray[curr_ind]
      aray[curr_ind] = tmp
      curr_ind = parent_ind
    parent_ind = ceiling(curr_ind/2) - 1
  return aray

def deHeap(aray):
  limit_ind = len(aray)-1
  fin_ind = 0
  curr_ind = 0
  while True:
    childs = (curr_ind+1)*2
    if childs > limit_ind:
      if childs-1 > limit_ind:
        break
      elif aray[childs-1]<aray[curr_ind]:
        tmp = aray[childs-1]
        aray[childs-1] = aray[curr_ind]
        aray[curr_ind] = tmp
        break
      else:
        break
    elif aray[childs-1]<aray[childs]:
      if aray[childs-1]<aray[curr_ind]:
        tmp = aray[childs-1]
        aray[childs-1] = aray[curr_ind]
        aray[curr_ind] = tmp
        curr_ind = childs-1
      else:
        break
    else:
      if aray[childs] < aray[curr_ind]:
        tmp = aray[childs]
        aray[childs] = aray[curr_ind]
        aray[curr_ind] = tmp
        curr_ind = childs
      else:
        break
  return aray


answer = []
ans_arr = []
heappie = int(input())
for i in range(heappie):
  apnd = int(input())
  if not apnd:
    if answer == []:
      ans_arr.append(0)
    else:
      ans_arr.append(answer[0])
      if len(answer) == 1:
        answer = []
        continue
      else:
        answer = answer[-1:] + answer[1:-1]
      answer = deHeap(answer)

  else:
    answer.append(apnd)
    answer = reHeap(answer)
    
for i in ans_arr:
  print(i)