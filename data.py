import random

# Dataset 1
fog_nodes_1 = [
    {'id': 'LimitedNode', 'cpu': 10, 'memory': 10, 'cloud_latency': 200, 'fec_latency': 10, 'edge_latency': 5,  'cloud_bandwidth': 500, 'fec_bandwidth': 100, 'edge_bandwidth': 50, 'cloud_power': 50, 'fec_power': 20, 'edge_power': 10},
    {'id': 'Mobile', 'cpu': 20, 'memory': 30, 'cloud_latency': 200, 'fec_latency': 2, 'edge_latency': 1,  'cloud_bandwidth': 1000, 'fec_bandwidth': 250, 'edge_bandwidth': 200, 'cloud_power': 300, 'fec_power': 82, 'edge_power': 50},
    {'id': 'Router', 'cpu': 50, 'memory': 50, 'cloud_latency': 200, 'fec_latency': 5, 'edge_latency': 3,  'cloud_bandwidth': 10000, 'fec_bandwidth': 5000, 'edge_bandwidth': 2500, 'cloud_power': 107, 'fec_power': 83, 'edge_power': 60},
    {'id': 'Fog-gateway', 'cpu': 40, 'memory': 60, 'cloud_latency': 200, 'fec_latency': 20, 'edge_latency': 10,  'cloud_bandwidth': 10000, 'fec_bandwidth': 10000, 'edge_bandwidth': 5000, 'cloud_power': 200, 'fec_power': 100, 'edge_power': 70},
]

modules_1 = [
    {'id': 1, 'cpu': 20, 'memory': 20},
    {'id': 2, 'cpu': 25, 'memory': 25},
    {'id': 3, 'cpu': 30, 'memory': 30},
    {'id': 4, 'cpu': 35, 'memory': 35},
    {'id': 5, 'cpu': 40, 'memory': 40},
    {'id': 6, 'cpu': 15, 'memory': 15},
    {'id': 7, 'cpu': 20, 'memory': 20},
    {'id': 8, 'cpu': 30, 'memory': 30},
    {'id': 9, 'cpu': 50, 'memory': 50},
    {'id': 10, 'cpu': 60, 'memory': 60},
]

# Dataset 2 (different parameters)
fog_nodes_2 = [
    {'id': 'NodeA', 'cpu': 30, 'memory': 40, 'cloud_latency': 180, 'fec_latency': 8, 'edge_latency': 4, 'cloud_bandwidth': 700, 'fec_bandwidth': 150, 'edge_bandwidth': 100, 'cloud_power': 60, 'fec_power': 25, 'edge_power': 15},
    {'id': 'NodeB', 'cpu': 25, 'memory': 35, 'cloud_latency': 190, 'fec_latency': 3, 'edge_latency': 2, 'cloud_bandwidth': 1200, 'fec_bandwidth': 300, 'edge_bandwidth': 250, 'cloud_power': 320, 'fec_power': 90, 'edge_power': 60},
    {'id': 'NodeC', 'cpu': 55, 'memory': 60, 'cloud_latency': 210, 'fec_latency': 6, 'edge_latency': 3, 'cloud_bandwidth': 11000, 'fec_bandwidth': 6000, 'edge_bandwidth': 3000, 'cloud_power': 110, 'fec_power': 85, 'edge_power': 70},
    {'id': 'NodeD', 'cpu': 45, 'memory': 70, 'cloud_latency': 205, 'fec_latency': 25, 'edge_latency': 12, 'cloud_bandwidth': 15000, 'fec_bandwidth': 12000, 'edge_bandwidth': 7000, 'cloud_power': 250, 'fec_power': 110, 'edge_power': 80},
]

modules_2 = [
    {'id': 11, 'cpu': 15, 'memory': 15},
    {'id': 12, 'cpu': 20, 'memory': 20},
    {'id': 13, 'cpu': 25, 'memory': 25},
    {'id': 14, 'cpu': 30, 'memory': 30},
    {'id': 15, 'cpu': 35, 'memory': 35},
    {'id': 16, 'cpu': 40, 'memory': 40},
    {'id': 17, 'cpu': 45, 'memory': 45},
    {'id': 18, 'cpu': 50, 'memory': 50},
    {'id': 19, 'cpu': 55, 'memory': 55},
    {'id': 20, 'cpu': 60, 'memory': 60},
]

# Dataset 3 (another variation)
fog_nodes_3 = [
    {'id': 'Node1', 'cpu': 40, 'memory': 50, 'cloud_latency': 160, 'fec_latency': 5, 'edge_latency': 2, 'cloud_bandwidth': 800, 'fec_bandwidth': 200, 'edge_bandwidth': 150, 'cloud_power': 70, 'fec_power': 30, 'edge_power': 20},
    {'id': 'Node2', 'cpu': 35, 'memory': 45, 'cloud_latency': 190, 'fec_latency': 4, 'edge_latency': 1, 'cloud_bandwidth': 900, 'fec_bandwidth': 250, 'edge_bandwidth': 180, 'cloud_power': 350, 'fec_power': 85, 'edge_power': 55},
    {'id': 'Node3', 'cpu': 60, 'memory': 70, 'cloud_latency': 220, 'fec_latency': 7, 'edge_latency': 5, 'cloud_bandwidth': 12000, 'fec_bandwidth': 7000, 'edge_bandwidth': 4000, 'cloud_power': 120, 'fec_power': 90, 'edge_power': 75},
    {'id': 'Node4', 'cpu': 50, 'memory': 80, 'cloud_latency': 230, 'fec_latency': 15, 'edge_latency': 8, 'cloud_bandwidth': 16000, 'fec_bandwidth': 15000, 'edge_bandwidth': 6000, 'cloud_power': 300, 'fec_power': 120, 'edge_power': 90},
]

modules_3 = [
    {'id': 21, 'cpu': 10, 'memory': 10},
    {'id': 22, 'cpu': 20, 'memory': 20},
    {'id': 23, 'cpu': 25, 'memory': 25},
    {'id': 24, 'cpu': 30, 'memory': 30},
    {'id': 25, 'cpu': 35, 'memory': 35},
    {'id': 26, 'cpu': 40, 'memory': 40},
    {'id': 27, 'cpu': 45, 'memory': 45},
    {'id': 28, 'cpu': 50, 'memory': 50},
    {'id': 29, 'cpu': 55, 'memory': 55},
    {'id': 30, 'cpu': 60, 'memory': 60},
]

# Function to shuffle nodes
def shuffle_fog_nodes(nodes):
    random.shuffle(nodes)
    nodes[0]['cpu'] -= 5
    nodes[0]['memory'] -= 5
    return nodes
