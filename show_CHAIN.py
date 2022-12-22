#

from main_chain import chain


def draw( ):
    for i in range(len(chain)):
        print(f'\nLevel {i}')
        for j in range(len(chain[i])):
            print(f'----- BLOCK {i}-{j} -----')
            # show the block
            for e in chain[i][j]:
                for k, v in e.items( ):
                    print(k, ':', v)
    print( )
