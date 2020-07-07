# 用两个链表存放两个数，输出两个数相加后的数，同样要用链表显示。
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# @param l1 ListNode类
# @param l2 ListNode类
# @return ListNode类
class Solution:
    def addTwoNumbers(self , l1 , l2 ):
        node1, node2, carry = l1, l2, 0
        head, cur = None, None
        while node1 is not None or node2 is not None:
            if node1 is None:
                cal = node2.val + carry
            elif node2 is None:
                cal = node1.val + carry
            else:
                cal = node1.val + node2.val + carry
            carry = cal//10
            b = cal%10
            head, cur = self.add_node(head, cur, b)
            if node1 is not None: node1 = node1.next
            if node2 is not None: node2 = node2.next
        # carry是进位，这里一定要注意，有可能全加完了，但是有多余进位
        if carry > 0:
            head, cur = self.add_node(head, cur, carry)
        return head

    def add_node(self, head, cur, value):
        if head is None:
            cur = ListNode(value)
            head = cur
        else:
            node = ListNode(value)
            cur.next = node
            cur = node
        return head, cur

    def display(self, node_list):
        node = node_list
        while node is not None:
            print(node.val)
            node = node.next
        print('='*10)

if __name__ == '__main__':
    list1 = [2, 4, 3]
    list2 = [5, 6, 4]
    head1, head2, node1, node2 = None, None, None, None
    for value in list1:
        if head1 is None:
            node1 = ListNode(value)
            head1 = node1
        else:
            node = ListNode(value)
            node1.next = node
            node1 = node

    for value in list2:
        if head2 is None:
            node2 = ListNode(value)
            head2 = node2
        else:
            node = ListNode(value)
            node2.next = node
            node2 = node
    s = Solution()
    s.display(head1)
    s.display(head2)
    ans = s.addTwoNumbers(head1, head2)
    s.display(ans)




