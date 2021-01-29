# BAEKJOON problem no.2607
# Find the number of Similar Word
# n: Number of Words
# Code a program that find the number of similar word of [First Word of User's input] from [Rest of User's Input]
# You can only change one word. [DOG -> GO'O'D, aab -> aab'c', hello -> hell'', hall -> hal'o']
# Order of the alphabets are not sensitive([ex]: abcd == dcab)

n = int(input())
words=[]
word_nums=[]
answer=0
answers=[]
for a in range(n):
  words.append(input())
base_word = words[0]
base_list = list(set(base_word))
base_list.sort()
for b in base_list:
  word_nums.append(base_word.count(b))
for i in words[1:]:
  cont_ = 0
  changes = 0
  if len(i)>len(base_word)+1 or len(i)<len(base_word)-1:
    continue
  for ii in range(len(base_list)):
    if abs(i.count(base_list[ii]) - word_nums[ii])>1:
      cont_ = 1
      break
    elif abs(i.count(base_list[ii]) - word_nums[ii]):
      changes += 1
  changes -= 1
  if cont_ == 1:
    cont_ = 0
    continue

  diff_word = list(set(i) - set(base_word))
  if len(diff_word)>1:
    continue
  elif len(diff_word):
    if i.count(diff_word[0])>1:
      continue
    changes += 1
  if changes >1:
    continue
  answers.append(i)
  answer+=1
print(answer)
print(answers)