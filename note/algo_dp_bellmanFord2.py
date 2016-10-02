"""
The Bellman-Ford algorithm
I modified this code from https://gist.github.com/joninvski/701720, 
to satisfy the vanlia problem
Forgive me on that

Since this algorihm is the same as the one on wikipedia
https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm
"""

# Step 1: For each node prepare the destination and predecessor
def initialize(graph, source):
    d = {} # Stands for destination
    p = {} # Stands for predecessor
    for node in graph:
        d[node] = float('Inf') # We start admiting that the rest of nodes are very very far
        p[node] = None
    d[source] = 0 # For the source we know how to reach
    return d, p

def relax(node, neighbour, graph, d, p):
    # If the distance between the node and the neighbour is lower than the one I have now
    if d[neighbour] > d[node] + graph[node][neighbour]:
        # Record this lower distance
        d[neighbour]  = d[node] + graph[node][neighbour]
        p[neighbour] = node

def bellman_ford(graph, source):
    d, p = initialize(graph, source)
    for i in range(len(graph)-1): #Run this until is converges
        for u in graph:
            for v in graph[u]: #For each neighbour of u
                relax(u, v, graph, d, p) #Lets relax it

    # Step 3: check for negative-weight cycles
    for u in graph:
        for v in graph[u]:
            '''
            Discover:
                If the shortest path reported is less than the original edge
                that's mean you can make the shortest path even shorter
            '''            
            try: 
                assert d[v] <= d[u] + graph[u][v]
            except AssertionError:
                print("UNSAFE AT ANY SPEED",end="")     
                return None,None

    for k in p:
        '''
        Discover: 
            Except the planet 1, 
            if the value is None, 
            that's mean planet 1 can't reach it
        '''        
        if k != 1:                
            if p[k] is None:
                print("OUT",end="")
                return None,None
                    
    return d, p

def begin():
    testCase = int(input())
    graph = {}
    for _ in range(testCase):
        vs,es = map(int,input().split(' '))                    
        for v in range(1,vs+1):
            graph[v] = {}
        for _ in range(es):
            u,v,w = map(int,input().split(' '))
            graph[u][v] = w
        d, p = bellman_ford(graph, 1)        

        if (d) is not None and (p) is not None:            
            for k,v in d.items():
                print(v,end=" ")  
                                          
        print()
if __name__ == '__main__': 
    begin()