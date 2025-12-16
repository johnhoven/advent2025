import files

def isAccessible(lines, i, j):
  
  ct = 0
  lenI = len(lines) - 1
  lenJ = len(lines[0]) - 1

  if lines[i][j] == ".":
    return False

  # line up
  ct += 1 if j > 0 and i > 0 and lines[i - 1][j - 1] == '@' else 0
  ct += 1 if i > 0 and lines[i - 1][j] == '@' else 0
  ct += 1 if i > 0 and j < lenJ and lines[i - 1][j + 1] == '@' else 0

  # same line, left right
  ct += 1 if j > 0  and lines[i][j - 1] == '@' else 0
  ct += 1 if j < lenJ and lines[i][j + 1] == '@' else 0

  #line down
  ct += 1 if i < lenI and j > 0 and lines[i + 1][j - 1] == '@' else 0
  ct += 1 if i < lenI and lines[i + 1][j] == '@' else 0
  ct += 1 if i < lenI and j < lenJ and lines[i + 1][j + 1] == '@' else 0

  if ct > 3:
    return False
  return True

def processPart1(fileName):
  lines = files.getLines(fileName)
  result = 0
  
  for i in range(0, len(lines)):
    for j in range(0, len(lines[i])):
      if isAccessible(lines, i, j):
        result = result + 1

  
  print(result)
  return result

def processPart2(fileName):
  lines = files.getLinesAsCharArrays(fileName)
  result = 0
  
  resultLast = 0
  while (resultLast > 0 or result == 0):
    resultLast = result
    for i in range(0, len(lines)):
        for j in range(0, len(lines[i])):
          if isAccessible(lines, i, j):
            result = result + 1
            lines[i][j] = "."
    resultLast = result - resultLast
        

  
  print(result)
  return result




