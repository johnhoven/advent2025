import files

def checkRanges(num, ranges):
  for r in ranges:
    if num >= r[0] and num <= r[1]:
      return True
  return False

def processPart1(fileName):
  lines = files.getLines(fileName)
  result = 0
  
  sawNewLine = False
  linesP1 = []
  #linesP2 = []

  for line in lines:
    if line == "":
      sawNewLine = True
    elif not sawNewLine:
      (lower, upper) = line.split('-')
      linesP1.append((float(lower), float(upper)))
    else:
      if checkRanges(float(line), linesP1):
        result = result + 1
      #linesP2.append(float(line))      

  
  
  print(result)
  return result

def compressRanges(ranges):
  i = 0
  while i < len(ranges):
    r1 = ranges[i]
    lower1 = r1[0]
    upper1 = r1[1]
    if lower1 == -1:
      i = i + 1
      continue

    for j in range(i + 1, len(ranges)):
      r2 = ranges[j]
      lower2 = r2[0]
      upper2 = r2[1]
      if lower2 == -1:
        continue

      if lower2 <=  upper1  and upper2 >= lower1:
        print(lower1, upper1, lower2, upper2)
        if lower2 < lower1:
          ranges.append((lower2, lower1 - 1))
          print('lower added', lower2, lower1 - 1)
        if upper2 > upper1:
          ranges.append((upper1 + 1, upper2))
          print('higher added', upper1 + 1, upper2)
        ranges[j] = (-1, -1)
    
    i = i + 1


def countCompressedRanges(ranges):
  result = 0
  for r1 in ranges:
    lower1 = r1[0]
    upper1 = r1[1]
    if lower1 == -1:
      continue;

    result += upper1 - lower1 + 1
  return result
    

def processPart2(fileName):
  lines = files.getLines(fileName)
  result = 0
  
  linesP1 = []

  for line in lines:
    if line == "":
      break
    else:
      (lower, upper) = line.split('-')
      linesP1.append((float(lower), float(upper)))
    
  compressRanges(linesP1)

  result = countCompressedRanges(linesP1)
  
  
  print(result)
  return result

