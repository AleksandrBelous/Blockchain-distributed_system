#

from main_chain import chain, operations_limit


def is_Exists_Block(levIdx, blIdx):
    if len(chain[levIdx]) > blIdx:
        return True
    else:
        return False


def is_Closed_Block(levIdx, blIdx):
    if len(chain[levIdx][blIdx]) == 1 + operations_limit + 1:
        return True
    else:
        return False


def is_Enough_Space_in_Block(levIdx, blIdx, required_space):
    if 1 + operations_limit - len(chain[levIdx][blIdx]) >= required_space:
        return True
    else:
        return False
