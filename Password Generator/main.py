import random

# possible characters lists
lowercase_characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

uppercase_characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G' ,'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+']

# print(lowercase_characters)
# print(uppercase_characters)
# print(numbers)
# print(special_characters)

pw = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
pw[0] = random.choice(lowercase_characters)
pw[1] = random.choice(lowercase_characters)
pw[2] = random.choice(uppercase_characters)
pw[3] = random.choice(numbers)
pw[4] = random.choice(lowercase_characters)
pw[5] = random.choice(uppercase_characters)
pw[6] = random.choice(uppercase_characters)
pw[7] = random.choice(special_characters)
pw[8] = random.choice(lowercase_characters)
pw[9] = random.choice(numbers)
pw[10] = random.choice(lowercase_characters)
pw[11] = random.choice(lowercase_characters)
pw[12] = random.choice(uppercase_characters)
pw[13] = random.choice(numbers)
pw[14] = random.choice(lowercase_characters)
pw[15] = random.choice(uppercase_characters)
pw[16] = random.choice(uppercase_characters)
pw[17] = random.choice(special_characters)
pw[18] = random.choice(lowercase_characters)
pw[19] = random.choice(numbers)
# print(pw)
pwS = ''.join(pw)
# print(pwS)

pwL = []
for i in range(10):
  charType = random.randint(1,4)
  if charType == 1:
    random_char = random.choice(lowercase_characters)
  elif charType == 2:
    random_char = random.choice(uppercase_characters)
  elif charType == 3:
    random_char = random.choice(numbers)
  else:
    special_characters = '!@#$%^&*()?'
    random_char = random.choice(special_characters)
  pwL.append(random_char)
print("Generated password list:", pwL)