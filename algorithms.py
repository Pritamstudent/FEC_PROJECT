
def next_fit(modules, fog_nodes, environment):
    nodes_copy = [node.copy() for node in fog_nodes]  # Ensure fog_nodes is not modified globally
    last_index = 0
    placed_count = 0
    total_latency = 0
    total_energy = 0
    total_network_usage = 0
   
    for module in modules:
        placed = False
        for i in range(last_index, len(nodes_copy)):
            node = nodes_copy[i]
            if node['cpu'] >= module['cpu'] and node['memory'] >= module['memory']:
                node['cpu'] -= module['cpu']
                node['memory'] -= module['memory']
               
                # Add edge environment metrics
                if environment == 'cloud':
                    total_latency += node['cloud_latency']
                    total_network_usage += node['cloud_bandwidth']
                    total_energy += node['cloud_power']
                elif environment == 'fog':
                    total_latency += node['fog_latency']
                    total_network_usage += node['fog_bandwidth']
                    total_energy += node['fog_power']
                elif environment == 'edge':
                    total_latency += node['edge_latency']
                    total_network_usage += node['edge_bandwidth']
                    total_energy += node['edge_power']
               
                print(f"Module {module['id']} placed on Node {node['id']} ({environment})")
                last_index = i
                placed = True
                placed_count += 1
                break
        if not placed:
            print(f"Module {module['id']} could not be placed.")
   
    return placed_count, total_latency, total_energy, total_network_usage, nodes_copy
def first_fit(modules, fog_nodes, environment):
    nodes_copy = [node.copy() for node in fog_nodes]  # Ensure fog_nodes is not modified globally
    placed_count = 0
    total_latency = 0
    total_energy = 0
    total_network_usage = 0
   
    for module in modules:
        placed = False
        for node in nodes_copy:
            if node['cpu'] >= module['cpu'] and node['memory'] >= module['memory']:
                node['cpu'] -= module['cpu']
                node['memory'] -= module['memory']
               
                # Add edge environment metrics
                if environment == 'cloud':
                    total_latency += node['cloud_latency']
                    total_network_usage += node['cloud_bandwidth']
                    total_energy += node['cloud_power']
                elif environment == 'fog':
                    total_latency += node['fog_latency']
                    total_network_usage += node['fog_bandwidth']
                    total_energy += node['fog_power']
                elif environment == 'edge':
                    total_latency += node['edge_latency']
                    total_network_usage += node['edge_bandwidth']
                    total_energy += node['edge_power']
               
                print(f"Module {module['id']} placed on Node {node['id']} ({environment})")
                placed = True
                placed_count += 1
                break
        if not placed:
            print(f"Module {module['id']} could not be placed.")
   
    return placed_count, total_latency, total_energy, total_network_usage, nodes_copy
