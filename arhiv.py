# encoding=utf-8
import tarfile
import os
import random
import re
from datetime import datetime, timedelta

atm = datetime.now()

#file = tarfile.open("C:\\girl\\sample.tar.gz", "r:gz") #open file
#file.extractall(r"C:\girl\files") #de-archivate file in the directory
guid = '{guid}' #comp guid

s = '2017-10-16T05:00:00+03:00' #start time
fmt = "%Y-%m-%dT%H:%M:%S+03:00" #time formatter
mytime = datetime.strptime(s, fmt)
d = timedelta(seconds=5)
#print(mytime.strftime("%Y.%m.%d %H:%M:%S"))

#fmt = "%Y-%m-%dT%H:%M:%S+03:00"

id = 1 #snapshot id
k=1 #just for naming archives
snapshots = os.listdir(r'C:\girl\files\origin') #make list of files in the directory to choose from

for i in range(720):
    next_time = mytime + timedelta(minutes=1)
    archive_name = guid + str(k)#+'-'+mytime.strftime(fmt)+'-'+next_time.strftime(fmt)
    print('Archive will be named -', archive_name)

    tar = tarfile.open("C:\\girl\\files\\archieves\\{}.tar.gz".format(archive_name), "w:gz")

    for j in range(12):

        inside_time_begin = mytime.strftime(fmt)
        mytime = mytime + d
        inside_time_end = mytime.strftime(fmt)
        print(inside_time_begin, inside_time_end) #generated snapshot name
        snapshot = random.choice(snapshots)
        print(id, snapshot)
        #copyfile("C:\\girl\\files\\{}".format(snapshot), "C:\\girl\\files\\another\\{}".format(id))

        with open("C:\\girl\\files\\origin\\{}".format(snapshot), 'r') as file:
            filedata = file.read()

        new_data = filedata.replace(re.search(r'begin...(.*)...end', filedata).group(1), inside_time_begin)
        new_data = new_data.replace(re.search(r'end...(.*)...state', filedata).group(1), inside_time_end)

        with open("C:\\girl\\files\\another\\{}".format(id), 'w') as file:
            file.write(new_data)

        tar.add("C:\\girl\\files\\another\\{}".format(id), arcname=str(id), recursive=False)




        id+=1 #next id in this day
    k+=1
    tar.close()

    print(datetime.now() - atm)