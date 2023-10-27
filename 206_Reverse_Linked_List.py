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
    def reverseList(self, head):
        current_node = head.next
        head.next = None
        new_list = head
        while current_node.next is not None:
            next_values = current_node.next
            inter = ListNode(val=current_node.val)
            inter.next = new_list
            new_list = inter
            current_node = next_values
        inter = ListNode(val=current_node.val)
        inter.next = new_list
        new_list = inter
        return new_list


if __name__ == '__main__':
    # Initiate linked list
    vals = [1]
    llist = LinkedList()
    llist.createList(head=vals)

    obj = Solution()

    print(obj.reverseList(head=llist.head))

    # Add node
