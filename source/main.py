#!utf-8
import yaml
from graphviz import Digraph

G = Digraph(format="png")
G.attr("node", shape="box", width="1", color="orange")
with open("process.yml") as f:
    dict=yaml.load(f)
    print(dict)
    G.node("inpute")
    G.render("order_state")