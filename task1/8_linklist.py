class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None 

   
  
def arr_to_list(arr):
        head=Node(arr[0])
        tmp=head
        for i in arr[1:]:
            tmp.next=Node(i)
            tmp=tmp.next
        return head


def printlst(h):
    while h!=None:
        print(h.data)
        h=h.next

a=list(map(int, input().split()))

lst=arr_to_list(a)
printlst(lst)