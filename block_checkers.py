#

import string
import random
import hashlib
import datetime
from main_chain import chain, operations_limit, head


def is_at_Least_One_Empty_Block():
    print('( in is_at_Least_One_Empty_Block fn...')
    res = False
    for i in range(head[0] + 1):
        lev_size = len(chain[i])
        for j in range(lev_size):
            # if len(chain[i][j]) == 1:
            if 1 + operations_limit - len(chain[i][j]) > 0:
                print(f'found already one empty block: block-{i}-{j}')
                res = True
                break
        if res:
            break
    print('...out of is_at_Least_One_Empty_Block fn )')
    return res


def is_Closed_Block(levIdx, blIdx):
    # if len(chain[levIdx][blIdx]) == 1 + operations_limit + 1:
    #     return True
    # else:
    #     return False
    return len(chain[levIdx][blIdx]) == 1 + operations_limit + 1


def is_Exists_Block(levIdx, blIdx):
    # if len(chain[levIdx]) > blIdx:
    #     return True
    # else:
    #     return False
    return len(chain[levIdx]) > blIdx


def is_Ready_to_Close_Block(levIdx, blIdx):  # (levIdx = head[0], blIdx = head[1]):
    return len(chain[levIdx][blIdx]) == 1 + operations_limit
    # if len(chain[levIdx][blIdx]) == 1 + operations_limit:
    #     return True
    # else:
    #     return False


# def is_Enough_Space_in_Block_v0(levIdx, blIdx, required_space):
#     if 1 + operations_limit - len(chain[levIdx][blIdx]) >= required_space:
#         return True
#     else:
#         return False


def is_Enough_Space_in_Block(levIdx, blIdx, required_space):
    # if 1 + operations_limit - len(chain[levIdx][blIdx]) >= required_space:
    #     return True
    # else:
    #     return False
    return 1 + operations_limit - len(chain[levIdx][blIdx]) >= required_space


def try_to_Find_Nonce(levelIdx, blockIdx):
    was_found = False
    
    def random_String():
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for _ in range(6))
    
    nonce = random_String()
    # make copy of block-file
    from block_getters import get_Block_Info
    copy_block_info = get_Block_Info(levelIdx, blockIdx)
    copy_block_info += nonce
    pr_hash = hashlib.md5(copy_block_info.encode()).hexdigest()
    from main_chain import nonce_requirements
    if pr_hash.count('0') == nonce_requirements:
        was_found = True
    return was_found, nonce


def is_Found_Nonce():
    print('( in is_Found_Nonce fn...')
    is_found = nonce = None
    win_i = win_j = None
    for i in range(head[0] + 1):
        level_size = len(chain[i])
        for j in range(level_size):
            if is_Ready_to_Close_Block(i, j):
                is_found, nonce = try_to_Find_Nonce(i, j)
                if is_found:
                    print(f'try to close {i}-{j}: success')
                    win_i = i
                    win_j = j
                    break
                else:
                    print(f'try to close {i}-{j}: failed')
        if is_found:
            break
    print('...out of is_Found_Nonce fn )')
    
    def action_to_String_with_Time_Mark(nonce):
        return nonce + ' ' + str(datetime.datetime.today())
    
    return is_found, win_i, win_j, action_to_String_with_Time_Mark(nonce)


def is_it_was_First_Closed_Block(win_i):
    count = 0
    lev_size = len(chain[win_i])
    for j in range(lev_size):
        if is_Closed_Block(win_i, j):
            count += 1
    # if count == 1:
    #     return True
    # else:
    #     return False
    return count == 1
