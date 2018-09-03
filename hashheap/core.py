#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: AlexHtZhang

''' 
HashHeap is a datastructure that supports O(logn) remove, O(1) top, O(logn) pop, O(logn) push with regarding to time complexity. 

This program was developed and tested under following environments:
python: 2.7.14.final.0
python-bits: 64
OS: Darwin
OS-release: 16.7.0
machine: x86_64
processor: i386
byteorder: little
LC_ALL: None
LANG: en_US.UTF-8
LOCALE: None.None
'''
class HashHeap:

    '''HashHeap is a datastructure that supports O(logn) remove, O(1) top, O(logn) pop, O(logn) push with regarding to time complexity. 
    '''
    
    def __init__(self, desc=False):
        '''Initalize hashheap.  
        :input: desc, ture for min heap, flase for max heap.  
        :type: bool 
        '''
        assert isinstance(desc, bool) 
        self.hash = dict()
        self.heap = []
        self.desc = desc
        
    @property
    def size(self):
        '''Get the size of the hashheap.  
        :input: None
        :type: None 
        :return: Size of the hashheap
        :type: int
        '''
        return len(self.heap)
        
    def push(self, item):
        '''push item into hashheap.  
        :input: item
        :type: type of item 
        :return: None
        :type: None
        '''
        self.heap.append(item)
        self.hash[item] = self.size - 1
        self._sift_up(self.size - 1)
        
    def pop(self):
        '''Remove and return the top of the HashHeap.  
        :input: None
        :type: None 
        :return: item in hashheap
        :type: type of item in hashheap
        '''
        item = self.heap[0]
        self.remove(item)
        return item
    
    def top(self):
        '''Return the top of the HashHeap without remove it.  
        :input: None
        :type: None 
        :return: item in hashheap
        :type: type of item in hashheap
        '''
        return self.heap[0]
        
    def remove(self, item):
        '''remove element in HashHeap in O(logn) time complexity.  
        :input: param
        :type: dict 
        :return: None
        :type: None
        '''
        if item not in self.hash:
            return
            
        index = self.hash[item]
        self._swap(index, self.size - 1)
        
        del self.hash[item]
        self.heap.pop()
        
        if index < self.size:
            self._sift_up(index)
            self._sift_down(index)

    def _smaller(self, left, right):
        return right < left if self.desc else left < right

    def _sift_up(self, index):
        while index != 0:
            parent = index // 2
            if self._smaller(self.heap[parent], self.heap[index]):
                break
            self._swap(parent, index)
            index = parent
    
    def _sift_down(self, index):
        if index is None:
            return
        while index * 2 < self.size:
            smallest = index
            left = index * 2
            right = index * 2 + 1
            
            if self._smaller(self.heap[left], self.heap[smallest]):
                smallest = left
                
            if right < self.size and self._smaller(self.heap[right], self.heap[smallest]):
                smallest = right
                
            if smallest == index:
                break
            
            self._swap(index, smallest)
            index = smallest
        
    def _swap(self, i, j):
        elem1 = self.heap[i]
        elem2 = self.heap[j]
        self.heap[i] = elem2
        self.heap[j] = elem1
        self.hash[elem1] = j
        self.hash[elem2] = i