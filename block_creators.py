#

from main_chain import chain, update_Head, head, tail
from block_getters import get_Block_Hash
from file_operations import save_new_Action_to_File
import datetime


def create_Block(prev_lev_idx, prev_block_idx, new_lev_idx, new_block_idx):
    block = list()
    
    def action_to_String_with_Time_Mark(nonce):
        return nonce + ' ' + str(datetime.datetime.today())
    
    prev_block_hash = action_to_String_with_Time_Mark(get_Block_Hash(prev_lev_idx, prev_block_idx))
    block.append({f"previous_block-{prev_lev_idx}-{prev_block_idx}'s_hash": prev_block_hash})
    first_str = [f"previous_block-{prev_lev_idx}-{prev_block_idx}'s_hash", prev_block_hash]
    save_new_Action_to_File(new_lev_idx, new_block_idx, first_str)
    return block


def create_New_Block_in_Level(cur_level_idx, new_block_idx):
    prev_lev_idx, prev_block_idx = tail[0], tail[1]
    chain[cur_level_idx].append(create_Block(prev_lev_idx, prev_block_idx, cur_level_idx, new_block_idx))


def create_New_Level_and_Block():
    chain.append(list())
    update_Head()
    new_level_idx = head[0]
    prev_lev_idx, prev_block_idx = tail[0], tail[1]
    chain[new_level_idx].append(create_Block(prev_lev_idx, prev_block_idx, new_level_idx, 0))
