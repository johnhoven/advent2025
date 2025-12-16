import files

def processPart1(fileName):
  lines = files.getLines(fileName)
  result = 0
  items = []

  for line in lines:
    for item in line.split(','):
      item = item.replace("\n", "")
      if item != None and item != "":
        items.append(item)
  
  for item in items:
    (lower, higher) = item.split('-')
    lu = len(higher)
    m = lu % 2
    if m == 1:
      lu = lu - 1

    l = len(lower)
    m = l % 2
    if (lu < l):
      continue
    if m == 1:
      lower = str(lower).rjust(lu, "0")

    lowNum = int( lower[0: int(lu / 2)] )
    highNum = int (lower[int(lu / 2):])

    higherNum = float(higher)
    lowerNum = float(lower)
    lessThan = int(higher[0: int(lu/2)])
    if lessThan < lowNum:
      lessThan = lessThan * 10

    print ((item, lowNum, highNum, lessThan))

    while lowNum <= lessThan:

      target = float(str(lowNum) + str(lowNum))
      if target <= higherNum and target >= lowerNum:
        print(target)
        result = result + target

      lowNum = lowNum + 1
    

  print (result)
  return result


def repeat(base, times):
  result = ""
  for i in range(times):
    result = result + base
  return result

def part2TestNumber(base, substr, repeats, lowerBounds, upperBounds,
    maxLength, dict):
  
  if maxLength % repeats != 0:
    return 0

  sub = str(base)[0:substr]
  targetNum = float(repeat(sub, repeats))
  if targetNum >= lowerBounds and targetNum <= upperBounds and not (targetNum in dict) and targetNum > 10:
    dict[targetNum] = True
    print(targetNum)
    return 0
  return 0

def part2SumKeys(dict):
  result = 0
  for k,v  in dict.items():
    result += k
  return result

def processPart2(fileName):
  lines = files.getLines(fileName)
  result = 0
  items = []

  for line in lines:
    for item in line.split(','):
      item = item.replace("\n", "")
      if item != None and item != "":
        items.append(item)
  
  found = {}

  for item in items:
    (lower, higher) = item.split('-')
    lu = len(higher)
    luOriginal = lu
    m = lu % 2
    if m == 1:
      lu = lu - 1


    l = len(lower)
    m = l % 2
    #if (lu < l):
     # continue
    if m == 1:
      lower = str(lower).rjust(lu, "0")

    lowNum = int( lower[0: int(lu / 2)] )
    highNum = int (lower[int(lu / 2):])

    higherNum = float(higher)
    lowerNum = float(lower)
    lessThan = int(higher[0: int(lu/2)])
    if lessThan < lowNum:
      lessThan = int(higher[0: int(lu/2) + 1])

    
    print ((item, lowNum, highNum, lessThan, int(higher[0: int(lu/2)]), lower))

    
    # Iterate from from half the left string to half the right string, adjusting for length differences
    # 824824821-824824827
    # would iterate from: 8248 to 8248
    # test each possible pattern with support up to 10 digits in length
    # If lower and upper bound have different lengths, test patterns for both lengths
    # digit 1, length times; first 2 digits X times, first 3 digits Y times, first 4 digits Z times, and first 5 digits 2 times, such that the resulting length falls in the number range
    # Example 2: 998-1012
    # Iterates from 9 to 10
    # From 9, tests 9 at length 3 and 99 at length 4
    # Iterates to 10 and tests 1 at length 3 (out of range) and 10 at length 4 (in range)

    while lowNum <= lessThan:

      lu = len(str(lowNum))
      if lu < l:
        lu = l

      result += part2TestNumber(lowNum, 1, lu, lowerNum, higherNum, lu, found )
      if lu == 10:
        result += part2TestNumber(lowNum, 2, 5, lowerNum, higherNum, lu, found )
        result += part2TestNumber(lowNum, 5, 2, lowerNum, higherNum, lu, found )
      if lu == 8:
        result += part2TestNumber(lowNum, 2, 4, lowerNum, higherNum, lu, found )
        result += part2TestNumber(lowNum, 4, 2, lowerNum, higherNum, lu, found )
      if lu == 6:
        result += part2TestNumber(lowNum, 2, 3, lowerNum, higherNum, lu, found )
        result += part2TestNumber(lowNum, 3, 2, lowerNum, higherNum, lu, found )
      if lu == 4:
        result += part2TestNumber(lowNum, 2, 2, lowerNum, higherNum, lu , found)
      if lu == 9:
        result += part2TestNumber(lowNum, 3, 3, lowerNum, higherNum, lu , found)
      
      if lu != luOriginal:
        lu = luOriginal
        result += part2TestNumber(lowNum, 1, lu, lowerNum, higherNum, lu, found )
        if lu == 10:
          result += part2TestNumber(lowNum, 2, 5, lowerNum, higherNum, lu, found )
          result += part2TestNumber(lowNum, 5, 2, lowerNum, higherNum, lu, found )
        if lu == 8:
          result += part2TestNumber(lowNum, 2, 4, lowerNum, higherNum, lu, found )
          result += part2TestNumber(lowNum, 4, 2, lowerNum, higherNum, lu, found )
        if lu == 6:
          result += part2TestNumber(lowNum, 2, 3, lowerNum, higherNum, lu, found )
          result += part2TestNumber(lowNum, 3, 2, lowerNum, higherNum, lu, found )
        if lu == 4:
          result += part2TestNumber(lowNum, 2, 2, lowerNum, higherNum, lu , found)
        if lu == 9:
          result += part2TestNumber(lowNum, 3, 3, lowerNum, higherNum, lu , found)


      lowNum = lowNum + 1
  
  result = part2SumKeys(found)

  print (result)
  return result

