import files

def processPart1(fileName):
  lines = files.getLinesAsCharArrays(fileName)
  result = 0
  height = len(lines)
  max = len(lines[0])
  start = lines[0].index("S")
  
  indexes = {}
  indexes[start] = True

  for i in range(1, height):
    
    line = lines[i]
    newIndex = {}

    for k,v in indexes.items():
      if line[k] == '^':
        result = result + 1
        print(("^", i, k))
        if k > 0:
          newIndex[k - 1] = True
        if k + 1 < max:
          newIndex[k + 1] = True
      else:
        newIndex[k] = True
    indexes = newIndex
  
  print(result)
  return result

def processPart2(fileName):
  lines = files.getLinesAsCharArrays(fileName)
  height = len(lines)
  max = len(lines[0])
  start = lines[0].index("S")
  
  indexes = {}
  indexes[start] = 1

  for i in range(1, height):
    
    line = lines[i]
    newIndex = {}

    for k,v in indexes.items():
      if line[k] == '^':
        #result = result + 1
        print(("^", i, k, v))
        if k > 0:
          newIndex[k - 1] = newIndex.get(k - 1, 0) + v 
        if k + 1 < max:
          newIndex[k + 1] = newIndex.get(k + 1, 0) + v
      else:
        newIndex[k] = newIndex.get(k, 0) + v
    indexes = newIndex
  
  result = 0
  for k, v in newIndex.items():
    result += v


  print(result)
  return result