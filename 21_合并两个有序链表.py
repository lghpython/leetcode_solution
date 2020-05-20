# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return self.next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        tmp = ListNode(0)
        pre = tmp
        while l1 and l2:
            if l1.val <= l2.val:
                tmp.next = ListNode(l1.val)
                tmp = tmp.next
                l1 = l1.next
            else:
                tmp.next = ListNode(l2.val)
                tmp = tmp.next
                l2 = l2.next
        if l1:
            tmp.next = l1
        if l2:
            tmp.next = l2
        return pre.next

        """
        tmp = ListNode(0)
        pre = tmp
        while l1 or l2:
            if l1 and l2:
                if l1.val <= l2.val:
                    tmp.next = ListNode(l1.val)
                    tmp = tmp.next
                    l1 = l1.next
                else:
                    tmp.next = ListNode(l2.val)
                    tmp = tmp.next
                    l2 = l2.next
            elif l1 and not l2:
                tmp.next = ListNode(l1.val)
                tmp = tmp.next
                l1 = l1.next
            else:
                tmp.next = ListNode(l2.val)
                tmp = tmp.next
                l2 = l2.next
        return pre.next
        """


if __name__ == '__main__':

    m1 = ListNode(1)
    n1 = m1.next
    n1= ListNode(2)
    n1 = n1.next
    n1= ListNode(4)

    m2 = ListNode(2)
    n2 = m2.next
    n2 = ListNode(5)
    n2 = n2.next
    n2 = ListNode(6)
    sm = Solution()

    sm.mergeTwoLists(m1, m2)