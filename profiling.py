import os
import pandas
from pandas import read_csv

pandas.set_option('display.max_rows', None)

os.system("perf stat -e 'syscalls:sys_enter_*' -a sleep 10 2>&1 | awk '$1 != 0' > perf.txt")


dfsyscallmap = read_csv("syscallmap.csv")


f = open("perf.txt", "r")


temp = []
new_temp = []

for line in f:
   temp.append(line)



f.close()


for n in temp[3:-3]:
  sp = n.split()
  new_temp.append(sp[0].replace(',', '')+","+sp[1][19:])


f = open("new.txt", "w")

f.write("Frequency,Syscall\n")
for x in new_temp:
  f.write(x+"\n")

f.close()


df = read_csv("new.txt")


df = df.sort_values('Frequency', ascending=False)

df = df.reset_index(drop=True)



print("Syscalls sorted (desc) by freq.:")
print("----------------------------------------------")
print(df)
print("----------------------------------------------\n")



kernelprofiler = []


for i in range(len(df.index)):
  syscalled = df.loc[i]["Syscall"]
  find = dfsyscallmap.loc[dfsyscallmap['Syscall'] == syscalled]
  if find.empty == 0 and find.iloc[0,1] not in kernelprofiler:
    kernelprofiler.append(find.iloc[0,1])



print("Kernel components accessed sorted by priority:")
print("----------------------------------------------")
for k in kernelprofiler:
  print(k)
