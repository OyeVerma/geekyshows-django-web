import os

def path(path):
    if '.' in path:
        return True
    else:
        return False

for i in os.listdir():
    if i == 'CORE':
        continue
    else:
        while path(i) == False:
            
