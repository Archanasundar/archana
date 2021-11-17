'''
given input "WORD" and print the output as shown bellow

DWOR
RDWO
ORDW
WORD

'''


string = "WORD"
for i in range(len(string)):
  s = string[-1]
  string = s + string[0 : len(string) - 1]
  print(string)
