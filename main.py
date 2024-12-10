import time
from algorithms import first_fit, next_fit
from data import shuffle_fog_nodes, fog_nodes_1, modules_1, fog_nodes_2, modules_2, fog_nodes_3, modules_3
from plot import show_plot
import matplotlib.pyplot as plt

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
    print(f"{'Algorithm':<15}{'Placed Modules':<15}{'Total Latency (ms)':<20}{'Total Energy (W)':<20}{'Total Network Usage (Mbps)':<20}{'Execution Time (s)'}")
    print("-" * 100)
   
    print(f"{'First Fit':<15}{first_fit_placed:<15}{first_fit_latency:<20}{first_fit_energy:<20}{first_fit_network:<20}{first_fit_time:.6f}")
    print(f"{'Next Fit':<15}{next_fit_placed:<15}{next_fit_latency:<20}{next_fit_energy:<20}{next_fit_network:<20}{next_fit_time:.6f}")
   
    return {
        'first_fit': {
            'latency': first_fit_latency,
            'energy': first_fit_energy,
            'network_usage': first_fit_network,
        },
        'next_fit': {
            'latency': next_fit_latency,
            'energy': next_fit_energy,
            'network_usage': next_fit_network,
        }
    }

def compare_and_plot(dataset_label, fog_nodes, modules):
    # Shuffle the fog nodes before comparison
    fog_nodes = shuffle_fog_nodes(fog_nodes)
    
    results_cloud = compare_algorithms(modules, fog_nodes, 'cloud')
    results_fog = compare_algorithms(modules, fog_nodes, 'fog')
    results_edge = compare_algorithms(modules, fog_nodes, 'edge')
    # Plot combined results
    show_plot(results_cloud, results_fog, results_edge, dataset_label)

# Run comparisons and plots for all three datasets
compare_and_plot('Dataset 1', fog_nodes_1, modules_1)
compare_and_plot('Dataset 2', fog_nodes_2, modules_2)
compare_and_plot('Dataset 3', fog_nodes_3, modules_3)

plt.show()  # Show all plots at once
