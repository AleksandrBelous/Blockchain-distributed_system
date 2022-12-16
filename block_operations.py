#
import hashlib

from main import create_Block
from main_chain import chain, root, nonce_requirements
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


def add_New_Block( ):
    print('in add_new_block fn')
    
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # add NONCE to the end of block
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    
    alphabet = '0123456789'
    pr_hash = None
    nonce = None
    while True:
        nonce = random_String( )
        # make copy of block-file
        copy = get_Block_Info(root[0], root[1])
        copy += nonce
        # with open('tmp', 'w') as tmp:
        #    tmp.write(copy)
        # pr_hash = file_operations.get_Block_Hash(root[0], root[1], nonce)
        pr_hash = hashlib.md5(copy.encode( )).hexdigest( )
        if pr_hash.count('0') == nonce_requirements:
            print(pr_hash)
            # create new block within this level
            last_str = ['nonce', nonce]
            file_operations.save_new_Action_to_File(root[0], root[1], last_str)
            break
    
    # fixing the level
    cur_level_idx = root[0] - 1
    # fixing the new block number
    cur_block_idx = root[1] - 1
    # fixing the block
    cur_block = chain[cur_level_idx][cur_block_idx]
    cur_block.append({ 'nonce': nonce })
    
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # predict block's number: n=n+1
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    root[1] += 1
    chain[cur_level_idx].append(create_Block(
            prev_block_hash = pr_hash,
            lineNumber = root[0],  # cur_level_idx + 1,
            blockNumber = root[1]))  # cur_block_idx + 1 + 1))
