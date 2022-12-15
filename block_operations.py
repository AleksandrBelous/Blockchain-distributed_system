#

from main import create_Block
from main_chain import chain, root, nonce_requirements
import file_operations
import itertools


def get_Block_Info(lineNumber, blockNumber):
    block_info = ''
    with open('blocks/block' + '-' + str(lineNumber) + '-' + str(blockNumber), 'r') as f:
        for line in f:
            block_info += line
    return block_info


def add_New_Block( ):
    print('in add_new_block fn')
    cur_level_idx = root[0] - 1
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # add NONCE to the end of block
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    alphabet = '0123456789'
    pr_hash = None
    while True:
        nonce = None
        for letter in itertools.product(alphabet, repeat = 6):
            nonce = ''.join(letter)
        # make copy of block-file
        pr_hash = file_operations.get_Block_Hash(root[0], root[1], nonce)
        if pr_hash.count('0') == nonce_requirements:
            print(pr_hash)
            # create new block within this level
            
            break
    
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # predict block's number: n=n+1
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    root[1] += 1
    chain[cur_level_idx].append(create_Block(
            prev_block_hash = pr_hash,
            lineNumber = root[0],  # cur_level_idx + 1,
            blockNumber = root[1]))  # cur_block_idx + 1 + 1))
