# https://leetcode.com/problems/odd-even-linked-list/
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        odds = ListNode(-1)
        evens = ListNode(-1)
        curodd = odds
        curev = evens
        ctr = 1
        while head:
            if ctr%2 == 1:
                curodd.next, curodd = head, head
            else:
                curev.next, curev = head, head
            ctr += 1
            head = head.next
        curodd.next = evens.next
        if curev:
            curev.next = None
        return odds.next