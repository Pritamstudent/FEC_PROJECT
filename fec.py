import time
import matplotlib.pyplot as plt
from algorithms import first_fit, next_fit


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


def plot_combined_comparison(results_cloud, results_fec, results_edge, dataset_label):
    algorithms = ['First Fit', 'Next Fit']
    
    # Metrics for Cloud
    cloud_latency = [results_cloud['first_fit']['latency'], results_cloud['next_fit']['latency']]
    cloud_energy = [results_cloud['first_fit']['energy'], results_cloud['next_fit']['energy']]
    cloud_network_usage = [results_cloud['first_fit']['network_usage'], results_cloud['next_fit']['network_usage']]
    
    # Metrics for FEC
    fec_latency = [results_fec['first_fit']['latency'], results_fec['next_fit']['latency']]
    fec_energy = [results_fec['first_fit']['energy'], results_fec['next_fit']['energy']]
    fec_network_usage = [results_fec['first_fit']['network_usage'], results_fec['next_fit']['network_usage']]
    
    # Metrics for Edge
    edge_latency = [results_edge['first_fit']['latency'], results_edge['next_fit']['latency']]
    edge_energy = [results_edge['first_fit']['energy'], results_edge['next_fit']['energy']]
    edge_network_usage = [results_edge['first_fit']['network_usage'], results_edge['next_fit']['network_usage']]
    
    # Bar width and x-axis positions
    x = range(len(algorithms))
    bar_width = 0.25
    
    # Create a figure with 3 horizontally aligned subplots
    fig, axs = plt.subplots(1, 3, figsize=(20, 6))
    
    # Latency Comparison
    axs[0].bar([i - bar_width for i in x], cloud_latency, width=bar_width, label='Cloud', color='blue')
    axs[0].bar([i for i in x], fec_latency, width=bar_width, label='FEC', color='green')
    axs[0].bar([i + bar_width for i in x], edge_latency, width=bar_width, label='Edge', color='orange')
    axs[0].set_title(f'Latency Comparison ({dataset_label})')
    axs[0].set_ylabel('Total Latency (ms)')
    axs[0].set_xticks(x)
    axs[0].set_xticklabels(algorithms)
    axs[0].legend()
    
    # Energy Comparison
    axs[1].bar([i - bar_width for i in x], cloud_energy, width=bar_width, label='Cloud', color='blue')
    axs[1].bar([i for i in x], fec_energy, width=bar_width, label='FEC', color='green')
    axs[1].bar([i + bar_width for i in x], edge_energy, width=bar_width, label='Edge', color='orange')
    axs[1].set_title(f'Energy Comparison ({dataset_label})')
    axs[1].set_ylabel('Total Energy (W)')
    axs[1].set_xticks(x)
    axs[1].set_xticklabels(algorithms)
    axs[1].legend()
    
    # Network Usage Comparison
    axs[2].bar([i - bar_width for i in x], cloud_network_usage, width=bar_width, label='Cloud', color='blue')
    axs[2].bar([i for i in x], fec_network_usage, width=bar_width, label='FEC', color='green')
    axs[2].bar([i + bar_width for i in x], edge_network_usage, width=bar_width, label='Edge', color='orange')
    axs[2].set_title(f'Network Usage Comparison ({dataset_label})')
    axs[2].set_ylabel('Total Network Usage (Mbps)')
    axs[2].set_xticks(x)
    axs[2].set_xticklabels(algorithms)
    axs[2].legend()
    
    # Adjust layout and display
    plt.tight_layout()
    plt.show()

import time
import matplotlib.pyplot as plt
from data import shuffle_fog_nodes, fog_nodes_1, modules_1, fog_nodes_2, modules_2, fog_nodes_3, modules_3

# Define the existing functions (first_fit, next_fit, compare_algorithms, plot_combined_comparison)

def compare_and_plot(dataset_label, fog_nodes, modules):
    # Shuffle the fog nodes before comparison
    fog_nodes = shuffle_fog_nodes(fog_nodes)
    
    results_cloud = compare_algorithms(modules, fog_nodes, 'cloud')
    results_fec = compare_algorithms(modules, fog_nodes, 'FEC')
    results_edge = compare_algorithms(modules, fog_nodes, 'edge')
    # Plot combined results
    plot_combined_comparison(results_cloud, results_fec, results_edge, dataset_label)

# Run comparisons and plots for all three datasets
compare_and_plot('Dataset 1', fog_nodes_1, modules_1)
compare_and_plot('Dataset 2', fog_nodes_2, modules_2)
compare_and_plot('Dataset 3', fog_nodes_3, modules_3)

plt.show()  # Show all plots at once
