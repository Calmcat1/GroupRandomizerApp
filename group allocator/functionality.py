# this file handles the functionality of the group
#this app basically consists of 3 modules, the array maker, shuffler and group placer

import random


#simple function for opening files and reading the contents and putting them to an array
def fileArray(file):
  file = open(file)
  variables = file.read()
  names = variables.split('\n')
  return names


#simple function takes the above array and randomizes it
def randomizeArray(fileResults):
    random.shuffle(fileResults)
    return fileResults

    
#simple function takes the results from the array above and puts it into groups
def nameAllocator(results):
  output = ''
  counter = 0
  groupNo = 1
  n = len(results)
  for i in range(n):
    if counter <= 5:
      output += results[i] + ' '
      counter += 1
    else:
      groupNo += 1
      output += '\n\n' + f'group{groupNo}:'  + '\n'
      counter = 0
  return 'group1:\n' + output 

  



  


# test cases

print(fileArray('filesToBeRead/demo.txt'))

print(nameAllocator(["Alice", "Bob", "Charlie", "David", "Emma", "Frank", "Grace", "Henry", "Isabella", "Jack", "Katherine", "Liam", "Mia", "Noah", "Olivia", "Peter", "Quinn", "Ryan", "Sophia", "Thomas"]
))

print(randomizeArray(['jim','here','what','are','you']))


#application full function test case

print(nameAllocator(randomizeArray(fileArray('filesToBeRead/demo.txt'))))




