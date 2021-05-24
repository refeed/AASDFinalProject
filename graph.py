import operator

from pprint import pprint
from table_to_graph import graph_dict
from queue import Queue


energy_dict = dict()


def add_energy_to_nama_node(nama_node_str):
    energy_dict['Nama-' + nama_node_str] = (
        energy_dict.get('Nama-' + nama_node_str, 0) + 1)


def get_nama_barang_nodes():
    nama_barang_nodes = []
    for key in graph_dict:
        if key.startswith('Nama-'):
            nama_barang_nodes.append(key.split('-')[1])
    return nama_barang_nodes


def generate_recommendation_from_current_energy_state():
    initial_nodes = set()
    bfs_queue = Queue()
    traversed_nodes = set()

    # Initial nodes
    for node in energy_dict:
        initial_nodes.add(node)
        bfs_queue.put(node)

    # Traverse each nodes
    while bfs_queue.qsize() > 0:
        current_node = bfs_queue.get()
        if current_node in traversed_nodes:
            continue
        current_energy = energy_dict[current_node]

        adjacent_nodes = graph_dict[current_node]
        energy_to_be_shared = current_energy / len(adjacent_nodes)
        for node in adjacent_nodes:
            bfs_queue.put(node)
            energy_dict[node] = energy_dict.get(node, 0) + energy_to_be_shared

        traversed_nodes.add(current_node)

    recommendation_energy_dict = {}
    for node in energy_dict:
        if node in initial_nodes or not node.startswith('Nama-'):
            continue
        recommendation_energy_dict[node] = energy_dict[node]

    recommendation_list = sorted(
        recommendation_energy_dict.items(), key=operator.itemgetter(1),
        reverse=True)

    return recommendation_list


if __name__ == '__main__':
    add_energy_to_nama_node(
        'ECLE Wireless On Ear Headphone Headset Gaming Super Bass Stereo Hitam')
    add_energy_to_nama_node(
        'ECLE Bluetooth Wireless Speaker Mini Portable Super Bass Stereo')

    pprint(generate_recommendation_from_current_energy_state())
