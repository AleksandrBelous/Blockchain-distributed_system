#

pool = list( )


def is_Pool_Empty( ):
    if len(pool) == 0:
        return True
    else:
        return False


def show_Pool( ):
    print('( in show_Pool fn...')
    for dict_line in pool:
        for k, v in dict_line.items( ):
            print(k, v)
    print('...in show_Pool fn )')
