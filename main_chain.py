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


# # fixing the root level
# cur_level_idx = head[0] - 1
# # fixing the root block number
# cur_block_idx = head[1] - 1
# # fixing the block
# cur_block = chain[cur_level_idx][cur_block_idx]

# # fixing the pre-root level
# prev_level_idx = tail[0] - 1
# # fixing the pre-root block number
# prev_block_idx = tail[1] - 1
# # fixing the block
# prev_block = chain[prev_level_idx][prev_block_idx]
