#

from main_chain import chain


def draw_Chain():
    for i in range(len(chain)):
        print(f'\n========== LEVEL {i} ==========\n')
        for j in range(len(chain[i])):
            print(f'----- BLOCK {i}-{j} -----')
            # show the block
            for n, e in enumerate(chain[i][j]):
                for k, v in e.items():
                    print(n, k, ':', v)
            print()
    # print()
