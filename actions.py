#

import datetime
# import time

from main_chain import chain, head, operations_limit  # , update_Tail
from checkers import *
from users import names, show_Names  # , reward_the_Miner
from memory_pool import pool_queue, show_Pool
from block_checkers import is_Enough_Space_in_Block, is_Ready_to_Close_Block  # , is_Found_Nonce
# from block_setters import set_All_New_Actions_to_Block
from block_operations import grow_Block_Tree  # close_Block
from block_creators import create_New_Block_in_Level  # create_New_Level_and_Block


def action_to_String_with_Time_Mark(act_info_second_part):
    res = ''
    for e in act_info_second_part:
        res += e + ' '
    res += str(datetime.datetime.today())
    return res


def find_Place_for_New_Action():
    print('( in find_Place_for_New_Action fn...')
    # fixing the root level
    cur_level_idx = head[0]
    # num of unsaved actions
    required_space = 1  # len(pool)
    # find blocks that go earlier and remain open
    was_found = was_awarded = False
    for i in range(cur_level_idx + 1):
        # fixing the block number
        num_of_blocks = len(chain[i])
        print(f'num of block in lev {i} is {num_of_blocks}')
        for j in range(num_of_blocks):
            print(f'try to put at {i}-{j}, space: {1 + operations_limit - len(chain[i][j])}, need: {required_space}')
            if is_Enough_Space_in_Block(i, j, required_space=required_space):
                was_found = True
                # alternative
                # put here
                #
                cur_block = chain[i][j]
                # count = 0
                # for dict_line in pool:
                while True:
                    if len(pool_queue) == 0:
                        break
                    show_Pool()
                    dict_line = pool_queue[0]
                    cur_block.append(dict_line)
                    # count += 1
                    print(f'puts {dict_line}')
                    action_key = action_value = None
                    for k, v in dict_line.items():
                        action_key, action_value = k, v
                    # save to file
                    from file_operations import save_new_Action_to_File
                    save_new_Action_to_File(
                            lineIdx=i,
                            blockIdx=j,
                            action_info=[action_key, action_value])
                    pool_queue.pop(0)
                    if not is_Enough_Space_in_Block(i, j, 1) or len(pool_queue) == 0:
                        break
                # for a in range(count):
                #     pool.pop(a)
                print(f'success put at {i}-{j}')
                if is_Ready_to_Close_Block(i, j):
                    was_awarded = grow_Block_Tree(cur_level_idx)
        #         # alternative
        #         # !!!!!
        #         was_found = True
        #         # !!!!!
        #         set_All_New_Actions_to_Block(i, j)
        #         print(f'success put at {i}-{j}')
        #         if is_Ready_to_Close_Block(i, j):
        #             was_awarded = grow_Block_Tree(cur_level_idx)
        #     break
        # if was_found:
        #     break
    
    if not was_found:
        # create new block within current level
        new_block_idx = len(chain[cur_level_idx])  # (len(chain[cur_level_idx]) - 1) + 1
        print(f'no empty block was found => created new block in level: {cur_level_idx}-{new_block_idx}')
        create_New_Block_in_Level(cur_level_idx, new_block_idx)
        # alternative
        cur_block = chain[cur_level_idx][new_block_idx]
        # count = 0
        # for dict_line in pool:
        while True:
            if len(pool_queue) == 0:
                break
            show_Pool()
            dict_line = pool_queue[0]
            cur_block.append(dict_line)
            # count += 1
            action_key = action_value = None
            for k, v in dict_line.items():
                action_key, action_value = k, v
            # save to file
            from file_operations import save_new_Action_to_File
            save_new_Action_to_File(
                    lineIdx=cur_level_idx,
                    blockIdx=new_block_idx,
                    action_info=[action_key, action_value])
            pool_queue.pop(0)
            if not is_Enough_Space_in_Block(cur_level_idx, new_block_idx, 1) or len(pool_queue) == 0:
                break
        # for i in range(count):
        #     pool.pop(i)
        # set_All_New_Actions_to_Block(cur_level_idx, new_block_idx)
        if is_Ready_to_Close_Block(cur_level_idx, new_block_idx):
            was_awarded = grow_Block_Tree(cur_level_idx)
            # # close current block
            # close_Block(cur_level_idx, new_block_idx)
            # was_awarded = reward_the_Miner( )
            # # create new line in chain
            # update_Tail(cur_level_idx, new_block_idx)
            # create_New_Level_and_Block( )
            # find nonce, do not close block
    
    if was_awarded or len(pool_queue) != 0:
        find_Place_for_New_Action()
    print('...out of find_Place_for_New_Action fn )')
    show_Pool()


def prepare_NEW_Action(act_info):
    """Will change the chain's block that is <class 'list'>"""
    # add new action
    action_key = act_info[0]
    action_value = action_to_String_with_Time_Mark(act_info_second_part=act_info[1:])
    new_line = {action_key: action_value}
    pool_queue.append(new_line)
    # addition if action is transaction
    if action_key == 'transaction':
        info = action_value.split(sep=' ')
        sender, recipient, money = info[0], info[1], info[2]
        debiting_info = sender + ' -' + money + ' ' + str(datetime.datetime.today())
        new_line = {'debiting': debiting_info}
        pool_queue.append(new_line)
        addition_info = recipient + ' +' + money + ' ' + str(datetime.datetime.today())
        new_line = {'addition': addition_info}
        pool_queue.append(new_line)
    # ready to clean the memory pool :)
    find_Place_for_New_Action()


def prepare_NEW_Actions():
    from random import randint
    for i in range(randint(1, operations_limit)):
        act_info = ['action', f'information-{i + 1}']
        # add new action
        action_key = act_info[0]
        action_value = action_to_String_with_Time_Mark(act_info_second_part=act_info[1:])
        new_line = {action_key: action_value}
        pool_queue.append(new_line)
        # ready to clean the memory pool :)
    find_Place_for_New_Action()


def choose_Action(act):
    if act == '0':
        # auto action
        prepare_NEW_Actions()
    elif act == '1':
        # user registration
        print('+ + + REGISTRATION + + +')
        name = input('>>> Name: ')
        if is_User_Exists(name):
            print(f'>>> The user <{name}> is already exists')
            return 1
        if name not in names:
            names.append(name)
        info = ['registration', name + ' 1000']
        prepare_NEW_Action(act_info=info)
    elif act == '2':
        # transaction
        print(' > > > TRANSACTION > > >')
        show_Names()
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
        prepare_NEW_Action(act_info=info)
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
        prepare_NEW_Action(act_info=info)
    else:
        return 0
