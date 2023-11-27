import os
import re
import csv
import networkx as nx

import pandas as pd
# 打开文件
# 版本为python3，如果为python2需要在字符串前面加上u
import re
G=nx.Graph()
name=[]
values=[]
file=open("TextAnalyser/output.csv","r",encoding='gbk')
stus=csv.reader(file)
for ss in stus:
    name.append(ss[0])
    values.append(ss[1])
file.close()
name.pop(0)
values.pop(0)
print(name)
print(values)
for i in range(100):
    G.add_node(name[i],weight=values[i])

edges=[]
print(G.nodes(data=True))
sname=name[0:100]
for name1 in sname:
    for name2 in sname:
        w=0
        for i in range(1,120):
            path="./data/"+f"{i}"+'.txt'
           
            file = open(path,"r",encoding='UTF-8')
            text=file.readlines()
            for sen in text:
                if name1 in sen and name2 in sen:
                            w+=1
        if w!=0 and name1!=name2:
            edges.append([name1,name2,w])
            G.add_edge(name1,name2,wg=w)
    print("进度+1\n")
    file.close()
print(edges)
print('\njjjjjjjjjjjjjj')
print(G.edges(data=True))

nodes=[]
for node in sname:
     num=name.index(node)
     nodes.append([node,node,values[num]])
with open('node.csv','w',encoding='utf-8',newline='') as f:
    writer=csv.writer(f)
    writer.writerow(['Id','label','weight'])
    writer.writerows(nodes)

edgesa=[]
for edge in G.edges(data=True):
     edgesa.append([edge[0],edge[1],edge[2]['wg'],'undirected'])
with open('edge.csv','w',encoding='utf-8',newline='') as f:
    writer=csv.writer(f)
    writer.writerow(['source','target','weight','Type'])
    writer.writerows(edgesa)

                                        
                    
