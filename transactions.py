#
import main


def set_NEW_Action(chain):
    """Will change the chain's block that is <class 'list'>"""
    data = input('data: ')
    
    # fixing the level, level is const within the func
    cur_level_idx = len(chain) - 1
    
    # fixing the block number
    cur_block_idx = len(chain[cur_level_idx]) - 1
    # fixing the block
    cur_block = chain[cur_level_idx][cur_block_idx]
    if len(cur_block) == main.block_len:
        # create new block within this level
        pr_hash = 'hash of prev block'
        chain[cur_level_idx].append(main.create_Block(prev_block_hash=pr_hash))
    
    # fixing the block number
    cur_block_idx = len(chain[cur_level_idx]) - 1
    # fixing the block
    cur_block = chain[cur_level_idx][cur_block_idx]
    # fixing a line for a transaction
    new_action_pos = len(cur_block)
    # add new transaction
    chain[cur_level_idx][cur_block_idx][new_action_pos] = data
