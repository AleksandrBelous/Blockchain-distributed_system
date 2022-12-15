#

import hashlib


def new_file_name(lineNumber, blockNumber):
    return 'blocks/block' + '-' + str(lineNumber) + '-' + str(blockNumber)


def save_new_Action_to_File(lineNumber, blockNumber, action_info):
    with open('blocks/block' + '-' + str(lineNumber) + '-' + str(blockNumber), 'a') as f:
        f.write(action_info[0])
        f.write(' : ')
        f.write(action_info[1])
        f.write('\n')


def get_Block_Hash(lineNumber, blockNumber, nonce):
    block_info = ''
    with open('blocks/block' + '-' + str(lineNumber) + '-' + str(blockNumber), 'r') as f:
        for line in f:
            block_info += line
        block_info += nonce
    block_hash = hashlib.md5(block_info.encode( )).hexdigest( )
    return block_hash


def save_Block_in_File(block, lineNumber, blockNumber):
    file_name = new_file_name(lineNumber, blockNumber)
    with open(file_name, 'w') as f:
        for k, v in block.items( ):
            f.write(k)
            f.write(' ')
            f.write(v)
            f.write('\n')
