#
import hashlib

from main import create_Block
from main_chain import chain, head, tail, nonce_requirements, allowed_operations
import file_operations
import string
import random
from memory_pool import pool


def random_String( ):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(6))


def get_Block_Info(lineNumber, blockNumber):
    block_info = ''
    with open('blocks/block' + '-' + str(lineNumber) + '-' + str(blockNumber), 'r') as f:
        for line in f:
            block_info += line
    return block_info


def get_Nonce(blockLevel, blockNumber):
    nonce = pr_hash = None
    while True:
        nonce = random_String( )
        # make copy of block-file
        copy = get_Block_Info(blockLevel, blockNumber)
        copy += nonce
        pr_hash = hashlib.md5(copy.encode( )).hexdigest( )
        if pr_hash.count('0') == nonce_requirements:
            # create new block within this level
            last_str = ['nonce', nonce]
            file_operations.save_new_Action_to_File(blockLevel, blockNumber, last_str)
            break
    return nonce, pr_hash


def new_Line_and_Block( ):
    """add NONCE to the end of block"""
    
    tail[0] = head[0]
    tail[1] = head[1]
    
    nonce, pr_hash = get_Nonce(blockLevel = head[0], blockNumber = head[1])
    
    # fixing the root level
    cur_level_idx = head[0] - 1
    # fixing the root block number
    cur_block_idx = head[1] - 1
    # fixing the block
    cur_block = chain[cur_level_idx][cur_block_idx]
    
    cur_block.append({ 'nonce': nonce })
    
    chain.append(list( ))
    # predict new block's line: x=x+1
    print(f'will change head[{cur_level_idx}][{cur_block_idx}]')
    head[0] += 1
    head[1] = 1
    # fixing the head level
    cur_level_idx = head[0] - 1
    # fixing the root block number
    print(f'changed to  head[{cur_level_idx}][{cur_block_idx}]')
    chain[cur_level_idx].append(create_Block(
            prev_block_hash = pr_hash,
            lineNumber = head[0],
            blockNumber = head[1]))


def new_Block_in_Line( ):
    print('we will need to create new block in line')
    # fixing the root level
    cur_level_idx = head[0] - 1
    # fixing the root block number
    cur_block_idx = head[1] - 1
    # fixing the block
    cur_block = chain[cur_level_idx][cur_block_idx]
    
    print(cur_block)
    
    pr_hash = cur_block[0]["previous block's hash"]
    print(f'pr_hash: {pr_hash}')
    
    new_block_idx = cur_block_idx + 1
    new_block_number = new_block_idx + 1
    tail[2] = new_block_number
    if len(chain[cur_level_idx]) == new_block_number:
        print(f'block {cur_level_idx + 1},{new_block_idx + 1} alr excsist')
    print(f'new block: chain[{cur_level_idx}][{new_block_idx}]')
    chain[cur_level_idx].append(create_Block(
            prev_block_hash = pr_hash,
            lineNumber = head[0],
            blockNumber = new_block_number))
    print(f'BLOCK LINE & NUM: {new_block_idx + 1},{new_block_number}')
    cur_block = chain[cur_level_idx][new_block_idx]
    print('pool is:')
    print(pool)
    for dict_line in pool:
        print(cur_block)
        cur_block.append(dict_line)
        print(dict_line)
        print(cur_block)
        action_key = action_value = None
        for k, v in dict_line.items( ):
            action_key, action_value = k, v
        file_operations.save_new_Action_to_File(
                lineNumber = head[0],
                blockNumber = new_block_number,
                action_info = [action_key, action_value])
        if len(cur_block) == 1 + allowed_operations:
            nonce, _ = get_Nonce(blockLevel = head[0], blockNumber = new_block_number)
            cur_block.append({ 'nonce': nonce })
            file_operations.save_new_Action_to_File(
                    lineNumber = head[0],
                    blockNumber = new_block_number,
                    action_info = [action_key, action_value])
            pool.clear( )
            break
        # pool.remove(dict_line)


def search_Unclosed_Block():
    for i in range(len(chain)):
        for j in range(len(chain[i])):
            cur_block = None
            if len(chain[i][j]) > 0:
                cur_block = chain[i][j]
            if len(cur_block) == 1 + allowed_operations:
                print('ok')
