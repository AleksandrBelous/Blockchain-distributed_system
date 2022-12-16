#
import hashlib

from main import create_Block
from main_chain import chain, head, tail, nonce_requirements
import file_operations
import string
import random


def random_String( ):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(6))


def get_Block_Info(lineNumber, blockNumber):
    block_info = ''
    with open('blocks/block' + '-' + str(lineNumber) + '-' + str(blockNumber), 'r') as f:
        for line in f:
            block_info += line
    return block_info


def get_Nonce( ):
    nonce = pr_hash = None
    while True:
        nonce = random_String( )
        # make copy of block-file
        copy = get_Block_Info(head[0], head[1])
        copy += nonce
        pr_hash = hashlib.md5(copy.encode( )).hexdigest( )
        if pr_hash.count('0') == nonce_requirements:
            # create new block within this level
            last_str = ['nonce', nonce]
            file_operations.save_new_Action_to_File(head[0], head[1], last_str)
            break
    return nonce, pr_hash


def new_Line_and_Block( ):
    """add NONCE to the end of block"""
    
    nonce, pr_hash = get_Nonce( )
    
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
    # fixing the root level
    cur_level_idx = head[0] - 1
    # fixing the root block number
    print(f'changed to  head[{cur_level_idx}][{cur_block_idx}]')
    chain[cur_level_idx].append(create_Block(
            prev_block_hash = pr_hash,
            lineNumber = head[0],
            blockNumber = head[1]))


def new_Block_in_Line( ):
    print('we will need to create new block in line')
