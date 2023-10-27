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
    def mergeTwoLists(self, list1, list2):
        node_1 = list1.head
        node_2 = list2.head
        if node_1.val > node_2.val:
            merged_list = ListNode(node_2.val)
            node_2 = node_2.next
        else:
            merged_list = ListNode(node_1.val)
            node_1 = node_1.next

        while node_1.next is not None and node_2.next is not None:
            if node_1.val > node_2.val:
                merged_list.next = ListNode(node_2.val)
                merged_list.next
                node_2 = node_2.next
            elif node_1.val < node_2.val:
                merged_list.next = ListNode(node_1.val)
                merged_list.next
                node_1 = node_1.next
            else:
                merged_list.next = ListNode(node_1.val)
                merged_list.next
                merged_list.next = ListNode(node_2.val)
                merged_list.next
                node_1 = node_1.next
                node_2 = node_2.next
        return merged_list

if __name__ == '__main__':
    # Initiate linked list
    list_1 = [1,2,4]
    llist_1 = LinkedList()
    llist_1.createList(head=list_1)

    list_2 = [1,3,4]
    llist_2 = LinkedList()
    llist_2.createList(head=list_2)


    obj = Solution()
    print(obj.mergeTwoLists(list1=llist_1, list2=llist_2))

