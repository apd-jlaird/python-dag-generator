# Python DAG Generator
> A simple Python application to generate DAGs from a CSV

## Instructions
1. Ensure GraphViz is installed on your computer:
   - Mac: https://formulae.brew.sh/formula/graphviz
   - Windows: https://graphviz.org/download/
2. Create and activate a virtual environment and install the required packages using pip:
    - `pip install -r requirements.txt`
3. Replace `input.csv` with your source file
4. Run the Python script:
    - `python main.py`

## Example Input
Create a CSV file defining the dependency relationships in the following structure: 

| dependency | dependent |
| --- | --- |
| a | b |
| a | c |
| b | d |
| c | d |
| a | e |
| c | e |
| d | e |

## Example Output
![DAG](images/DAG.svg)