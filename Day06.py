import files

def processPart1(fileName):
  lines = files.getLinesSplit(fileName)
  result = 0
  width = len(lines[0])
  height = len(lines)

  for i in range(0, width):
    operator = lines[height - 1][i]
    total = int(lines[0][i])

    for j in range(1, height - 1):
      if (operator == "+"):
        total = total + int(lines[j][i])
      if (operator == "*"):
        total = total * int(lines[j][i])

    result += total
    print (total)

  
  
  
  
  
  print(result)
  return result

def computerNumber(numbers, operator):
  print((numbers, operator))
  if len(numbers) == 0:
    return 0
  total = numbers[0]
  for n in range(1, len(numbers)):
    if (operator == "+"):
      total = total + numbers[n]
    if (operator == "*"):
      total = total * numbers[n]

  print (total)
  return total

def processPart2(fileName):
  # Can't split
  lines = files.getLines(fileName)
  result = 0
  width = len(lines[0])
  height = len(lines)
  lastOperator = ""
  numbers = []

  for i in range(0, width):
    operator = lines[height - 1][i]

    if (operator == " "):
      None
    else:
      result += computerNumber(numbers, lastOperator)
      lastOperator = operator
      numbers = []

    number = ""
    for j in range(0, height - 1):
      c = lines[j][i]
      if (c != " "):
        number = number + c

    if number != "":
      numbers.append(float(number))

  result += computerNumber(numbers, lastOperator)
  print(result)
  return result