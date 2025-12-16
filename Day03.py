import files

def part1FindJoltage(items):

  n = items[0]
  index = 0
  for i in range(1, len(items) - 1):
    if items[i] > n:
      n = items[i]
      index = i
  
  print((items, n, index))

  o = items[index + 1]
  index2 = index + 1
  if index2 + 1 < len(items):
    for i in range(index2 + 1, len(items)):
      if items[i] > o:
        o = items[i]
        index2 = i

  return int( n + o )

def processPart1(fileName):
  lines = files.getLines(fileName)
  result = 0
  items = []

  for line in lines:
    joltage = part1FindJoltage(list(line))
    print(joltage)
    result += joltage
  
  print(result)
  return result

def getLargestUpTo(items, startIndex, upToIndex):
  # At each index we have one of two options
  # Add our joltage or skip
  
  m = items[startIndex]
  mi = startIndex
  for i in range(startIndex, upToIndex):
    if (items[i] > m):
      m = items[i]
      mi = i
  
  return mi

    

def part2FindJoltage(items):

  results = []
  targetLength = 12
  lastIndex = 0
  running = 0
  while targetLength > 0:
    lastIndex = getLargestUpTo(items, lastIndex, len(items) - targetLength + 1 )
    results.append(lastIndex)
    targetLength = targetLength - 1
    running = running * 10 + int(items[lastIndex])
    lastIndex = lastIndex + 1

  print (running)
  return running

def processPart2(fileName):
  lines = files.getLines(fileName)
  result = 0
  items = []

  for line in lines:
    joltage = part2FindJoltage(list(line))
    result += joltage
  
  print(result)
  return result



