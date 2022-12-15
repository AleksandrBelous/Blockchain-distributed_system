#

import os


def is_User_Exists(name):
    max_hour = max_minute = max_sec = 0
    
    def exchange(h, m, s):
        nonlocal max_hour, max_minute, max_sec
        max_hour, max_minute, max_sec = h, m, s
    
    res = False
    for file in os.listdir('blocks'):
        with open('blocks/' + file, 'r') as f:
            for line in f:
                action_info = line.split(sep = ' ')
                
                action = action_info[0]
                cur_name = action_info[2]
                
                def get_Cur_Time( ):
                    nonlocal action_info
                    time = action_info[-1].split(sep = ':')
                    h = int(time[0])
                    m = int(time[1])
                    s = float(time[2])
                    return h, m, s
                
                if action == 'registration' and cur_name == name:
                    hour, minute, sec = get_Cur_Time( )
                    # hour >= max_hour and minute >= max_minute and sec > max_sec
                    if hour > max_hour:
                        exchange(hour, minute, sec)
                        res = True
                    elif hour >= max_hour and minute > max_minute:
                        exchange(hour, minute, sec)
                        res = True
                    elif hour >= max_hour and minute >= max_minute and sec > max_sec:
                        exchange(hour, minute, sec)
                        res = True
                
                if action == 'deleting' and cur_name == name:
                    hour, minute, sec = get_Cur_Time( )
                    if hour > max_hour:
                        exchange(hour, minute, sec)
                        res = False
                    elif hour >= max_hour and minute > max_minute:
                        exchange(hour, minute, sec)
                        res = False
                    elif hour >= max_hour and minute >= max_minute and sec > max_sec:
                        exchange(hour, minute, sec)
                        res = False
    return res


def is_Enough_Money(name, diff_money):
    max_hour = max_minute = max_sec = 0
    # variable amount, the amount will change during the search
    total_money = 0
    
    def exchange(h, m, s):
        nonlocal max_hour, max_minute, max_sec
        max_hour, max_minute, max_sec = h, m, s
    
    res = False
    for file in os.listdir('blocks'):
        with open('blocks/' + file, 'r') as f:
            for line in f:
                action_info = line.split(sep = ' ')
                
                action = action_info[0]
                cur_name = action_info[2]
                
                def get_Cur_Time( ):
                    nonlocal action_info
                    time = action_info[-1].split(sep = ':')
                    h = int(time[0])
                    m = int(time[1])
                    s = float(time[2])
                    return h, m, s
                
                if action == 'registration' and cur_name == name:
                    hour, minute, sec = get_Cur_Time( )
                    # hour >= max_hour and minute >= max_minute and sec > max_sec
                    if hour > max_hour:
                        exchange(hour, minute, sec)
                        cur_money = int(action_info[3])
                        total_money = cur_money
                        # if cur_money >= diff_money:
                        #     res = True
                        # else:
                        #     res = False
                    elif hour >= max_hour and minute > max_minute:
                        exchange(hour, minute, sec)
                        cur_money = int(action_info[3])
                        total_money = cur_money
                        # if cur_money >= diff_money:
                        #     res = True
                        # else:
                        #     res = False
                    elif hour >= max_hour and minute >= max_minute and sec > max_sec:
                        exchange(hour, minute, sec)
                        cur_money = int(action_info[3])
                        total_money = cur_money
                        # if cur_money >= diff_money:
                        #     res = True
                        # else:
                        #     res = False
                
                if action == 'transaction' and action_info[2] == name:  # cur_name is sender
                    hour, minute, sec = get_Cur_Time( )
                    # hour >= max_hour and minute >= max_minute and sec > max_sec
                    if hour > max_hour:
                        exchange(hour, minute, sec)
                        # sender loses money
                        total_money -= int(action_info[4])
                        # if cur_money >= diff_money:
                        #     res = True
                        # else:
                        #     res = False
                    elif hour >= max_hour and minute > max_minute:
                        exchange(hour, minute, sec)
                        total_money -= int(action_info[4])
                        # if cur_money >= diff_money:
                        #     res = True
                        # else:
                        #     res = False
                    elif hour >= max_hour and minute >= max_minute and sec > max_sec:
                        exchange(hour, minute, sec)
                        total_money -= int(action_info[4])
                        # if cur_money >= diff_money:
                        #     res = True
                        # else:
                        #     res = False
                
                if action == 'transaction' and action_info[3] == name:  # cur_name is recipient
                    hour, minute, sec = get_Cur_Time( )
                    # hour >= max_hour and minute >= max_minute and sec > max_sec
                    if hour > max_hour:
                        exchange(hour, minute, sec)
                        # recipient gets money
                        total_money += int(action_info[4])
                        # if cur_money >= diff_money:
                        #     res = True
                        # else:
                        #     res = False
                    elif hour >= max_hour and minute > max_minute:
                        exchange(hour, minute, sec)
                        total_money += int(action_info[4])
                        # if cur_money >= diff_money:
                        #     res = True
                        # else:
                        #     res = False
                    elif hour >= max_hour and minute >= max_minute and sec > max_sec:
                        exchange(hour, minute, sec)
                        total_money += int(action_info[4])
                        # if cur_money >= diff_money:
                        #     res = True
                        # else:
                        #     res = False
                
                if action == 'deleting' and cur_name == name:
                    hour, minute, sec = get_Cur_Time( )
                    if hour > max_hour:
                        exchange(hour, minute, sec)
                        total_money = 0
                        # res = False
                    elif hour >= max_hour and minute > max_minute:
                        exchange(hour, minute, sec)
                        total_money = 0
                        # res = False
                    elif hour >= max_hour and minute >= max_minute and sec > max_sec:
                        exchange(hour, minute, sec)
                        total_money = 0
                        # res = False
    if total_money >= int(diff_money):
        res = True
    else:
        res = False
    return res


def is_User_Deleted(name):
    max_hour = max_minute = max_sec = 0
    
    def exchange(h, m, s):
        nonlocal max_hour, max_minute, max_sec
        max_hour, max_minute, max_sec = h, m, s
    
    res = False
    for file in os.listdir('blocks'):
        with open('blocks/' + file, 'r') as f:
            for line in f:
                action_info = line.split(sep = ' ')
                
                action = action_info[0]
                cur_name = action_info[2]
                
                def get_Cur_Time( ):
                    nonlocal action_info
                    time = action_info[-1].split(sep = ':')
                    h = int(time[0])
                    m = int(time[1])
                    s = float(time[2])
                    return h, m, s
                
                if action == 'deleting' and cur_name == name:
                    hour, minute, sec = get_Cur_Time( )
                    if hour > max_hour:
                        exchange(hour, minute, sec)
                        res = True
                    elif hour >= max_hour and minute > max_minute:
                        exchange(hour, minute, sec)
                        res = True
                    elif hour >= max_hour and minute >= max_minute and sec > max_sec:
                        exchange(hour, minute, sec)
                        res = True
    return res
