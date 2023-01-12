#
import hashlib


def get_Block_Info(lineIdx, blockIdx):
    block_info = ''
    with open('blocks/block' + '-' + str(lineIdx) + '-' + str(blockIdx), 'r') as f:
        for line in f:
            block_info += line
    return block_info


def get_Block_Hash(lineIdx, blockIdx):
    block_info = ''
    with open('blocks/block' + '-' + str(lineIdx) + '-' + str(blockIdx), 'r') as f:
        for line in f:
            block_info += line
    block_hash = hashlib.md5(block_info.encode()).hexdigest()
    return block_hash
