#

chain = list( )

operations_limit = 3

nonce_requirements = 1

# tail->head is pwd through the main blocks

head = dict( )


def update_Head( ):
    head[0] += 1
    head[1] = 0


tail = dict( )


def update_Tail(i, j):
    tail[0] = i
    tail[1] = j
