import pandas as pd
from graphviz import Graph
import argparse
import os
import shutil

def clear_output_directory():
    """Clear the contents of the /output directory."""
    output_dir = 'output'
    if os.path.exists(output_dir):
        # Remove all files in the output directory
        shutil.rmtree(output_dir)
    # Recreate the output directory
    os.makedirs(output_dir)

def generate_graphviz(df):
    """Generate Graphviz graph and save it as an SVG file in the output directory."""
    graph = Graph(format='svg', graph_attr={'rankdir': 'LR'})

    # Add nodes to the Graphviz graph for each item in the CSV file
    nodes = set(df['dependency']).union(set(df['dependent']))
    for node in nodes:
        graph.node(node)

    # Add edges to the Graphviz graph for each dependency relationship in the CSV file
    for _, row in df.iterrows():
        graph.edge(row['dependency'], row['dependent'])

    # Generate the SVG file in the output directory
    output_path = 'output/DAG'
    graph.render(output_path, view=True)
    print(f"Graphviz SVG output saved to {output_path}.svg")


def generate_mermaid(df):
    """Generate Mermaid diagram and save it as a Markdown file in the output directory."""
    mermaid_code = "```mermaid\ngraph LR\n"
    
    # Add nodes and edges for each dependency relationship in the CSV file
    for _, row in df.iterrows():
        mermaid_code += f"    {row['dependency']} --> {row['dependent']}\n"
    
    mermaid_code += "```"

    # Save the Mermaid diagram to a Markdown file in the output directory
    output_path = 'output/DAG.md'
    with open(output_path, 'w') as f:
        f.write(mermaid_code)
    print(f"Mermaid Markdown output saved to {output_path}")


if __name__ == "__main__":
    # Create the argument parser
    parser = argparse.ArgumentParser(description='Generate a graph from a CSV file using Graphviz or Mermaid.')
    
    # Add the arguments
    parser.add_argument('-i', type=str, required=True, help='Path to the input CSV file')
    parser.add_argument('-m', type=str, required=True, help='Output mode (graphviz or mermaid)')

    # Parse the arguments
    args = parser.parse_args()

    input_csv_path = args.i
    output_mode = args.m.lower()

    # Check if the input file exists
    if not os.path.exists(input_csv_path):
        print(f"Error: Input file {input_csv_path} does not exist.")
        exit(1)

    # Clear the /output directory
    clear_output_directory()

    # Load the CSV file into a pandas DataFrame
    df = pd.read_csv(input_csv_path)

    # Generate output based on the specified mode
    if output_mode == 'graphviz':
        generate_graphviz(df)
    elif output_mode == 'mermaid':
        generate_mermaid(df)
    else:
        print("Error: Output mode must be either 'graphviz' or 'mermaid'")
        exit(1)