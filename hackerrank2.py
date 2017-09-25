s = input()
queue = []
stack = []

for let in s:
    queue.append(let)
    stack.append(let)


print(queue, stack)




for i in range(4):
    letter = stack.pop()
    print(letter)

