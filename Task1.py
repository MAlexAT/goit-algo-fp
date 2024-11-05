# Використовуємо початкову реалізацію однозв'язного списку, надану в конспекті, і додаємо нові функції.

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # Функція реверсування однозв'язного списку
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    # Функція сортування однозв'язного списку (сортування вставками)
    def sort(self):
        if self.head is None or self.head.next is None:
            return

        sorted_list = None
        current = self.head
        while current:
            next_node = current.next
            sorted_list = self._sorted_insert(sorted_list, current)
            current = next_node
        self.head = sorted_list

    def _sorted_insert(self, sorted_head, new_node):
        if sorted_head is None or new_node.data < sorted_head.data:
            new_node.next = sorted_head
            return new_node
        else:
            current = sorted_head
            while current.next and current.next.data < new_node.data:
                current = current.next
            new_node.next = current.next
            current.next = new_node
        return sorted_head

    # Функція для об'єднання двох відсортованих списків
    @staticmethod
    def merge_sorted_lists(list1, list2):
        dummy = Node()
        tail = dummy

        a = list1.head
        b = list2.head

        while a and b:
            if a.data < b.data:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next
            tail = tail.next

        tail.next = a if a else b

        merged_list = LinkedList()
        merged_list.head = dummy.next
        return merged_list


# Приклад використання
llist1 = LinkedList()
llist1.insert_at_end(5)
llist1.insert_at_end(1)
llist1.insert_at_end(4)

print("Оригінальний список:")
llist1.print_list()

# Реверсування списку
llist1.reverse()
print("Реверсований список:")
llist1.print_list()

# Сортування списку
llist1.sort()
print("Відсортований список:")
llist1.print_list()

# Створення другого відсортованого списку
llist2 = LinkedList()
llist2.insert_at_end(2)
llist2.insert_at_end(3)
llist2.insert_at_end(6)

# Об'єднання двох відсортованих списків
merged_list = LinkedList.merge_sorted_lists(llist1, llist2)
print("Об'єднаний відсортований список:")
merged_list.print_list()
