#

from main_chain import chain, head, update_Tail
from file_operations import save_new_Action_to_File
from block_creators import create_New_Level_and_Block, create_New_Block_in_Level
from block_checkers import is_Found_Nonce, is_at_Least_One_Empty_Block, is_it_was_First_Closed_Block
from block_setters import set_Nonce_to_Block
from users import reward_the_Miner


def close_Block(lineIdx, blockIdx, nonce):
    """add NONCE to the end of block"""
    # nonce = set_Nonce_to_Block(lineIdx, blockIdx)
    cur_block = chain[lineIdx][blockIdx]
    cur_block.append({ 'nonce': nonce })
    last_str = ['nonce', nonce]
    save_new_Action_to_File(lineIdx, blockIdx, last_str)


def grow_Block_Tree(cur_level_idx):
    print('( in grow_Block_Tree fn...')
    was_awarded = False
    # find nonce, do not close block
    if cur_level_idx != 0:
        if not is_at_Least_One_Empty_Block( ):
            new_block_idx = len(chain[cur_level_idx])  # (len(chain[cur_level_idx]) - 1) + 1
            print(f'not enough blocks in level, created new one {cur_level_idx}-{new_block_idx}')
            create_New_Block_in_Level(cur_level_idx, new_block_idx)
        # try to close at least one block in level
        smn_nonce_was_found, win_i, win_j, smn_nonce = is_Found_Nonce( )
        if smn_nonce_was_found:
            # close win_i, win_j block
            close_Block(win_i, win_j, smn_nonce)
            was_awarded = reward_the_Miner( )
            # create new line in chain
            # if win_i == head[0] and win_j == head[1]:
            if is_it_was_First_Closed_Block(win_i):
                update_Tail(win_i, win_j)
                create_New_Level_and_Block( )
                print('just created new level and block')
    else:
        nonce = set_Nonce_to_Block(0, 0)
        close_Block(0, 0, nonce)
        update_Tail(head[0], head[1])
        create_New_Level_and_Block( )
        print('just closed 0-0')
        was_awarded = reward_the_Miner( )
    print('...out of  grow_Block_Tree fn )')
    return was_awarded
