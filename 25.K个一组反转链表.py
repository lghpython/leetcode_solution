# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        zero = ListNode(0)
        zero.next = head
        tail = zero
        pre = zero
        count = 0
        while tail:
            count += 1
            tail = tail.next
            if not tail: break
            if count % k == 0:
                head = pre.next
                # 当前指针插入tail后面
                while pre.next != tail:
                    cur = pre.next
                    pre.next = cur.next
                    cur.next = tail.next
                    tail.next = cur
                pre = head
                tail = head
        return zero.next

if __name__ == '__main__':
    l = ListNode(1)
    c = l.next
    c = ListNode(2)
    c = c.next
    c = ListNode(3)
    c.next = ListNode( 4)
    c = c.next
    c.next = ListNode(5 )
    s= Solution()
    print(s.reverseKGroup(l,3))
