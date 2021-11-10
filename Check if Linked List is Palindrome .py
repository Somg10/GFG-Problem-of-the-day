class Solution:
    
    def reverseList(self, temp):  
        current = temp;  
        prevNode = None;  
        nextNode = None;  
          
        while(current != None):  
            nextNode = current.next;  
            current.next = prevNode;  
            prevNode = current;  
            current = nextNode;  
        return prevNode;  
        
    def getSize(self, head):
        count = 0
        curr_node = head
        while curr_node:
            count +=1
            curr_node = curr_node.next
        return count
    
    def isPalindrome(self, head):
        #code here
        current = head;  
        flag = True; 
        s = self.getSize(head)
        mid = (s//2) if(s%2 == 0) else ((s+1)//2);   
        for i in range(1, mid):  
            current = current.next;  
        revHead = self.reverseList(current.next);  
    
        while(head != None and revHead != None):  
            if(head.data != revHead.data):  
                flag = False;  
                break;  
                  
            head = head.next;  
            revHead = revHead.next;   
        return flag

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node 

if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        n = int(input())
        a = LinkedList() # create a new linked list 'a'.
        nodes_a = list(map(int, input().strip().split()))
        for x in nodes_a:
            a.append(x)  # add to the end of the list

        if Solution().isPalindrome(a.head):
            print(1)
        else:
            print(0)
# } Driver Code Ends
