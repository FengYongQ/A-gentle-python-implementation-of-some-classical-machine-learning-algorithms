def find_categoryCART(row, tree_node):
    childNode = tree_node.children
    if tree_node.feature == None:
        row['supervised'] = tree_node.category
        return
    else:
        node = childNode.get(row[tree_node.feature])
        if node == None:
            node = childNode.get(list(childNode.keys())[1])
        find_categoryCART(row, node)
        return

def predict(test_data, tree_node):
    num = len(test_data)
    test_data['supervised'] = None
    for i in range(num):
        row = test_data.loc[i]
        find_categoryCART(row, tree_node)
        test_data.loc[i]['supervised'] = row['supervised']