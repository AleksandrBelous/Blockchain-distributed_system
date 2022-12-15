#

from main_chain import chain

def draw():
    for i in range(len(chain)):
        print(f'Level {i + 1}')
        for j in range(len(chain[i])):
            print(f'----- BLOCK {j + 1} -----')
            # show the block
            for e in chain[i][j]:
                for k, v in e.items( ):
                    print(k, ':', v)
