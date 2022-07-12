import networkx as nx

node = nx.nx_agraph.read_dot("roadmap.dot")

print(node.nodes["london"])

"""
output:

Traceback (most recent call last):
  File "E:\Programacao\PythonDjango\Python-Stacks-Queues\python\graph.py", line 3, in <module>
    node = nx.nx_agraph.read_dot("roadmap.dot")
  File "E:\Programacao\PythonDjango\Python-Stacks-Queues\venv\lib\site-packages\networkx\drawing\nx_agraph.py", line 205, in read_dot
    raise ImportError(
ImportError: read_dot() requires pygraphviz http://pygraphviz.github.io/
"""
