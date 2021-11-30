#defining glyft so that returns work properly
def gLyft():
    #taking in input file names
  locationsFileName = input('Enter Locations Filename: ')
  namesFileName = input('Enter Names Filename: ')
#opening files and running errors if they don't exist
  try:
    fhandlocations = open(locationsFileName)
  except:
    print ('Input file could not be opened.')
    return 1;

  try:
    fhandnames = open(namesFileName)
  except:
    print ('Input file could not be opened.')
    return 1;
#opening a writable output file
  fhandoutput = open('journey.txt', "w")
#initializing some variables
  columnsBoundaryRight = None
  rowsBoundaryLower = None
  startColumn = None
  startRow = None
  endColumn = None
  endRow = None
  counterOfLocationsVisited = 0
  allCoordinateColumns = []
  allCoordinateRows = []
  allCoordinateLetters = []
  allCoordinateHashes = []
  hashesAndNames = dict()
  visitedLog = []
#processing the inputs from the locations as a sorted set of strings
  i = 0
  for line in fhandlocations:
    i = i + 1
    workingSplitLine = line.split()
    if i == 1:
      columnsBoundaryRight = int(workingSplitLine[0])
      rowsBoundaryLower = int(workingSplitLine[1])
      continue
    if i == 2:
      startColumn = int(workingSplitLine[0])
      startRow = int(workingSplitLine[1])
      continue
    if i == 3:
      endColumn = int(workingSplitLine[0])
      endRow = int(workingSplitLine[1])
      continue

    if (i > 3 and 1<= int(workingSplitLine[0]) <= columnsBoundaryRight and 1<= int(workingSplitLine[1]) <= rowsBoundaryLower):
      allCoordinateColumns.append(workingSplitLine[0])
      allCoordinateRows.append(workingSplitLine[1])
      allCoordinateLetters.append(workingSplitLine[2])
      allCoordinateHashes.append(workingSplitLine[3])
      counterOfLocationsVisited = counterOfLocationsVisited + 1
      visitedLog.append(0)

#excepting if the points are out of boundaries
    else:
      print(workingSplitLine[3],'is out of range - ignoring')


  #define an order for the planets
  currentColumnPos = startColumn
  currentRowPos = startRow
  k = 0
  presentWorkingBestDistance = columnsBoundaryRight**2 + rowsBoundaryLower**2
  presentWorkingBestHash = None
  l = 0
  finalOrderedHashList = []
  finalCoordinateColumns = []
  finalCoordinateRows = []
  finalCoordinateLetters = []
  m = 0
  print(allCoordinateHashes)
  while l < len(allCoordinateHashes):
      k = 0
      presentWorkingBestDistance = columnsBoundaryRight**2 + rowsBoundaryLower**2
      presentWorkingBestHash = None
      m = None

      while k < len(allCoordinateHashes):
          print('ran inner loop')
          if (visitedLog[k] == 0):
              diffXs= int(allCoordinateColumns[k]) - int(currentColumnPos)
              diffYs = int(allCoordinateRows[k])  - int(currentRowPos)
              currentDist = diffXs * diffXs + diffYs * diffYs
              print(currentDist)
              print(presentWorkingBestHash)
              print()

              if (currentDist < int(presentWorkingBestDistance)):
                  presentWorkingBestHash = allCoordinateHashes[k]
                  m = k
                  presentWorkingBestDistance = currentDist
                  visitedLog[k] = 1

              if (currentDist == int(presentWorkingBestDistance)):
                  if (presentWorkingBestHash > allCoordinateHashes[k]):
                      presentWorkingBestHash = allCoordinateHashes[k]
                      m=k
                      presentWorkingBestDistance = currentDist
                      visitedLog [k] = 1
          k = k + 1
      l = l + 1
      k = 0
      print(allCoordinateColumns)
      try:
          finalOrderedHashList.append(presentWorkingBestHash)
          finalCoordinateColumns.append(allCoordinateColumns[m])
          finalCoordinateRows.append(allCoordinateRows[m])
          finalCoordinateLetters.append(allCoordinateLetters[m])
          currentColumnPos = allCoordinateColumns[m]
          currentRowPos = allCoordinateRows[m]
      except:
          print('except1')
  print(finalOrderedHashList)
  print(finalCoordinateColumns)
  print(finalCoordinateRows)
  print(finalCoordinateLetters)
#replacing the XX and fixing the _ to space
  item = ''
  for lineNames in fhandnames:
    lineWorkingNames = lineNames.split()
    item = lineWorkingNames[1]

    item = item.replace('XX','')
    item = item.replace('_',' ')
    hashesAndNames[lineWorkingNames[0]] = item

#making a map of periods and planet symbols
  print('BRUHHHHHHHHHHH')
  listMapFinal = []
  n = 0
  o = 0
  while n < rowsBoundaryLower:
      o = 0
      while o < columnsBoundaryRight:
          #listMapFinal.append('.')
          listMapFinal.append(o)
          o = o + 1
      n = n + 1
  print(rowsBoundaryLower, columnsBoundaryRight)
  print(listMapFinal)

  p = 0
  print((int(finalCoordinateRows[p]) - 1) * int(columnsBoundaryRight) + int(finalCoordinateRows[p]) - 1)
  print(finalCoordinateRows)
  print(finalCoordinateColumns)
  print(finalCoordinateLetters)
  print(listMapFinal)
  while p < counterOfLocationsVisited - 1:
      listMapFinal[(int(finalCoordinateRows[p]) - 1) * int(columnsBoundaryRight) + int(finalCoordinateRows[p]) - 1] = finalCoordinateLetters
      p = p + 1
  listMapFinal[(int(startRow) - 1) * int(columnsBoundaryRight) + int(startColumn) - 1] = 'S'
  listMapFinal[(int(endRow) - 1) * int(columnsBoundaryRight) + int(endColumn) - 1] = 'E'


  listMapFinalString = ''
  for items in listMapFinal:
      listMapFinalString = listMapFinalString + str(items)

  q = 0
  while q < rowsBoundaryLower - 1:
      fhandoutput.write(listMapFinalString[q * columnsBoundaryRight : (q+1) * columnsBoundaryRight])
      q = q + 1

#print out the instructions for the output file
  fhandoutput.write("Start at " + str(startColumn) + " " + str(startRow) +"\n")
  j=0
  while j < int(len(finalCoordinateColumns)): #THIS ONLY RUNS ONCE FOR SOME REASON
    fhandoutput.write("Go to " + str(hashesAndNames[finalOrderedHashList[j]]) + " at " + str(finalCoordinateColumns[j]) + " "+ str(finalCoordinateRows[j])+"\n")
    j = j+1


  fhandoutput.write("End at " + str(endColumn) + " "+ str(endRow))

  fhandoutput.close()

gLyft()
