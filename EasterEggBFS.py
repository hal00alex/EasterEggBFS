def bfs (graph, start, end):
    #BFS always uses queue
    queue = [(start, [start])]

    while stack:
        #remove vertex closest to start/ next node
        (vertex, edge) = stack.pop(0)

        #go through the edges related to the node 
        for next in graph[vertex] - set(edge):

            #stop if goal was reached 
            if (next == end):
                #make sure function includes the last node 
                yield edge + [next]
                #print (stack)
                #return stack
                
            #add to queue so while loop continues 
            else:
                queue.append((next, edge + [next]))

   

def main():
    
    #dictonary with set value so I can pop
    graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'Egg']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'Egg': set(['B', 'F'])}
    
    #call path function and print path 
    print (list(bfs (graph, 'A', 'Egg')))
    
main() 
         
