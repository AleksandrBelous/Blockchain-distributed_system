#

import string
import random
import hashlib
from main_chain import chain, operations_limit, head


def is_Closed_Block(levIdx, blIdx):
    if len(chain[levIdx][blIdx]) == 1 + operations_limit + 1:
        return True
    else:
        return False


def is_Exists_Block(levIdx, blIdx):
    if len(chain[levIdx]) > blIdx:
        return True
    else:
        return False


def is_Ready_to_Close_Block(levIdx = head[0], blIdx = head[1]):
    if len(chain[levIdx][blIdx]) == 1 + operations_limit:
        return True
    else:
        return False


def is_Enough_Space_in_Block(levIdx, blIdx, required_space):
    if 1 + operations_limit - len(chain[levIdx][blIdx]) >= required_space:
        return True
    else:
        return False


def try_to_Find_Nonce(levelIdx, blockIdx):
    nonce = None
    was_found = False
    
    def random_String( ):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for _ in range(6))
    
    nonce = random_String( )
    # make copy of block-file
    from block_getters import get_Block_Info
    copy_block_info = get_Block_Info(levelIdx, blockIdx)
    copy_block_info += nonce
    pr_hash = hashlib.md5(copy_block_info.encode( )).hexdigest( )
    from main_chain import nonce_requirements
    if pr_hash.count('0') == nonce_requirements:
        was_found = True
    return was_found, nonce


def is_Found_Nonce( ):
    is_found = nonce = None
    win_i = win_j = None
    for i in range(head[0] + 1):
        level_size = len(chain[i])
        for j in range(level_size):
            if is_Ready_to_Close_Block(i, j):
                is_found, nonce = try_to_Find_Nonce(i, j)
                if is_found:
                    win_i = i
                    win_j = j
                    break
        if is_found:
            break
    return is_found, win_i, win_j, nonce
