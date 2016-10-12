'''
iter nested loop with dependency in one line
'''
b = [["Apple","Banana","Cat"],["Apple","Scope","Baby"]]
def nested_original(b):
    result = set()
    for subList in b:
        for token in subList:
            result.add(token)
    return sorted(result)

def nested_oneLine(b):
    return sorted(set(token for subList in b for token in subList))
    
assert(nested_oneLine(b) == nested_original(b))
