import tkinter as tk
from tkinter import ttk
import random
import networkx as nx
import matplotlib.pyplot as plt

def generate_random_graph(num_nodes, density, directed=False):
    inf = float('inf')
    graph = [[inf for _ in range(num_nodes)] for _ in range(num_nodes)]
    
    for i in range(num_nodes):
        graph[i][i] = 0

    for i in range(num_nodes):
        for j in range(num_nodes):
            if i != j and random.random() < density:
                weight = random.randint(1, 10)
                graph[i][j] = weight
                if not directed:
                    graph[j][i] = weight
    
    return graph

def display_graph(graph, text_widget):
    text_widget.delete(1.0, tk.END)
    for row in graph:
        text_widget.insert(tk.END, ' '.join(f'{w:5}' if w != float('inf') else '  inf' for w in row) + '\n')

def networkplot(graph, directed=False):
    G = nx.DiGraph() if directed else nx.Graph()
    for i, row in enumerate(graph):
        for j, weight in enumerate(row):
            if weight != float('inf') and i != j:
                G.add_edge(i, j, weight=weight)
    pos = nx.spring_layout(G)
    edge_labels = {(i, j): f'{weight}' for i, j, weight in G.edges(data='weight')}
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.show()

def generate_and_display_graph():
    num_nodes = int(nodes_entry.get())
    density = float(density_entry.get())
    directed = directed_var.get()
    
    graph = generate_random_graph(num_nodes, density, directed)
    display_graph(graph, graph_display)
    networkplot(graph, directed)

app = tk.Tk()
app.title("Random Graph Generator")

frame = ttk.Frame(app, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

ttk.Label(frame, text="Number of Nodes:").grid(row=0, column=0, sticky=tk.W)
nodes_entry = ttk.Entry(frame, width=7)
nodes_entry.grid(row=0, column=1)
nodes_entry.insert(0, "5")

ttk.Label(frame, text="Density (0-1):").grid(row=1, column=0, sticky=tk.W)
density_entry = ttk.Entry(frame, width=7)
density_entry.grid(row=1, column=1)
density_entry.insert(0, "0.4")

directed_var = tk.BooleanVar()
directed_check = ttk.Checkbutton(frame, text="Directed Graph", variable=directed_var)
directed_check.grid(row=2, columnspan=2, sticky=tk.W)

generate_button = ttk.Button(frame, text="Generate Graph", command=generate_and_display_graph)
generate_button.grid(row=3, columnspan=2)

graph_display = tk.Text(frame, width=60, height=15)
graph_display.grid(row=4, columnspan=2, pady=10)

app.mainloop()
