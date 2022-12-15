#

print(int('-100') + int('+100'))

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