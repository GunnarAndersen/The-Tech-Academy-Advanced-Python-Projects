


import os

fPath = os.listdir(path='C:\\drillFolder\\')

print(fPath)

file = 'Flex.txt'
jPath = os.path.join(fPath,file)
print(jPath)
