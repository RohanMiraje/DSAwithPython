# queue using two stacks
stack1 = []
stack2 = []

q1 = []
q2 = []


def push(key):
    print(f'push: {key}')
    while q1:
        q2.append(q1.pop(0))
    q1.append(key)


def pop():
    res = -1
    if q1:
        res = q1.pop(0)
    while q2:
        q1.append(q2.pop())
    return res


def enqueue(key):
    print(f'enqueue: {key}')
    stack1.append(key)


def dequeue():
    while not stack2:
        while stack1:
            stack2.append(stack1.pop())
        if not stack2:
            print('queue is empty')
            return -1
    return stack2.pop()


if __name__ == '__main__':
    # for i in range(5):
    #     enqueue(i)
    # print(f'stack1: {stack1}')
    # print(f'stack2: {stack2}')
    # for _ in range(3):
    #     print(f'dequeue:{dequeue()}')
    # print(f'stack1: {stack1}')
    # print(f'stack2: {stack2}')
    for i in range(5):
        push(i)
    print(f'q1: {q1}')
    print(f'q2: {q2}')
    for _ in range(3):
        print(f'pop:{pop()}')
    print(f'q1: {q1}')
    print(f'q2: {q2}')
