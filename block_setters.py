#

import string
import random
import hashlib

from actions import action_to_String
from main_chain import nonce_requirements
from block_getters import get_Block_Info
from file_operations import save_new_Action_to_File
from main_chain import chain
from memory_pool import pool


def set_New_Block(prev_block_hash, lineIdx, blockIdx):
    block = list( )
    block.append({ "previous block's hash": prev_block_hash })
    line_second_part = action_to_String([prev_block_hash])
    save_new_Action_to_File(lineIdx, blockIdx, ["previous block's hash", line_second_part])
    return block


def set_Nonce_to_Block(levelIdx, blockIdx):
    nonce = pr_hash = None
    
    def random_String( ):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for _ in range(6))
    
    while True:
        nonce = random_String( )
        # make copy of block-file
        copy = get_Block_Info(levelIdx, blockIdx)
        copy += nonce
        pr_hash = hashlib.md5(copy.encode( )).hexdigest( )
        if pr_hash.count('0') == nonce_requirements:
            last_str = ['nonce', nonce]
            save_new_Action_to_File(levelIdx, blockIdx, last_str)
            break
    return nonce, pr_hash


def set_All_New_Actions_to_Block(levIdx, blockIdx):
    cur_block = chain[levIdx][blockIdx]
    # save all new actions to block and to it's file
    for dict_line in pool:
        cur_block.append(dict_line)
        action_key = action_value = None
        for k, v in dict_line.items( ):
            action_key, action_value = k, v
        # save to file
        save_new_Action_to_File(
                lineIdx = levIdx,
                blockIdx = blockIdx,
                action_info = [action_key, action_value])
