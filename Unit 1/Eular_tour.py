# Find Eulerian Tour
#
# Write a function that takes in a graph
# represented as a list of tuples
# and return a list of nodes that
# you would follow on an Eulerian Tour
#
# For example, if the input graph was
# [(1, 2), (2, 3), (3, 1)]
# A possible Eulerian tour would be [1, 2, 3, 1]

def find_eulerian_tour(graph):
    # your code here
    list = []
    list1 = []
    startnode = graph[0][0]
    print graph
    
    freq = calculate_frequecy(graph)
    print freq
    even = odd = 0
    
    for i in range(0, len(freq)):
        if freq[i][1] % 2 == 0:
            even = even + 1
        else:
            print "odd"
            odd = odd + 1
    
    if odd > 0:
        print "Tour not possible"
    else:
        ind = 0
        x = y = 0
        for a in range(0, len(freq)):
            if freq[a][1] == 2:
                ind = freq[a][0]
                break
        
        for k in range(0, len(graph)):
            if graph[k][0] == ind:
                x = k
                y = 0
                break
            elif graph[k][1] == ind:
                x = k
                y = 1
                break
                
        graph, list = traverse(graph, len(freq), x, y)
        print graph, list
        while len(graph) > 0:
            index1, index2, index3 = check(graph, list)
            print index1, index2, index3
            graph, list1 = traverse(graph, len(freq), index1, index2)
            print graph, list1
            
            for k in range(1, len(list1)):
                list.insert(index3 + 1, list1[len(list1) - k])
            print list
        
    return list

def traverse(graph, length, index1, index2):
    list = []
    list.append(graph[index1][index2])
    
    for i in range(0, length):
        j = list[len(list) - 1]
        for k in range(0, len(graph)):
            if graph[k][0] == j:
                list.append(graph[k][1])
                graph.remove(graph[k])
                break
            elif graph[k][1] == j:
                list.append(graph[k][0])
                graph.remove(graph[k])
                break
                

    return graph, list
        
def check(graph, list):
    for i in range(0, len(list)):
        for j in range(0, len(graph)):
            if list[i] == graph[j][0]:
                return j, 0, i
            elif list[i] == graph[j][1]:
                return j, 1, i
    
    
def calculate_frequecy(graph):
    list = []
    for i in range(0, len(graph)):
        x = graph[i][0]
        y = graph[i][1]
        xfound = 0
        yfound = 0
        for j in range(0, len(list)):
            if x == list[j][0]:
                list[j][1] = list[j][1] + 1
                xfound = 1
            elif y == list[j][0]:
                list[j][1] = list[j][1] + 1
                yfound = 1
        if xfound == 0:
            list.append([x, 1])
        if yfound == 0:
            list.append([y, 1])
    return list
        
        
        
        
find_eulerian_tour([(8, 16), (8, 18), (16, 17), (18, 19), (3, 17), (13, 17), (5, 13), (3, 4), (0, 18), (3, 14), (11, 14), (1, 8), (1, 9), (4, 12), (2, 19), (1, 10), (7, 9), (13, 15), (6, 12), (0, 1), (2, 11), (3, 18), (5, 6), (7, 15), (8, 13), (10, 17)])

