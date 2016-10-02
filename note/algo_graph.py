import time
'''
The following demonstration was referenced from Python Software Foundation 
https://www.python.org/doc/essays/graphs/
'''

'''
Simple directed Graph representation
A -> B
|    ^
v    |
C -> D
'''
graph = {'A': ['C','B'],
         'B': [''],
         'C': ['D'],
         'D': ['B']}

assert('C' in graph['A'])
assert('B' in graph['A'])
assert('' in graph['B'])
assert('D' in graph['C'])
assert('B' in graph['D'])

'''
The following algorithm implemented by brutal-force, 
because it's the most beautiful thing in the world
Finding the possible path between the node of start and end
and fill in the graph, given the path is optionally blank
'''
def findPath (graph, start, end, path=[]):
    path = path + [start]

    if start == end:
        return path #Are you playing wiht me bro?

    if not start in graph:
      return None #Are you still playing with me bro?

    '''
    Begin brute force here
    Scanning each element in the list from 
    the given start node
    '''
    for node in graph[start]:
        if node not in path: #Have not recorded this path before
            #New shit homie
            newpath = findPath(graph, node, end, path)
            if newpath:
                return newpath
            return None
            
start = time.time()
print(findPath (graph, 'A', 'D'))
print(time.time() - start)


















