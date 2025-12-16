def getLines(fileName):
    with open('aoc/' + fileName , 'r') as file:
        linesCleaned = []
        for line in file.readlines():
            line = line.replace("\n", "")
            linesCleaned.append(line)
        return linesCleaned

def getLinesAsCharArrays(fileName):
    with open('aoc/' + fileName , 'r') as file:
        linesCleaned = []
        for line in file.readlines():
            line = line.replace("\n", "")
            linesCleaned.append(list(line))
        return linesCleaned