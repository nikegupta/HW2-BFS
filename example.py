from search import graph
import networkx as nx
import matplotlib.pyplot as plt

def main():
    g = graph.Graph('data/citation_network.adjlist')
    print(g.bfs('Lani Wu','Tony Kapra'))

    # #to visualize the graph 
    # plt.figure(figsize=(128,128))
    # nx.draw_networkx(g.graph)
    # plt.savefig('example_graph_full.png',)

if __name__ == "__main__":
    main()