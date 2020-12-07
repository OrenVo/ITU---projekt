#!/usr/bin/python3
import os
import time
import crypt


#https://stackoverflow.com/questions/28195805/running-notify-send-as-root

# awk '{u=$2+$4; t=$2+$4+$5; if (NR==1){u1=u; t1=t;} else print ($2+$4-u1) * 100 / (t-t1) "%"; }' <(grep 'cpu ' /proc/stat) <(sleep 1;grep 'cpu ' /proc/stat) # command to calculate cpu usage (not perfectly accurate)
# cat /proc/asound/card*/pcm*/sub*/status | grep state: # if running audio then state:RUNNING
def check_password(user, password):
    lines = []
    with open('/etc/shadow', 'rt') as f:
        lines = f.readlines()
    user_p_line = [x for x in lines if x[:len(user)] == user]   # Get line from user
    if user_p_line: # user found
        pass_part = user_p_line[0].split(':')[1]
        pass_part = [x for x in pass_part.split('$') if x != '']
        p_hash = pass_part[2]
        salt = pass_part[1]
        alg_id = pass_part[0]
        print(alg_id, salt, p_hash, sep=' ')
        print(crypt.crypt(password, f'${alg_id}${salt}'))
        return crypt.crypt(password, f'${alg_id}${salt}') == user_p_line[0].split(':')[1]
    else:   # user not found
        return False

def turn_off_pc(sleep=0):
    os.system(f'notify-send Shutdown "Computer will be shut down in {sleep} sec"')
    time.sleep(sleep)
    print("Computer is off")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    check_password(user='basicuser', password='basicuser')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
