import random

def generate_ipv4_address():
	ip_parts=[str(random.randint(0,255)) for _ in range(4)]
	return ".".join(ip_parts)

def generate_unique_ipv4_addresses(num_addresses):
	unique_addresses= set()
	while len(unique_addresses)<num_addresses:
		unique_addresses.add(generate_ipv4_address())
	return list(unique_addresses)

num_infected_nodes=40
num_uninfected_nodes=600

all_ip_addresses=generate_unique_ipv4_addresses(num_infected_nodes+num_uninfected_nodes)

random.shuffle(all_ip_addresses)

infected_node_addresses = all_ip_addresses[:num_infected_nodes]
uninfected_node_addresses=all_ip_addresses[num_infected_nodes:]

with open('mozi/infected_nodes.txt','w') as infected_file:
	for address in infected_node_addresses:
		infected_file.write(f"{address}\n")
with open("mozi/uninfected_nodes.txt","w") as uninfected_file:
	for address in uninfected_node_addresses:
		uninfected_file.write(f"{address}\n")

print(f"{num_infected_nodes}generate")
print(f"{num_uninfected_nodes}generate")
