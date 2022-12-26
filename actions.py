#

import datetime
from main_chain import chain, head, operations_limit  # , update_Tail
from checkers import *
from users import names, show_Names  # , reward_the_Miner
from memory_pool import pool
from block_checkers import is_Enough_Space_in_Block, is_Ready_to_Close_Block  # , is_Found_Nonce
from block_setters import set_All_New_Actions_to_Block
from block_operations import grow_Block_Tree  # close_Block
from block_creators import create_New_Block_in_Level  # create_New_Level_and_Block


def action_to_String_with_Time_Mark(act_info_second_part):
    res = ''
    for e in act_info_second_part:
        res += e + ' '
    res += str(datetime.datetime.today( ))
    return res


def find_Place_for_New_Action( ):
    # fixing the root level
    cur_level_idx = head[0]
    # num of unsaved actions
    required_space = len(pool)
    # find blocks that go earlier and remain open
    was_found = was_awarded = False
    for i in range(cur_level_idx + 1):
        # fixing the block number
        num_of_blocks = len(chain[i])
        print(f'num of block in lev {i} is {num_of_blocks}')
        for j in range(num_of_blocks):
            print(f'!!! try to put at {i}-{j}, space: {1 + operations_limit - len(chain[i][j])}, need: {required_space}')
            if is_Enough_Space_in_Block(i, j, required_space = required_space):
                # !!!!!
                was_found = True
                # !!!!!
                set_All_New_Actions_to_Block(i, j)
                print(f'success put at {i}-{j}')
                if is_Ready_to_Close_Block(i, j):
                    was_awarded = grow_Block_Tree(cur_level_idx)
                # # find nonce, do not close block
                # new_block_idx = len(chain[cur_level_idx])  # (len(chain[cur_level_idx]) - 1) + 1
                # create_New_Block_in_Level(cur_level_idx, new_block_idx)
                # # try to close at least one block in level
                # smn_nonce_was_found, win_i, win_j, smn_nonce = is_Found_Nonce( )
                # if smn_nonce_was_found:
                #     # close win_i, win_j block
                #     close_Block(win_i, win_j, smn_nonce)
                #     was_awarded = reward_the_Miner( )
                #     # create new line in chain
                #     if win_i == head[0] and win_j == head[1]:
                #         update_Tail(win_i, win_j)
                #         create_New_Level_and_Block( )
            break
        if was_found:
            break
    
    if not was_found:
        # create new block within current level
        new_block_idx = len(chain[cur_level_idx])  # (len(chain[cur_level_idx]) - 1) + 1
        print(f'^^^^^ no found => created new in level: {cur_level_idx}-{new_block_idx}')
        create_New_Block_in_Level(cur_level_idx, new_block_idx)
        set_All_New_Actions_to_Block(cur_level_idx, new_block_idx)
        if is_Ready_to_Close_Block(cur_level_idx, new_block_idx):
            was_awarded = grow_Block_Tree(cur_level_idx)
            # # close current block
            # close_Block(cur_level_idx, new_block_idx)
            # was_awarded = reward_the_Miner( )
            # # create new line in chain
            # update_Tail(cur_level_idx, new_block_idx)
            # create_New_Level_and_Block( )
            # find nonce, do not close block
    
    if was_awarded:
        find_Place_for_New_Action( )


def prepare_NEW_Action(act_info):
    """Will change the chain's block that is <class 'list'>"""
    # add new action
    action_key = act_info[0]
    action_value = action_to_String_with_Time_Mark(act_info_second_part = act_info[1:])
    new_line = { action_key: action_value }
    pool.append(new_line)
    # addition if action is transaction
    if action_key == 'transaction':
        info = action_value.split(sep = ' ')
        sender, recipient, money = info[0], info[1], info[2]
        debiting_info = sender + ' -' + money + ' ' + str(datetime.datetime.today( ))
        new_line = { 'debiting': debiting_info }
        pool.append(new_line)
        addition_info = recipient + ' +' + money + ' ' + str(datetime.datetime.today( ))
        new_line = { 'addition': addition_info }
        pool.append(new_line)
    
    find_Place_for_New_Action( )


def choose_Action(act):
    if act == '1':
        # user registration
        print('+ + + REGISTRATION + + +')
        name = input('>>> Name: ')
        if is_User_Exists(name):
            print(f'>>> The user <{name}> is already exists')
            return 1
        if name not in names:
            names.append(name)
        info = ['registration', name + ' 1000']
        prepare_NEW_Action(act_info = info)
    elif act == '2':
        # transaction
        print(' > > > TRANSACTION > > >')
        show_Names( )
        sender = input('>>> Sender: ')
        if not is_User_Exists(sender):
            print(f'>>> The user <{sender}> does not exist')
            return 1
        recipient = input('>>> Recipient: ')
        if not is_User_Exists(recipient):
            print(f'>>> The user <{recipient}> does not exist')
            return 1
        transfer_amount = input('>>> Transfer amount: ')
        if not is_Enough_Money(sender, transfer_amount):
            print(f'>>> The user <{sender}> does not have enough money')
            return 1
        info = ['transaction', sender, recipient, transfer_amount]
        prepare_NEW_Action(act_info = info)
    elif act == '3':
        # deleting a user
        print('- - - DELETING - - -')
        name = input('>>> Name: ')
        if not is_User_Exists(name):
            print(f'>>> The user <{name}> does not exist')
            return 1
        if is_User_Deleted(name):
            print(f'>>> The user <{name}> was already deleted')
            return 1
        if name in names:
            names.remove(name)
        info = ['deleting', name]
        prepare_NEW_Action(act_info = info)
    else:
        return 0
