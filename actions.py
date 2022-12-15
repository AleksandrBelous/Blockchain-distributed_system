#

import datetime
from main import create_Block
from main_chain import chain, allowed_operations
from checkers import *
from users import names, show_Names
from memory_pool import pool
import file_operations


def action_to_String(act_info_second_part):
    res = ''
    for e in act_info_second_part:
        res += e + ' '
    res += str(datetime.datetime.today( ))
    return res


def set_NEW_Action(act_info):
    """Will change the chain's block that is <class 'list'>"""
    pool.clear( )
    # add new action
    action_key = act_info[0]
    action_value = action_to_String(act_info_second_part = act_info[1:])
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
    
    # fixing the level, level is const within the func
    cur_level_idx = len(chain) - 1
    # fixing the block number
    cur_block_idx = len(chain[cur_level_idx]) - 1
    # fixing the block
    cur_block = chain[cur_level_idx][cur_block_idx]
    
    if len(cur_block) == 1 + allowed_operations:
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # add NONCE to the end of block
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # create new block within this level
        pr_hash = file_operations.get_Block_Hash(cur_level_idx + 1, cur_block_idx + 1)
        chain[cur_level_idx].append(create_Block(
                prev_block_hash = pr_hash,
                lineNumber = cur_level_idx + 1,
                # predict block's number: n=n+1
                blockNumber = cur_block_idx + 1 + 1))
        # block_number = block_number + 1
    
    # fixing the new block number
    cur_block_idx = len(chain[cur_level_idx]) - 1
    # fixing the block
    cur_block = chain[cur_level_idx][cur_block_idx]

    # number of unsaved operations
    unsaved = len(pool)

    if 1 + allowed_operations - len(cur_block) < unsaved:
        print('not enough mem')
    
    # save new action to block and it's file
    for dict_line in pool:
        cur_block.append(dict_line)
        action_key = action_value = None
        for k, v in dict_line.items( ):
            action_key, action_value = k, v
        # action_key = pair[0]  # dict_line.keys( )[0]
        # action_value = dict_line[action_key]
        file_operations.save_new_Action_to_File(
                lineNumber = cur_level_idx + 1,
                blockNumber = cur_block_idx + 1,
                action_info = [action_key, action_value])


def choose_Action(act):
    if act == '1':
        # user registration
        print('+ + + REGISTRATION + + +')
        name = input('Name: ')
        if is_User_Exists(name):
            print(f'The user <{name}> is already exists')
            return 1
        if name not in names:
            names.append(name)
        info = ['registration', name + ' 1000']
        set_NEW_Action(act_info = info)
    elif act == '2':
        # transaction
        print(' > > > TRANSACTION > > >')
        show_Names( )
        sender = input('Sender: ')
        if not is_User_Exists(sender):
            print(f'The user <{sender}> does not exist')
            return 1
        recipient = input('Recipient: ')
        if not is_User_Exists(recipient):
            print(f'The user <{recipient}> does not exist')
            return 1
        transfer_amount = input('Transfer amount: ')
        if not is_Enough_Money(sender, transfer_amount):
            print(f'The user <{sender}> has not enough money')
            return 1
        info = ['transaction', sender, recipient, transfer_amount]
        set_NEW_Action(act_info = info)
    elif act == '3':
        # deleting a user
        print('- - - DELETING - - -')
        name = input('Name: ')
        if not is_User_Exists(name):
            print(f'The user <{name}> does not exist')
            return 1
        if is_User_Deleted(name):
            print(f'The user <{name}> was already deleted')
            return 1
        if name in names:
            names.remove(name)
        info = ['deleting', name]
        set_NEW_Action(act_info = info)
    else:
        return 0
