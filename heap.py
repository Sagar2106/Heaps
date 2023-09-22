#!/usr/bin/env python
# coding: utf-8

import numpy as np
import sys

#Heap algorithm implementation
class min_heap:
    def __init__(self,max_size):
        self.max_size=max_size
        self.size=0
        self.heap = [0]*self.max_size
    
    def swap(self, n1, n2):
        temp=self.heap[n1]
        self.heap[n1] = self.heap[n2]
        self.heap[n2] = temp
      
    def parentindex(self,index):
        return (index-1)//2
    
    def leftindex(self,index):
        return (2*index+1)
    
    def rightindex(self,index):
        return (2*index+2)
    
    def parentcheck(self,index):
        return self.parentindex(index) >= 0
    
    def leftcheck(self,index):
        return self.leftindex(index) < self.size
    
    def rightcheck(self,index):
        return self.rightindex(index) < self.size

    def heapify_down(self):
        size=0
        while (self.leftcheck(size)):
            smallest_index = self.leftindex(size)
            if (self.rightcheck(size)):
                if self.heap[self.rightindex(size)] < self.heap[self.leftindex(size)]:
                    smallest_index = self.rightindex(size)
            if self.heap[size] < self.heap[smallest_index]:
                break
            else:
                self.swap(size,smallest_index)
            size=smallest_index
    
    def heapify_up(self,index):
        index= self.size - 1
        while (self.parentcheck(index) and self.heap[self.parentindex(index)] > self.heap[index]):
            self.swap(index,self.parentindex(index))
            index=self.parentindex(index)
    
    def push(self,data):
        if self.size==self.max_size:
            raise("Heap is full!")
        self.heap[self.size]=data
        self.size += 1
        self.heapify_up(self.size)

    def pop(self):
        if self.size==0:
            raise("Heap is empty!")
        data =  self.heap[0]
        self.heap[0] = self.heap[self.size-1]
        self.size -= 1
        self.heapify_down()
        return data
    
    def print_heap(self):
        for i in range(self.max_size):
            if i+1 > self.size:
                self.heap[i] = None
            print("Heap: ",self.heap[i])

#Reading and writing files taken as input from the terminal

with open(sys.argv[1], 'r') as fi, open (sys.argv[2], 'w') as fo:

        data = fi.read()
        myline = []
        popped = []        
        count=0
        heap_size = data.count("A") #Occurences of A = max_size of heap
        minheap=min_heap(heap_size)
        
        #reading the file one line at a time 
        for line in data.splitlines():
            myline.append(line)
            curr_line = myline[count].split(" ")
            
            #splitting current line with "space" as the divider and checking if the first word is A or E
            if curr_line[0] == 'A':
                temp=int(curr_line[1])
                minheap.push(temp)
            
            elif curr_line[0] == 'E':
                delete = minheap.pop()
                popped = np.append(popped,delete)
            count += 1
        
        #writing to the file taken from the terminal
        for line in popped:
            fo.write("%d" %line + "\n")

#Run the program as 
# python aoa_pa1.py "input_file_name" "output_file_name"