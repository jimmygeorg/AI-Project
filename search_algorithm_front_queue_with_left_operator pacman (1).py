""" ----------------------------------------------------------------------------
******** Search Code for DFS  and other search methods
******** (expanding front and extending queue)
******** author:  AI lab
********
******** Κώδικας για DFS και άλλες μεθόδους αναζήτησης
******** (επέκταση μετώπου και διαχείριση ουράς)
******** Συγγραφέας: Εργαστήριο ΤΝ
"""

import copy

import sys 
sys.setrecursionlimit(10**6) 

""" Helper functions for checking operator's conditions """

#def can_eat(state):
      

#def can_move_right(state):
    

def can_move_left(state):
    return not state[0][0]=='p'


""" Operator function: eat, move right, move left """

#def eat(state):
    

#def move_right(state):
    

def move_left(state):
    if can_move_left(state):
        for i in range(len(state)):
            if state[i][0]=='p':
                state[i][0]=''
                state[i-1][0]='p'
                return state
    else:
        return None

""" Function that checks if current state is a goal state """

#def is_goal_state(state):
    

""" Function that finds the children of current state """

def find_children(state):
    children=[]
    
    left_state=copy.deepcopy(state)
    child_left=move_left(left_state)
    

    if not child_left==None:
        children.append(child_left)  
        
    
    return children


""" ----------------------------------------------------------------------------
**** FRONT
**** Διαχείριση Μετώπου
"""

""" ----------------------------------------------------------------------------
** initialization of front
** Αρχικοποίηση Μετώπου
"""

def make_front(state):
    return [state]

""" ----------------------------------------------------------------------------
**** expanding front
**** επέκταση μετώπου    
"""

def expand_front(front, method):  
    if method=='DFS':        
        if front:
            print("Front:")
            print(front)
            node=front.pop(0)
            for child in find_children(node):     
                front.insert(0,child)
    
    """
    #elif method=='BFS':
    """
    #elif method=='BestFS':
    #else: "other methods to be added"        
    
    return front

""" ----------------------------------------------------------------------------
**** QUEUE
**** Διαχείριση ουράς
"""

""" ----------------------------------------------------------------------------
** initialization of queue
** Αρχικοποίηση ουράς
"""

def make_queue(state):
    return [[state]]

""" ----------------------------------------------------------------------------
**** expanding queue
**** επέκταση ουράς
"""

def extend_queue(queue, method):
    if method=='DFS':
        print("Queue:")
        print(queue)
        node=queue.pop(0)
        queue_copy=copy.deepcopy(queue)
        children=find_children(node[-1])
        for child in children:
            path=copy.deepcopy(node)
            path.append(child)
            queue_copy.insert(0,path)
    
    #elif method=='BFS':
    #elif method=='BestFS':
    #else: "other methods to be added" 
    
    return queue_copy
            
""" ----------------------------------------------------------------------------
**** Problem depending functions
**** ο κόσμος του προβλήματος (αν απαιτείται) και υπόλοιπες συναρτήσεις σχετικές με το πρόβλημα

  #### to be  added ####
"""

""" ----------------------------------------------------------------------------
**** Basic recursive function to create search tree (recursive tree expansion)
**** Βασική αναδρομική συνάρτηση για δημιουργία δέντρου αναζήτησης (αναδρομική επέκταση δέντρου)
"""
#def find_solution(front, queue, closed, method):
def find_solution(front, queue, closed, goal, method):
       
    if not front:
        print('No solution')
    
    elif front[0] in closed:
        new_front=copy.deepcopy(front)
        new_front.pop(0)
        new_queue=copy.deepcopy(queue)
        new_queue.pop(0)
        find_solution(new_front, new_queue, closed, goal, method)
    
    #elif is_goal_state(front[0]):
    elif front[0]==goal:
        print('This is the solution: ')
        print(queue[0])
    
    else:
        closed.append(front[0])
        front_copy=copy.deepcopy(front)
        front_children=expand_front(front_copy, method)
        queue_copy=copy.deepcopy(queue)
        queue_children=extend_queue(queue_copy, method)
        closed_copy=copy.deepcopy(closed)
        find_solution(front_children, queue_children, closed_copy, goal, method)
	#find_solution(front_children, queue_children, closed_copy, method)
        
        
"""" ----------------------------------------------------------------------------
** Executing the code
** κλήση εκτέλεσης κώδικα
"""
          
def main():
    
    initial_state=[['','d'],['','f'],['p',''],['',''],['','f'],['','']]   
    goal=[['',''],['',''],['',''],['',''],['p',''],['','']]
    """ ----------------------------------------------------------------------------
    **** πρέπει να οριστεί η is_goal_state, καθώς δεν είναι μόνο μια η τελική κατάσταση
    """
   
    method='DFS'
    
    """ ----------------------------------------------------------------------------
    **** starting search
    **** έναρξη αναζήτησης
    """
    find_solution(make_front(initial_state), make_queue(initial_state), [], goal, 'DFS')
    #find_solution(make_front(initial_state), make_queue(initial_state), [], 'DFS')

        

if __name__ == "__main__":
    main()