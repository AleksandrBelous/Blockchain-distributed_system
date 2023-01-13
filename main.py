#
import os.path
import datetime
import shutil


if __name__ == '__main__':
    from main_chain import chain, head, tail
    from actions import choose_Action
    
    if os.path.isdir('blocks'):
        
        # shutil.rmtree('blocks')
        for file in os.listdir('blocks'):
            if 'block' in file:
                explication = file.split('-')
                _, lev_idx, bl_idx = explication[0], int(explication[1]), int(explication[2])
                print(len(chain))
                if lev_idx not in range(len(chain)):
                    chain.append([])
                if bl_idx not in range(len(chain[lev_idx])):
                    chain[lev_idx].append([])
                
                with open('blocks/' + file, 'r') as f:
                    for line in f:
                        action_info = line.split(sep=' ')
                        action_kye = action_info[0]
                        action_value = ''
                        for e in action_info[2:]:
                            action_value += ' ' + e.removesuffix('\n')
                        print(action_kye, action_value)
                        chain[lev_idx][bl_idx].append({action_kye: action_value})
            elif 'head' in file:
                with open('blocks/head', 'r') as f:
                    heads = f.read().split()
                    head[0], head[1] = int(heads[0]), int(heads[1])
                    print(head)
            else:
                with open('blocks/tail', 'r') as f:
                    tails = f.read().split()
                    tail[0], tail[1] = int(tails[0]), int(tails[1])
                    print(tail)
    else:
        if os.path.isdir('blocks'):
            shutil.rmtree('blocks')
        os.mkdir('blocks')
        
        chain.append(list())
        
        # def root_BLock():
        #     return [{'Initial block': 'my-Block-Chain system'}]
        
        head[0] = 0  # last head's level
        head[1] = 0  # last head's block
        with open('blocks/head', 'w') as f:
            f.write(f'{head[0]} {head[1]}')
        
        tail[0] = -1  # previous block's level
        tail[1] = 0  # previous block's number
        with open('blocks/tail', 'w') as f:
            f.write(f'{tail[0]} {tail[1]}')
        
        
        def action_to_String_with_Time_Mark(act_info_second_part):
            res = ''
            for e in act_info_second_part:
                res += e + ' '
            res += str(datetime.datetime.today())
            return res
        
        
        second_part = action_to_String_with_Time_Mark(['my-Block-Chain_system'])
        
        chain[0].append([{'Initial_block': second_part}])
        
        from file_operations import save_new_Action_to_File
        
        save_new_Action_to_File(
                lineIdx=head[0],
                blockIdx=head[1],
                action_info=['Initial_block', second_part])
    
    from show_CHAIN import draw_Chain
    
    # from actions import choose_Action
    
    while True:
        draw_Chain()
        act = input('Action - "0" -- Auto action,\n'
                    '       - "1" -- User registration,\n'
                    '       - "2" -- Transaction,\n'
                    '       - "3" -- Deleting a user,\n'
                    '       - "4" -- Exit\n'
                    '       ------------------------->: ')
        
        res = choose_Action(act=act)
        if res == 0:
            break
        elif res == 1:
            continue
    print('====================')
    draw_Chain()
