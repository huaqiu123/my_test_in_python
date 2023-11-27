import random
import networkx as nx
import csv

with open("mozi/infected_nodes.txt","r") as infected_file:
	infected_nodes=infected_file.read().splitlines()
with open("mozi/uninfected_nodes.txt","r") as uninfected_file:
	uninfected_nodes=uninfected_file.read().splitlines()
with open("mozi/infection_flows.csv","w",newline="") as csv_file:
	writer=csv.writer(csv_file)
	writer.writerow(['source_ip','target_ip','weight'])

	for target_ip in uninfected_nodes:
		for source_ip in infected_nodes:
			weight=round(random.uniform(0.000001,0.00002),16)
			writer.writerow([source_ip,target_ip,weight]) 




