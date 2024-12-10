import matplotlib.pyplot as plt

def show_plot(results_cloud, results_fec, results_edge, dataset_label):
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
    bar_width = 0.1
    
    # Create a figure with 3 horizontally aligned subplots
    fig, axs = plt.subplots(1, 3, figsize=(12, 6))
    
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

# Define the existing functions (first_fit, next_fit, compare_algorithms, plot_combined_comparison)
