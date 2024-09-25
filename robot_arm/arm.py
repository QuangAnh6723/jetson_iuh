__pos_init = 'init'
__pos_0 = 'pos0'
__pos_1 = 'pos1'
__pos_2 = 'pos2'

def go_pos(pos: int):
    print('robot going to',end=' ')
    if pos == 0:
        print(__pos_0)
    elif pos == 1:
        print(__pos_1)
    elif pos == 2:
        print(__pos_2)
    else:
        print(__pos_init)
    