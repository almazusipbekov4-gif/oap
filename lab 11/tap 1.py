# Задача 1: Создание графа в виде словаря (список смежности) из 5 вершин
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': [],
    'D': [],
    'E': []
}

# Задача 2: Добавление новой вершины и соединение её с другими
graph['F'] = ['C', 'E']
graph['A'].append('F')  # соединяем 'A' с новой вершиной 'F'

print("Исходный граф:", graph)


# Задача 3: Функция для вывода всех соседей заданной вершины
def print_neighbors(g, node):
    if node in g:
        print(f"Соседи вершины {node}: {g[node]}")
    else:
        print(f"Вершина {node} отсутствует в графе.")

print_neighbors(graph, 'A')


# Задача 4: Реализация алгоритма DFS (рекурсивно)
def dfs_recursive(g, node, visited=None):
    if visited is None:
        visited = set()
    
    if node not in visited:
        print(node, end=' ')
        visited.add(node)
        for neighbor in g.get(node, []):
            dfs_recursive(g, neighbor, visited)
            
    return visited

print("\nОбход DFS (рекурсивно) из вершины 'A':")
dfs_recursive(graph, 'A')


# Задача 5: Реализация алгоритма DFS (через стек)
def dfs_stack(g, start_node):
    visited = set()
    stack = [start_node]
    traversal_order = []
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            traversal_order.append(node)
            # Добавляем соседей в обратном порядке, чтобы они обрабатывались слева направо
            for neighbor in reversed(g.get(node, [])):
                if neighbor not in visited:
                    stack.append(neighbor)
                    
    return traversal_order

print("\nОбход DFS (через стек) из вершины 'A':", dfs_stack(graph, 'A'))


# Задача 6 & 7: Реализация алгоритма BFS (через очередь) и программа обхода
from collections import deque

def bfs(g, start_node):
    visited = set()
    queue = deque([start_node])
    visited.add(start_node)
    traversal_order = []
    
    while queue:
        node = queue.popleft()
        traversal_order.append(node)
        
        for neighbor in g.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                
    return traversal_order

print("Обход BFS (через очередь) из вершины 'A':", bfs(graph, 'A'))


# Задача 8: Проверка, существует ли путь между двумя вершинами
def has_path(g, start, end):
    if start not in g or end not in g:
        return False
    visited = set()
    queue = deque([start])
    visited.add(start)
    
    while queue:
        node = queue.popleft()
        if node == end:
            return True
        for neighbor in g.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                
    return False

print("Существует ли путь из 'A' в 'D':", has_path(graph, 'A', 'D'))
print("Существует ли путь из 'C' в 'A':", has_path(graph, 'C', 'A'))


# Задача 9: Определение количества вершин, достижимых из заданной вершины
def count_reachable(g, start_node):
    if start_node not in g:
        return 0
    visited = dfs_recursive(g, start_node)
    return len(visited)

print(f"Количество достижимых вершин из 'A': {count_reachable(graph, 'A')}")


# Задача 10 (повышенной сложности): Кратчайший путь между двумя вершинами с помощью BFS
def shortest_path(g, start, end):
    if start not in g or end not in g:
        return None
    
    queue = deque([[start]])
    visited = {start}
    
    while queue:
        path = queue.popleft()
        node = path[-1]
        
        if node == end:
            return path
            
        for neighbor in g.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
                
    return None

print("Кратчайший путь из 'A' в 'E':", shortest_path(graph, 'A', 'E'))