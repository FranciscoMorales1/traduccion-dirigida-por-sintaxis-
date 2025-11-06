from graphviz import Digraph

def graph_ast(node):
    dot = Digraph(comment="AST", format="png")
    _add_nodes(dot, node)
    dot.render("AST_output", view=False)  # Genera AST_output.png
    return "AST_output.png"

def _add_nodes(dot, node, parent_id=None):
    current_id = id(node)
    
    if node.value is not None:
        label = f"{node.op}\\n{node.value}"
    else:
        label = node.op
    
    dot.node(str(current_id), label)

    if parent_id is not None:
        dot.edge(str(parent_id), str(current_id))

    if node.left:
        _add_nodes(dot, node.left, current_id)
    if node.right:
        _add_nodes(dot, node.right, current_id)
