#

from main_chain import chain
from file_operations import save_new_Action_to_File
from block_setters import set_Nonce_to_Block


def close_Block(lineIdx, blockIdx):
    """add NONCE to the end of block"""
    nonce = set_Nonce_to_Block(lineIdx, blockIdx)
    cur_block = chain[lineIdx][blockIdx]
    cur_block.append({ 'nonce': nonce })
    last_str = ['nonce', nonce]
    save_new_Action_to_File(lineIdx, blockIdx, last_str)
