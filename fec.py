import time

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
               
                if environment == 'cloud':
                    total_latency += node['cloud_latency']
                    total_network_usage += node['cloud_network_usage']
                    total_energy += (module['cpu'] * node['energy_per_cpu']) + (module['memory'] * node['energy_per_memory'])
                elif environment == 'FEC':
                    total_latency += node['fec_latency']
                    total_network_usage += node['fec_network_usage']
                    total_energy += (module['cpu'] * node['energy_per_cpu']) + (module['memory'] * node['energy_per_memory'])
               
                print(f"Module {module['id']} placed on Node {node['id']} ({environment})")
                placed = True
                placed_count += 1
                break
        if not placed:
            print(f"Module {module['id']} could not be placed.")
   
    return placed_count, total_latency, total_energy, total_network_usage, nodes_copy

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
               
                if environment == 'cloud':
                    total_latency += node['cloud_latency']
                    total_network_usage += node['cloud_network_usage']
                    total_energy += (module['cpu'] * node['energy_per_cpu']) + (module['memory'] * node['energy_per_memory'])
                elif environment == 'FEC':
                    total_latency += node['fec_latency']
                    total_network_usage += node['fec_network_usage']
                    total_energy += (module['cpu'] * node['energy_per_cpu']) + (module['memory'] * node['energy_per_memory'])
               
                print(f"Module {module['id']} placed on Node {node['id']} ({environment})")
                last_index = i
                placed = True
                placed_count += 1
                break
        if not placed:
            print(f"Module {module['id']} could not be placed.")
   
    return placed_count, total_latency, total_energy, total_network_usage, nodes_copy

def compare_algorithms(modules, fog_nodes, environment):
    print(f"\nComparing {environment} environment - {len(modules)} modules and {len(fog_nodes)} fog nodes")
   
    print("First Fit Algorithm:")
    start_time = time.time()
    first_fit_placed, first_fit_latency, first_fit_energy, first_fit_network, first_fit_nodes = first_fit(modules, fog_nodes, environment)
    first_fit_time = time.time() - start_time
   
    print("\nNext Fit Algorithm:")
    start_time = time.time()
    next_fit_placed, next_fit_latency, next_fit_energy, next_fit_network, next_fit_nodes = next_fit(modules, fog_nodes, environment)
    next_fit_time = time.time() - start_time
   
    print("\nComparison Results:")
    print(f"{'Algorithm':<15}{'Placed Modules':<15}{'Total Latency (ms)':<20}{'Total Energy (J)':<20}{'Total Network Usage (MB)':<20}{'Execution Time (s)'}")
    print("-" * 100)
   
    print(f"{'First Fit':<15}{first_fit_placed:<15}{first_fit_latency:<20}{first_fit_energy:<20}{first_fit_network:<20}{first_fit_time:.6f}")
    print(f"{'Next Fit':<15}{next_fit_placed:<15}{next_fit_latency:<20}{next_fit_energy:<20}{next_fit_network:<20}{next_fit_time:.6f}")

# Test Data 1: Balanced modules and nodes
modules1 = [
    {'id': 1, 'cpu': 10, 'memory': 20},
    {'id': 2, 'cpu': 15, 'memory': 25},
    {'id': 3, 'cpu': 20, 'memory': 30},
    {'id': 4, 'cpu': 25, 'memory': 35},
    {'id': 5, 'cpu': 30, 'memory': 40},
    {'id': 6, 'cpu': 15, 'memory': 15},
    {'id': 7, 'cpu': 10, 'memory': 10},
    {'id': 8, 'cpu': 20, 'memory': 25},
]

fog_nodes1 = [
    {'id': 'A', 'cpu': 50, 'memory': 60, 'cloud_latency': 5, 'fec_latency': 15, 'cloud_network_usage': 100, 'fec_network_usage': 300, 'energy_per_cpu': 0.5, 'energy_per_memory': 0.3},
    {'id': 'B', 'cpu': 50, 'memory': 50, 'cloud_latency': 8, 'fec_latency': 18, 'cloud_network_usage': 120, 'fec_network_usage': 320, 'energy_per_cpu': 0.4, 'energy_per_memory': 0.2},
    {'id': 'C', 'cpu': 40, 'memory': 40, 'cloud_latency': 6, 'fec_latency': 16, 'cloud_network_usage': 110, 'fec_network_usage': 310, 'energy_per_cpu': 0.6, 'energy_per_memory': 0.4},
]

# Test Data 2: High resource demands and high energy usage
modules2 = [
    {'id': 1, 'cpu': 40, 'memory': 50},
    {'id': 2, 'cpu': 45, 'memory': 55},
    {'id': 3, 'cpu': 50, 'memory': 60},
    {'id': 4, 'cpu': 60, 'memory': 70},
    {'id': 5, 'cpu': 35, 'memory': 45},
    {'id': 6, 'cpu': 40, 'memory': 50},
    {'id': 7, 'cpu': 55, 'memory': 65},
    {'id': 8, 'cpu': 50, 'memory': 55},
]

fog_nodes2 = [
    {'id': 'A', 'cpu': 100, 'memory': 120, 'cloud_latency': 5, 'fec_latency': 15, 'cloud_network_usage': 150, 'fec_network_usage': 400, 'energy_per_cpu': 0.7, 'energy_per_memory': 0.5},
    {'id': 'B', 'cpu': 80, 'memory': 100, 'cloud_latency': 10, 'fec_latency': 20, 'cloud_network_usage': 160, 'fec_network_usage': 420, 'energy_per_cpu': 0.8, 'energy_per_memory': 0.6},
    {'id': 'C', 'cpu': 60, 'memory': 80, 'cloud_latency': 8, 'fec_latency': 18, 'cloud_network_usage': 155, 'fec_network_usage': 410, 'energy_per_cpu': 0.9, 'energy_per_memory': 0.7},
]

# Test Data 3: Small modules with lower power and latency constraints
modules3 = [
    {'id': 1, 'cpu': 5, 'memory': 5},
    {'id': 2, 'cpu': 10, 'memory': 10},
    {'id': 3, 'cpu': 5, 'memory': 5},
    {'id': 4, 'cpu': 10, 'memory': 10},
    {'id': 5, 'cpu': 8, 'memory': 8},
    {'id': 6, 'cpu': 6, 'memory': 6},
    {'id': 7, 'cpu': 9, 'memory': 9},
    {'id': 8, 'cpu': 5, 'memory': 5},
]

fog_nodes3 = [
    {'id': 'A', 'cpu': 50, 'memory': 60, 'cloud_latency': 3, 'fec_latency': 12, 'cloud_network_usage': 80, 'fec_network_usage': 250, 'energy_per_cpu': 0.3, 'energy_per_memory': 0.2},
    {'id': 'B', 'cpu': 40, 'memory': 50, 'cloud_latency': 4, 'fec_latency': 14, 'cloud_network_usage': 90, 'fec_network_usage': 270, 'energy_per_cpu': 0.2, 'energy_per_memory': 0.1},
    {'id': 'C', 'cpu': 30, 'memory': 40, 'cloud_latency': 2, 'fec_latency': 10, 'cloud_network_usage': 85, 'fec_network_usage': 260, 'energy_per_cpu': 0.25, 'energy_per_memory': 0.15},
]

# Run comparisons for the new datasets
compare_algorithms(modules1, fog_nodes1, 'cloud')
compare_algorithms(modules1, fog_nodes1, 'FEC')

compare_algorithms(modules2, fog_nodes2, 'cloud')
compare_algorithms(modules2, fog_nodes2, 'FEC')

compare_algorithms(modules3, fog_nodes3, 'cloud')
compare_algorithms(modules3, fog_nodes3, 'FEC')

