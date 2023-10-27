class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def createList(self, head):
        self.head = ListNode(val=head[0])
        last_node = self.head
        for i in range(1, len(head)):
            current_node = ListNode(val=head[i])
            last_node.next = current_node
            last_node = last_node.next
        return self.head

    def __str__(self):
        string_list = ''
        current_node = self.head
        string_list += f"{current_node.val}"
        while current_node.next is not None:
            current_node = current_node.next
            string_list += f"--->{current_node.val}"
        return string_list




class Solution:
    def deleteDuplicates(self, head):
        current_node = head.head
        while current_node.next is not None:
            if current_node.val == current_node.next.val:
                current_node.next = current_node.next.next
            current_node = current_node.next
            if current_node is None:
                break


if __name__ == '__main__':
    vals = [1,1,2,3,3]
    head = LinkedList()
    head.createList(vals)

    obj = Solution()
    print(obj.deleteDuplicates(head))
