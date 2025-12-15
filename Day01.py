import files

def processPart1(fileName):
  lines = files.getLines(fileName)

  current = 50
  result = 0

  for line in lines:
    current = turnPart1(current, line)
    if current == 0:
      result = result + 1

  return result



def turnPart1(current, line):
  
  dir = line[0:1]
  num = int(line[1:])

  if dir == 'L':
    num = num * -1

  current = current + num

  while current < 0:
    current = current + 100

  while current > 99:
    current = current - 100

  return current;

def processPart2(fileName):
  lines = files.getLines(fileName)

  current = 50
  result = 0

  currentb = 50
  resultb = 0

  for line in lines:

    pre = current

    (current, subresult) = turnPart2(current, line)
    result = result + subresult

    (currentb, subresultb) = turnPart2b(currentb, line)
    resultb = resultb + subresultb

    if result != resultb:
      print (pre, line, current, result, currentb, resultb)



  return (result, resultb)

def turnPart2(current, line):
  
  dir = line[0:1]
  num = int(line[1:])

  if dir == 'L':
    num = num * -1
    if current == 0:
      num = num + 1
      current = 99

  #wasZero = current == 0
  current = current + num
  subResult = 0

  while current < 0:

    ##if wasZero:
      ##wasZero = False
      ##subResult = subResult - 1

    current = current + 100
    subResult = subResult + 1

  while current > 99:
    current = current - 100
    subResult = subResult + 1

  if current == 0 and dir == 'L':
    subResult = subResult + 1

  return (current, subResult)

def turnPart2b(current, line):
  
  dir = line[0:1]
  num = int(line[1:])

  result = 0

  if dir == 'L':
    while num > 0:
      current = current - 1
      if current == 0:
        result = result + 1
      elif current == -1:
        current = 99
      num = num - 1      
  else:
    while num > 0:
      current = current + 1
      if current == 100:
        current = 0
      if current == 0:
        result = result + 1
      
      num = num - 1

  
  return (current, result)