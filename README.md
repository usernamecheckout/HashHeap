HashHeap
=======================
Python's implementation of java's TreeMap. 
Hope similar data structure can be added to python offical library.


Install 
-----

-   Install via `$ pip install HashHeap` .

How to use
-----
-   `$ from HashHeap import HashHeap` .


    def __init__(self, desc=False):
        '''Initalize hashheap.  
        :input: desc, ture for min heap, flase for max heap.  
        :type: bool 
        '''
        
    def size(self):
        '''Get the size of the hashheap.  
        :input: None
        :type: None 
        :return: Size of the hashheap
        :type: int
        '''
        
    def push(self, item):
        '''push item into hashheap.  
        :input: item
        :type: type of item 
        :return: None
        :type: None
        '''
        
    def pop(self):
        '''Remove and return the top of the HashHeap.  
        :input: None
        :type: None 
        :return: item in hashheap
        :type: type of item in hashheap
        '''
    
    def top(self):
        '''Return the top of the HashHeap without remove it.  
        :input: None
        :type: None 
        :return: item in hashheap
        :type: type of item in hashheap
        '''
        
    def remove(self, item):
        '''remove element in HashHeap in O(logn) time complexity.  
        :input: param
        :type: dict 
        :return: None
        :type: None
        '''


And ...
-------

Pull requests are encouraged!
