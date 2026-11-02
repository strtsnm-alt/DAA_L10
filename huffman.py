chars = ['a', 'b', 'c', 'd', 'e', 'f']
freq = [5, 9, 12, 13, 16, 45]

nodes = [[freq[i], chars[i]] for i in range(len(chars))]

while len(nodes) > 1:
    nodes.sort(key=lambda x: x[0])
    
    left = nodes.pop(0)
    right = nodes.pop(0)
    
    parent_freq = left[0] + right[0]
    parent = [parent_freq, [left, right]]
    
    nodes.append(parent)

print("Final: ", nodes[0])
