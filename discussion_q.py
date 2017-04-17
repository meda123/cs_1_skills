
# Discussions and questions:

""""
RUNTIME

1. What determines the workdload of figuring out whether your box of animal
crakers contains an elephant? 

Runtime complexity determines the workload of figuring out whether my box of 
animal crackers contains an elephant. Since the worst case scenario is always assumed 
in calculating runtime, we can assume that an elephant is not in the box of 
animal crakers. As such, one would have to inspect each cracker in the box of
animal crackers box, thus the runtime would be O(n)


2. Order the following runtimes in descending order of efficiency (that is, 
fastest runtimes first, slowest last) as n approaches infinity:

O(1)
O(log n)
O(n)
O(n log n)
O(n^2)
O(2^n)
"""


""" 
STACKS AND QUEUES 

In the following cases, would a stack or queue be a more appropriate data structure? 

1) The process of loading and unloading pallets onto a flatbed truck? 
Stack, since pallets are generally unloaded using the LIFO method 

2) Putting bottle caps on bottles of beer as they roll down an assembly line
Queue, since the bear that first reached the assembly line gets a cap (FIFO)

3)Calculating the solution to this mathematical expression: 2 + (7 * 4) - (3 / 2)
Stack, we're taking advantage of the LIFO aspect of stacks (the older items are
at the bottom) so when we're trying to match parentheses, we're given the nearest
to match. 
"""

""" 
LINKED LISTS 

Question 1)

a) Which are the nodes? Apple, Berry, and Cherry are nodes 

b) What is the data for each node? Apple (string), Berry (string), and Cherry (string)

c) Where is the head/tail? Apple is the head and there is no tail because it has
not been assingned. 


Question 2) What’s the difference between doubly- and singly-linked lists?
Single linked lists allows for single direction travel (next) whereas a doubly-linked
list allows for double direction travel (next and previoux)


Question 3) Why is it faster to append to a linked list if we keep track of 
the tail as an attribute? If the tail is not clearly labeled, rather than appending
to the tail node, we would have to traverse the entire linked list to figure out 
if we are indeed at the last node. 
"""



""" Trees 
1) In search of burritos BFS order: 
    Food
    Italian, Indian, Mexican 
    Indian, Mexican, Lasagna, Pizza, 
    Mexican, Lasagna, Pizza, Tikka Masala, Saag
    Lasagna, Pizza, Tikka Masala, Saag, Burritos, Tacos, Enchillada
    Pizza, Tikka Masala, Saag, Burritos, Tacos, Enchillada 
    Tikka Masala, Saag, Burritos, Tacos, Enchillada, Thin Crust, Chicago-style, NY style
    Saag, Burritos, Tacos, Enchillada, Thin Crust, Chicago-style, NY style 
    Burritos, Tacos, Enchillada, Thin Crust, Chicago-style, NY style 
    -- Pop Burrito and we've found it!! -- 

2) In search of Chicago-style in DFS:
    Food 
    Italian
    Lasagna, Pizza
    Pizza, thin crust, chicago-style, NY style 
    Thin crust, chicago-style, NY style 
    Chicago-style, NY style
    -- Pop Chicago-style and we've found it!! -- 

"""










