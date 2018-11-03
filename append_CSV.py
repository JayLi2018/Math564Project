import os
import glob


os.chdir("/home/chenjie/Desktop/Math564Project/nba_reference/")
fout=open("all.csv","a") #append mode
# first file:
for line in open("player_2014.csv"):
    fout.write(line)
# now the rest:    
for num in range(2015,2018):
    f = open("player_"+str(num)+".csv")
    f.__next__()# skip the header
    for line in f:
         fout.write(line)
    f.close() # not really needed
fout.close()



