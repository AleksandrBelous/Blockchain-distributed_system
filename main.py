#
import os.path
import shutil


if __name__ == '__main__':
    
    if os.path.isdir('blocks'):
        shutil.rmtree('blocks')
    
    os.mkdir('blocks')
    
    from main_chain import chain, head, tail
    
    chain.append(list( ))
    
    
    def root_BLock( ):
        return [{ 'Initial block': 'my-Block-Chain system' }]
    
    
    chain[0].append(root_BLock( ))
    
    head[0] = 0  # last head's level
    head[1] = 0  # last head's block
    
    tail[0] = -1  # previous block's level
    tail[1] = 0  # previous block's number
    from actions import action_to_String_with_Time_Mark, choose_Action
    
    second_part = action_to_String_with_Time_Mark(act_info_second_part = ['my-Block-Chain system'])
    from file_operations import save_new_Action_to_File
    
    save_new_Action_to_File(
            lineIdx = head[0],
            blockIdx = head[1],
            action_info = ['Initial block', second_part])
    
    from show_CHAIN import draw
    
    while True:
        draw( )
        act = input('Action - "1" -- User registration,\n'
                    '       - "2" -- Transaction,\n'
                    '       - "3" -- Deleting a user,\n'
                    '       - "4" -- Exit\n'
                    '       ------------------------->: ')
        res = choose_Action(act = act)
        if res == 0:
            break
        elif res == 1:
            continue
    print('====================')
    draw( )
