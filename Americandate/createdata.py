import os
import date
print('hhhhhhhhh')
cwd=os.getcwd()
datapath=cwd+'\\Americandate\\data'
print(datapath)
for i in range(1,1000):
    name=list(date.days_to_date_str(i))
    print(name)
    file=open(datapath+'\\'+name,'w')
    file.write(name)
    file.close()