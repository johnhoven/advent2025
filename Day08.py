import files
import math

class Coordinate:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.circuitNumber = -1
    def print(self):
        return f"{self.x},{self.y},{self.z}"
    
    def calculate(self, coordinates):
       self.calculations = []
       for c in coordinates:
          if c == self:
             self.calculations.append(-1)
          else:
             dx = self.x - c.x
             dy = self.y - c.y
             dz = self.z - c.z
             dist = math.sqrt( dx * dx + dy * dy + dz * dz)
             self.calculations(dist)

def updateCircuits(circutManager, c1, c2, certNum):
   newCircuit = []
   if c1.circuitNumber >= 0:
      
      if c2.circuitNumber == c1.circuitNumber:
         return 0

      old = c1.circuitNumber
      for c in circutManager[c1.circuitNumber]:
         c.circuitNumber = certNum
         newCircuit.append(c)
      del circutManager[old]
   else:
      newCircuit.append(c1)
      c1.circuitNumber = certNum

   if c2.circuitNumber >= 0:
      old = c2.circuitNumber
      for c in circutManager[c2.circuitNumber]:
         c.circuitNumber = certNum
         newCircuit.append(c)
      del circutManager[old]
   else:
      newCircuit.append(c2)
      c2.circuitNumber = certNum
   
   circutManager[certNum] = newCircuit
   return len(newCircuit)
    

def processPart1(fileName, connections):
  lines = files.getLinesSplit(fileName, ",")
  coords = []

  calcResults = {}

  for line in lines:
    coords.append(Coordinate(int(line[0]), int(line[1]), int(line[2])))
  
  for i in range(0, len(coords)):
    c = coords[i]
    for j in range(i + 1, len(coords)):
      c2 = coords[j]

      dx = c2.x - c.x
      dy = c2.y - c.y
      dz = c2.z - c.z
      dist = math.sqrt( dx * dx + dy * dy + dz * dz)

      dict = calcResults.get(dist, [])
      dict.append((c, c2))
      calcResults[dist] = dict
  
  sortedKeys = list(calcResults.keys())
  sortedKeys.sort()
  circuitManager = {}
  certNum = 0
  for key in sortedKeys:
     dict = calcResults[key]
     for connectTuple in dict:
        c1 = connectTuple[0]
        c2 = connectTuple[1]
        
        updateCircuits(circuitManager, c1, c2, certNum)
        certNum = certNum + 1
        if certNum >= connections:
           break;
     if certNum >= connections:
           break;
     
  results = []
  for k,v in circuitManager.items():
     results.append(len(v))

  results.sort(reverse=True)
  print(results)

  result = results[0] * results[1] * results[2]
  
  print(result)
  return result

def processPart2(fileName):
  lines = files.getLinesSplit(fileName, ",")
  targetSize = len(lines)
  coords = []

  calcResults = {}

  for line in lines:
    coords.append(Coordinate(int(line[0]), int(line[1]), int(line[2])))
  
  for i in range(0, len(coords)):
    c = coords[i]
    for j in range(i + 1, len(coords)):
      c2 = coords[j]

      dx = c2.x - c.x
      dy = c2.y - c.y
      dz = c2.z - c.z
      dist = math.sqrt( dx * dx + dy * dy + dz * dz)

      dict = calcResults.get(dist, [])
      dict.append((c, c2))
      calcResults[dist] = dict
  
  sortedKeys = list(calcResults.keys())
  sortedKeys.sort()
  circuitManager = {}
  certNum = 0
  result = None
  for key in sortedKeys:
     dict = calcResults[key]
     for connectTuple in dict:
        c1 = connectTuple[0]
        c2 = connectTuple[1]
        
        newSize = updateCircuits(circuitManager, c1, c2, certNum)
        certNum = certNum + 1
        
        if newSize == targetSize:
           print(c1.x, c2.x, newSize)
           result = c1.x * c2.x
           break;
        
     if result != None:
           break;
     
  
  print(result)
  return result
