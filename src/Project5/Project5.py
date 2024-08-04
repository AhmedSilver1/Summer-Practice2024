grades = []


def printResult():

  print(grades)
  print(average(grades))
  print(max(grades))
  print(min(grades))


def addToList():
  i = input(int())
  while int(i) >= 0:
    grades.append(i)
    print("Enter another grade")
    i = input(int())


def max(list):
  max = 0
  for elemnent in list:
    if int(elemnent) > int(max):
      max = elemnent
  return max


def min(list):
  min = int(list[0])
  for elemnent in list:
    if int(elemnent) < int(min):
      min = elemnent
  return min


def average(list):
  sum = int(list[0])
  for element in list:
    sum += int(element)

  return sum / len(list)


print(
    "Hello user, please enter a number between 0 and 10 to add grades and enter -1 to stop"
)
addToList()
printResult()
