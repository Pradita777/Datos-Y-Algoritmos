import numpy as np

def getFile(fileName):
    
  with open(fileName) as file:
    text = file.read()
    return text

def getRowsNColumns(text):
    
   nRows = text.split("\n")
   nColumns = nRows[0].split(",")
   
   return len(nRows), len(nColumns)

def getMatrix(text,numberOfRows,numberOfColumns):
  matrix = np.zeros( (numberOfRows-1,numberOfColumns) )
  rows = text.split("\n")
  
  index = 0
  
  for row in rows:
    jIndex = 0
    columns = row.split(",")
    
    for column in columns:
      if column != '':
        matrix[index][jIndex] = int(column)
        jIndex = jIndex + 1
        
    index = index + 1
    
  return matrix
def main():
  nameFile = "_56caf73c-2d5d-11e7-a28f-c563b2540923.csv"
  text = getFile(nameFile)
  numberOfRows, numberOfColumns = getRowsNColumns(text)
  matrix = getMatrix(text, numberOfRows, numberOfColumns)
  print(matrix)

main()
