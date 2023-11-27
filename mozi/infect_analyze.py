import networkx as nx
import random
import matplotlib.pyplot as plt
import csv

G=nx.DiGraph()

with open("mozi/infection_flows.csv","r",encoding='utf-8') as f:
	reader=csv.reader(f)
	next(reader)
	for row in reader:
		source_ip,target_ip,weight1=row
		G.add_edge(source_ip,target_ip,weight=float(weight1))

def simulation(graph,seed,iter_num):
	for node in graph:
		graph.nodes[node]['state']=0
	graph.nodes[seed]['state']=1
	all_infected_nodes_round=[]
	infected_nodes=[seed]
	new_nodes_graph=nx.DiGraph()
	new_nodes_graph.add_node(seed)
	for i in range(iter_num):
		new_nodes=[]
		for node in infected_nodes:
			for near in graph.neighbors(node):
				w=graph.get_edge_data(node,near)
				if random.uniform(0,1)<10000*float(w['weight']):
					graph.nodes[near]['state']=1
					new_nodes.append(near)
					new_nodes_graph.add_edge(node,near)
		infected_nodes.extend(new_nodes)
		all_infected_nodes_round.append(list(set(infected_nodes)))

	return infected_nodes,all_infected_nodes_round

s=[]

for no in G:
	all_number=[]
	for i in range(1,11):
		all_infected_nodes,_ =simulation(graph=G,seed=no,iter_num=i)
		all_number.append(len(all_infected_nodes))

	s.append([no]+all_number)

top=sorted(s,key=lambda x:x[-1],reverse=True)[:10]
f_top=[(node[0],node[1:]) for node in top]
for item in f_top:
	print(item)

top_10=[data[0] for data in top]
with open("mozi/infection_flows.csv","r",newline='',encoding='utf-8') as f:
	reader=csv.reader(f)
	header=next(reader)
	top_10_data=[row for row in reader if row[0] in top_10]

with open("mozi/top_10_flows.csv","w",newline='',encoding='utf-8') as f:
	writer=csv.writer(f)
	writer.writerow(header)
	writer.writerows(top_10_data)


ip_weight_sum={ip:[0,0] for ip in top_10}

with open("mozi/infection_flows.csv","r",newline="",encoding='utf-8') as f:
	reader=csv.reader(f)
	next(reader)

	for row in reader:
		source,target,weight2=row
		if source in top_10:
			ip_weight_sum[source][0]+=float(weight2)
			ip_weight_sum[source][1]+=1


ip_weight_average={ip:sum_count[0] for ip,sum_count in ip_weight_sum.items()}

with open("mozi/top10_infected_nodes.csv","w",newline="",encoding='utf-8') as f:
	writer=csv.writer(f)
	writer.writerow(['Id','weight'])
	writer.writerows(ip_weight_average.items())


def random_color():
	colora=['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
	color=''
	for i in range(6):
		color+=colora[random.randint(0,14)]

	return '#'+color
marker=['.',',','v','^','>','#','@','d','x','p','+']
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
plt.figure(figsize=(12,7))
for node in top[:3]:
	ip=node[0]
	x=[i for i in range(11)]
	y=[0]
	y.extend(node[1:])
	plt.plot(x,y,color=random_color(),marker=marker[top.index(node)],label=ip,linewidth=2.5)

plt.xlim(0,len(x))
plt.ylim(0,max(y))
plt.xlabel('Round',fontsize=25)
plt.ylabel('Number',fontsize=25)
plt.legend(fontsize=20,loc='upper right',bbox_to_anchor=(1.13,1.0),borderaxespad=0.)
plt.show()