def bfs(start):
    queue = []
    queue.append(start)

    while queue:
        current = queue.pop()
        print(current.value)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
