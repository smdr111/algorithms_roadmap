#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  4 13:31:21 2025

@author: samandaroripov
"""

class Node:
    
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList :
    
    def __init__(self):
        self.head=None
        
    
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
    
    
    def push(self,new_data):
        new_node = Node(new_data)
        
        new_node.next = self.head
        
        self.head = new_node
    
    
    def insertAfter(self,prev_node,new_data):
        
        if prev_node is None:
            return ('Node does not exist')
        
        new_node = Node(new_data)
        
        new_node.next = prev_node.next
        
        prev_node.next = new_node
    
    
    def append(self,new_data):
        
        new_node = Node(new_data)
        
        if self.head is None:
            
            self.head = new_node
            
            return
        
        last = self.head
        
        while last.next:
            
            last = last.next
        
        last.next = new_node
    def deleteNode(self,key):
        
        temp = self.head
        
        if (temp and temp.data == key):
            self.head = temp.next
            temp=None
            return
        
        while temp:
            if temp.data==key:
                break
            
            prev = temp
            temp = temp.next
        if temp==None:
            return
        prev.next = temp.next
        temp=None
        
            
    
           
    
llist = LinkedList()

llist.head = Node('Monday')
tuesday = Node('Tuesday')
wednesday = Node('Wednesday')

llist.head.next = tuesday
tuesday.next = wednesday

# llist.printList()

llist.push('Sunday')
# llist.printList()

llist.insertAfter(llist.head.next, 'Monday Night')
# list.printList()

llist.append('Thursday')
# llist.printList()

llist.deleteNode('Monday Night')
llist.printList()























