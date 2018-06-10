import os
from datetime import datetime
if __name__=='__main__':
    print(os.listdir('.'))
    print(os.uname())
    print(os.name)
    print(os.stat('data.json')[-4])
    stat = os.stat('data.json')
    atime = datetime.fromtimestamp(stat.st_atime)
    print(atime)

    for filename in os.listdir('.'):
        stat = os.stat(filename)
        print(filename, stat.st_size, stat.st_atime)

