# Задачи 1 & 2: Класс Node и класс LinkedList
class Node:
    def __init__(self, data):
        self.data = data  # поле для хранения данных
        self.next = None  # ссылка на следующий элемент

class LinkedList:
    def __init__(self):
        self.head = None  # инициализация пустого списка

    # Задача 3: Добавление элемента в начало списка
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Задача 4: Добавление элемента в конец списка
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # Задача 5: Вывод всех элементов списка
    def display(self):
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" → ".join(elements))

    # Задача 6: Поиск элемента в списке
    def search(self, value):
        current = self.head
        while current:
            if current.data == value:
                return True
            current = current.next
        return False

    # Задача 7: Удаление первого элемента списка
    def delete_head(self):
        if self.head:
            self.head = self.head.next

    # Задача 8: Подсчёт количества элементов в списке
    def count(self):
        counter = 0
        current = self.head
        while current:
            counter += 1
            current = current.next
        return counter

    # Задача 10 (Повышенной сложности): Разворот связного списка
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev


print("=== ДЕМОНСТРАЦИЯ ОСНОВНЫХ ЗАДАЧ (1–8, 10) ===")

# Задача 1 (Создание узлов вручную и связывание)
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node1.next = node2
node2.next = node3
print(f"Ручная связь узлов: {node1.data} → {node2.data} → {node3.data}")

# Создание экземпляра связного списка
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)

print("\nЗадача 4 (Добавление в конец 10 → 20 → 30 → 40):")
ll.display()

# Задача 3 (Добавление в начало)
ll.prepend(5)
print("После добавления элемента 5 в начало:")
ll.display()

# Задача 6 (Поиск элемента)
print("Поиск элемента 20 в списке:", ll.search(20))  # True
print("Поиск элемента 99 в списке:", ll.search(99))  # False

# Задача 7 (Удаление первого элемента)
print("\nЗадача 7 (Удаление первого элемента):")
print("До удаления:")
ll.display()
ll.delete_head()
print("После удаления:")
ll.display()

# Задача 8 (Подсчет количества элементов)
print("Количество элементов в списке:", ll.count())

# Задача 10 (Разворот связного списка)
print("\nЗадача 10 (Разворот списка):")
print("Исходный список:")
ll.display()
ll.reverse()
print("После разворота:")
ll.display()


print("\n=== ЗАДАНИЕ 9. Ввод 5 чисел пользователем ===")
user_list = LinkedList()
print("Введите 5 целых чисел для добавления в связный список:")
for i in range(5):
    while True:
        try:
            val = int(input(f"Число {i + 1}: "))
            user_list.append(val)
            break
        except ValueError:
            print("Ошибка: введите целое число.")

print("Итоговый связный список из введенных чисел:")
user_list.display()