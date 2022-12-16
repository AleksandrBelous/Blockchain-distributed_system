#

import datetime
from main_chain import allowed_operations, chain, head
from checkers import *
from users import names, show_Names
from memory_pool import pool
import file_operations
import block_operations


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
    
    # number of unsaved operations
    unsaved = len(pool)
    print(f'unsaved: {unsaved}')
    # fixing the root level
    cur_level_idx = head[0] - 1
    # fixing the root block number
    cur_block_idx = head[1] - 1
    # fixing the block
    cur_block = chain[cur_level_idx][cur_block_idx]
    
    if 1 + allowed_operations - len(cur_block) < unsaved and 1 + allowed_operations != len(cur_block):
        block_operations.new_Block_in_Line( )
    
    # if len(cur_block) == 1 + allowed_operations:
    #     block_operations.new_Line_and_Block( )
    #
    # # fixing the level
    # cur_level_idx = head[0] - 1
    # # fixing the new block number
    # cur_block_idx = head[1] - 1
    # print(f'chain[{cur_level_idx}][{cur_block_idx}]')
    # # fixing the block
    # cur_block = chain[cur_level_idx][cur_block_idx]
    #
    # # number of unsaved operations
    # unsaved = len(pool)
    #
    # if 1 + allowed_operations - len(cur_block) < unsaved:
    #     print('not enough memory')

    # fixing the root level
    cur_level_idx = head[0] - 1
    # fixing the root block number
    cur_block_idx = head[1] - 1
    # fixing the block
    cur_block = chain[cur_level_idx][cur_block_idx]
    
    if len(cur_block) == 1 + allowed_operations:
        block_operations.new_Line_and_Block( )

    # fixing the root level
    cur_level_idx = head[0] - 1
    # fixing the root block number
    cur_block_idx = head[1] - 1
    # fixing the block
    cur_block = chain[cur_level_idx][cur_block_idx]
    
    # save new action/actions to block and to it's file
    for dict_line in pool:
        cur_block.append(dict_line)
        action_key = action_value = None
        for k, v in dict_line.items( ):
            action_key, action_value = k, v
        # action_key = pair[0]  # dict_line.keys( )[0]
        # action_value = dict_line[action_key]
        file_operations.save_new_Action_to_File(
                lineNumber = head[0],  # cur_level_idx + 1,
                blockNumber = head[1],  # cur_block_idx + 1,
                action_info = [action_key, action_value])
    
    # after new entries we check whether it is necessary to close the block
    if len(cur_block) == 1 + allowed_operations:
        block_operations.new_Line_and_Block( )


def choose_Action(act):
    from show_CHAIN import draw
    draw()
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
            print(f'The user <{sender}> does not have enough money')
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
