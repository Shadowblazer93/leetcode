# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def spiralMatrix(self, m, n, head):
        matrix = [[-1 for i in range(n)] for i in range(m)]
        x,y=0,0
        dx,dy=1,0

        while head:
            matrix[y][x]=head.val
            if x+dx<0 or x+dx>=n or y+dy<0 or y+dy>=m or matrix[y+dy][x+dx]!=-1: dx, dy = -dy, dx
            x,y=x+dx,y+dy
            head = head.next

        return matrix