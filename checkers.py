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
                action_info = line.split(sep=' ')
                
                action = action_info[0]
                cur_name = action_info[2]
                
                def get_Cur_Time():
                    nonlocal action_info
                    time = action_info[-1].split(sep=':')
                    h = int(time[0])
                    m = int(time[1])
                    s = float(time[2])
                    return h, m, s
                
                if action == 'registration' and cur_name == name:
                    hour, minute, sec = get_Cur_Time()
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
                    hour, minute, sec = get_Cur_Time()
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
    
    res = None
    for file in os.listdir('blocks'):
        with open('blocks/' + file, 'r') as f:
            for line in f:
                action_info = line.split(sep=' ')
                
                action = action_info[0]
                cur_name = action_info[2]
                
                def get_Cur_Time():
                    nonlocal action_info
                    time = action_info[-1].split(sep=':')
                    h = int(time[0])
                    m = int(time[1])
                    s = float(time[2])
                    return h, m, s
                
                if action == 'registration' and cur_name == name:
                    cur_money = int(action_info[3])
                    hour, minute, sec = get_Cur_Time()
                    # hour >= max_hour and minute >= max_minute and sec > max_sec
                    if hour > max_hour:
                        exchange(hour, minute, sec)
                        total_money = cur_money
                    elif hour >= max_hour and minute > max_minute:
                        exchange(hour, minute, sec)
                        total_money = cur_money
                    elif hour >= max_hour and minute >= max_minute and sec > max_sec:
                        exchange(hour, minute, sec)
                        total_money = cur_money
                
                if (action == 'debiting' or action == 'addition' or action == 'awarding') and cur_name == name:
                    hour, minute, sec = get_Cur_Time()
                    cur_money = int(action_info[3])
                    if hour > max_hour:
                        exchange(hour, minute, sec)
                        total_money += cur_money
                    elif hour >= max_hour and minute > max_minute:
                        exchange(hour, minute, sec)
                        total_money += cur_money
                    elif hour >= max_hour and minute >= max_minute and sec > max_sec:
                        exchange(hour, minute, sec)
                        total_money += cur_money
                
                if action == 'deleting' and cur_name == name:
                    hour, minute, sec = get_Cur_Time()
                    if hour > max_hour:
                        exchange(hour, minute, sec)
                        total_money = 0
                    elif hour >= max_hour and minute > max_minute:
                        exchange(hour, minute, sec)
                        total_money = 0
                    elif hour >= max_hour and minute >= max_minute and sec > max_sec:
                        exchange(hour, minute, sec)
                        total_money = 0
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
                action_info = line.split(sep=' ')
                
                action = action_info[0]
                cur_name = action_info[2]
                
                def get_Cur_Time():
                    nonlocal action_info
                    time = action_info[-1].split(sep=':')
                    h = int(time[0])
                    m = int(time[1])
                    s = float(time[2])
                    return h, m, s
                
                if action == 'deleting' and cur_name == name:
                    hour, minute, sec = get_Cur_Time()
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
