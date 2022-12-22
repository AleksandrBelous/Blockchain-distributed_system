#

from main_chain import chain, operations_limit, head


def is_Exists_Block(levIdx, blIdx):
    if len(chain[levIdx]) > blIdx:
        return True
    else:
        return False


def is_Ready_to_Close_Block(levIdx = head[0], blIdx = head[1]):
    if len(chain[levIdx][blIdx]) == 1 + operations_limit:
        return True
    else:
        return False


def is_Enough_Space_in_Block(levIdx, blIdx, required_space):
    if 1 + operations_limit - len(chain[levIdx][blIdx]) >= required_space:
        return True
    else:
        return False
