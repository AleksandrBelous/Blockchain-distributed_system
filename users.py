#
import random
import datetime
from actions import prepare_NEW_Action

names = list( )


def show_Names( ):
    for name in names:
        print(name, end = ' ')
    print(end = '\n')


def reward_the_Miner( ):
    name = random.choice(names)
    addition_info = name + ' + 250 ' + str(datetime.datetime.today( ))
    new_line = { 'addition': addition_info }
    prepare_NEW_Action(act_info = new_line)
