
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Добавление элемента в начало
    def add_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Добавление элемента в конец
    def add_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node

    # Вывод элементов списка
    def display(self):
        current = self.head

        while current is not None:
            print(current.data, end="")
            if current.next is not None:
                print(" -> ", end="")
            current = current.next

        print()

    # Поиск элемента
    def search(self, value):
        current = self.head

        while current is not None:
            if current.data == value:
                return True
            current = current.next

        return False

    # Удаление первого элемента
    def remove_front(self):
        if self.head is not None:
            self.head = self.head.next

    # Подсчёт элементов
    def count(self):
        total = 0
        current = self.head

        while current is not None:
            total += 1
            current = current.next

        return total

    # Разворот списка
    def reverse(self):
        previous = None
        current = self.head

        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        self.head = previous


# Задача 1: создание и связывание узлов
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

node1.next = node2
node2.next = node3

print("Задача 1: Связанные узлы")
print(node1.data, "->", node1.next.data,
      "->", node1.next.next.data)

# Задача 2: создание пустого списка
linked_list = LinkedList()
print("\nЗадача 2: Создан пустой список")

# Задача 3: добавление в начало
linked_list.add_front(10)
linked_list.add_front(20)
linked_list.add_front(30)

print("\nЗадача 3: Добавление в начало")
linked_list.display()

# Задача 4: добавление в конец
linked_list.add_end(40)

print("\nЗадача 4: Добавление в конец")
linked_list.display()

# Задача 5: вывод элементов
print("\nЗадача 5: Вывод списка")
linked_list.display()

# Задача 6: поиск элемента
print("\nЗадача 6: Поиск элемента")
print("20 найден:", linked_list.search(20))
print("50 найден:", linked_list.search(50))

# Задача 7: удаление первого элемента
print("\nЗадача 7: Удаление первого элемента")
print("До удаления:")
linked_list.display()

linked_list.remove_front()

print("После удаления:")
linked_list.display()

# Задача 8: подсчёт элементов
print("\nЗадача 8: Количество элементов")
print("Количество элементов:", linked_list.count())

# Задача 9: ввод пяти чисел
print("\nЗадача 9: Введите 5 чисел")
user_list = LinkedList()

for i in range(5):
    number = int(input(f"Введите число {i + 1}: "))
    user_list.add_end(number)

print("Полученный список:")
user_list.display()

# Задача 10: разворот списка
print("\nЗадача 10: Разворот списка")
print("Исходный список:")
user_list.display()

user_list.reverse()

print("После разворота:")
user_list.display()