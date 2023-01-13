#


def new_file_name(lineNumber, blockNumber):
    return 'blocks/block' + '-' + str(lineNumber) + '-' + str(blockNumber)


def save_new_Action_to_File(lineIdx, blockIdx, action_info):
    with open('blocks/block' + '-' + str(lineIdx) + '-' + str(blockIdx), 'a') as f:
        f.write(action_info[0])
        f.write(' : ')
        f.write(action_info[1])
        f.write('\n')


def save_Block_in_File(block, lineIdx, blockIdx):
    file_name = new_file_name(lineIdx, blockIdx)
    with open(file_name, 'w') as f:
        for k, v in block.items():
            f.write(k)
            f.write(' ')
            f.write(v)
            f.write('\n')
