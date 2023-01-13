#

chain = list()

operations_limit = 3

nonce_requirements = 3

# tail->head is pwd through the main blocks

head = dict()


def update_Head():
    head[0] += 1
    head[1] = 0
    with open('blocks/head', 'w') as f:
        f.write(f'{head[0]} {head[1]}')


tail = dict()


def update_Tail(i, j):
    tail[0] = i
    tail[1] = j
    with open('blocks/tail', 'w') as f:
        f.write(f'{tail[0]} {tail[1]}')
