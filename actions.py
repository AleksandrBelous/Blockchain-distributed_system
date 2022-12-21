#

import datetime
from main_chain import operations_limit, chain, head
from checkers import *
from users import names, show_Names
from memory_pool import pool
from block_checkers import is_Enough_Space_in_Block, is_Closed_Block
import file_operations
import block_operations


def action_to_String(act_info_second_part):
    res = ''
    for e in act_info_second_part:
        res += e + ' '
    res += str(datetime.datetime.today( ))
    return res


def save_NEW_Action(leveIdx, blockIdx):
    required_space = len(pool)
    while is_Enough_Space_in_Block(levIdx = leveIdx, blIdx = blockIdx, required_space = required_space):
        print( )


def prepare_NEW_Action(act_info):
    """Will change the chain's block that is <class 'list'>"""
    ####################################################################################################################
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
    ####################################################################################################################
    # fixing the root level
    cur_level_idx = head[0]
    # fixing the root block number
    cur_block_idx = head[1]
    # fixing the block
    cur_block = chain[cur_level_idx][cur_block_idx]
    
    if not is_Closed_Block(levIdx = cur_level_idx, blIdx = cur_block_idx):
        save_NEW_Action(cur_level_idx, cur_block_idx)
    
    # number of unsaved operations
    unsaved = len(pool)
    
    # while unsaved!=0:
    
    # fixing the root level
    cur_level_idx = head[0] - 1
    # fixing the root block number
    cur_block_idx = head[1] - 1
    # fixing the block
    cur_block = chain[cur_level_idx][cur_block_idx]
    
    # if len(cur_block) == 1 + allowed_operations:
    #     block_operations.new_Line_and_Block( )
    
    if 1 + operations_limit != len(cur_block) and 1 + operations_limit - len(cur_block) < unsaved:
        print(f'unsaved: {unsaved}')
        print(f'1 + allowed_operations: {1 + operations_limit}')
        print(f'1 + allowed_operations - len(cur_block): {1 + operations_limit - len(cur_block)}')
        block_operations.new_Block_in_Line( )
    
    # fixing the root level
    cur_level_idx = head[0] - 1
    # fixing the root block number
    cur_block_idx = head[1] - 1
    # fixing the block
    cur_block = chain[cur_level_idx][cur_block_idx]
    
    if len(cur_block) == 1 + operations_limit:
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
                lineIdx = head[0],  # cur_level_idx + 1,
                blockIdx = head[1],  # cur_block_idx + 1,
                action_info = [action_key, action_value])
    
    # after new entries we check whether it is necessary to close the block
    if len(cur_block) == 1 + operations_limit:
        block_operations.new_Line_and_Block( )


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
