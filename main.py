import pandas as pd
from graphviz import Graph

# Install Graphviz using pip
# pip install graphviz

# Create a CSV file with your dependencies
# The CSV file should contain two columns: 'dependency' and 'dependent'
# Each row represents a dependency relationship between two items

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('input/input.csv')

# Create a Graphviz graph object
graph = Graph(format='svg', graph_attr={'rankdir': 'LR'})

# Add nodes to the graph for each item in the CSV file
nodes = set(df['dependency']).union(set(df['dependent']))
for node in nodes:
    graph.node(node)

# Add edges to the graph for each dependency relationship in the CSV file
for _, row in df.iterrows():
    graph.edge(row['dependency'], row['dependent'])

# Generate an SVG file from the graph
graph.render('output/DAG', view=True)