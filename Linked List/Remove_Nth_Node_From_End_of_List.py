# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

    p1 = p2 = head
    for i in range(n):
        p2 = p2.next

    # Handles edge cases like length 1,2 linked lists.
    if p2 is None:
        head = head.next
        return head
    
    while p2.next is not None:
        p1 = p1.next
        p2 = p2.next

    p1.next = p1.next.next
    return head
    

def main():
    removeNthFromEnd()

if __name__ == "__main__":
    main()