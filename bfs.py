from search import *
#abubakarasif3111@gmail.com
#https://github.com/Abubakar3111
#https://www.linkedin.com/in/abubakar-asif-b3b94021a/
#graph={'A':{'B','C'},'B':{'D','E'},'C':{'F','G'},'D':{},'E':{},'F':{},'G':{}}
#graph={'S':{'A','B','C'},'A':{'D','E'},'B':{'G'},'C':{'F'},'D':{'H'},'E':{'G'},'F':{'G'}}
graph = {'Abbottabad': set(['Mansehra', 'Haripur', 'Muree']),
'Mansehra':set(['Abbottabad', 'Attar Shisha', 'Besham']), 'Haripur': set(['Hassan Abdal', 'Swabi']), 
'Muree': set(['Islamabad', 'Muzzafar Abad']), 'Attar Shisha':set(['Mansehra', 'Naran', 'Muzzafar Abad']), 
'Besham':set(['Khwazakhela', 'Chilas']), 'Hassan Abdal': set(['Jehangira', 'Taxila']), 'Swabi':set(['Haripur', 'Jehangira']), 
'Islamabad':set(['Muree', 'Rawalpindi']), 'Muzzafar Abad': set(['Muree', 'Attar Shisha']), 
'Khwazakhela':set(['Besham', 'Mingora', 'Kalam']), 'Chilas':set(['Besham', 'Naran', 'Gilgit']),
'Jehangira':set(['Swabi', 'Hassan Abdal', 'Nowshera']), 'Taxila':set(['Hassan Abdal', 'Rawalpindi']), 
'Rawalpindi':set(['Islamabad', 'Taxila']), 'Mingora':set(['Nowshera', 'Khwazakhela']), 'Kalam':set(['Khwazakhela']), 
'Naran':set(['Attar Shisha', 'Chilas']), 'Gilgit':set(['chilas']), 'Nowshera':set(['Peshawar', 'Jehangira']), 
'Peshawar' :set(['Nowshera'])}
class Node():
    def __init__(self,state,parent=None,cost=0,heuristic=0):
        self.state=state
        self.parent=parent
        self.cost=cost
        self.heuristic=heuristic
    def __repr__(self):
        return repr(self.state)


def goal_test(state):
    if state==goal:
        return True
    else: 
        return False

    
def sucessors(state): 
    return graph[state]
    
    
def node_to_path(node): 
    path=[node.state]
    while node.parent != None: 
        node=node.parent
        path.append(node.state)
    path.reverse()
   #print(path)
    return path

def bfs(initial):
    frontier=Queue()
    inode=Node(initial)
    frontier.push(inode)
    explored={initial}
    while  frontier.empty:
       print(frontier)
       print('hello')
       current_node=frontier.pop()
       current_state=current_node.state
       
       if goal_test(current_state):
           print(node_to_path(current_node))
           return current_node
       for child in sucessors(current_state):
           if child not in explored:
              frontier.push(Node(child,current_node))
              explored.add(child)
    return None       
        
            
    
    
start='Abbottabad'
goal='Naran'
bfs(start)
