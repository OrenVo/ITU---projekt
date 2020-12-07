#!/usr/bin/python3

import time
import os
import subprocess
import psutil



Actions = {
    "Poweroff": "poweroff",
    "Reboot": "reboot",
    "Hibernate": "",  # TBA
    "Suspend": "",   # TBA
    "Script": None
}


class Timer:
    def __init__(self):
        self.path = None        # path to script to be executed after time expires
        self.action = None      # Action to be executed
        self.time_set = 0       # time set to the timer
        self.time_left = 0      # time left after start of timer
        self.running = False    # whether timer is running or not
        self.stop = False       # whether timer should stop

    def set_timer(self, time_set: int):
        self.time_set = self.time_left = time_set
        self.running = False
        self.stop = False

    def set_action(self, action: str):
        self.action = action

    def set_script(self, path: str, parameters):
        self.path = path
        assert isinstance(parameters, list) or parameters is None
        if parameters:
            for parameter in parameters:
                self.path += parameter

    def start(self):
        assert self.time_set != 0
        assert self.running is False
        self.running = True
        for i in range(self.time_set):  # TODO notify
            if self.stop:
                self.running = False
                self.time_left = self.time_set
                self.stop = False
                break
            self.time_left -= 1
            time.sleep(1)
            if self.time_left == 0:
                self.do_action()

    def do_action(self):
        assert  self.time_left != 0
        action = Actions.get(self.action)
        assert action is not None
        if self.path:  # TODO maybe check if exist
            os.system(self.path)
        if action:
            os.system(action)
        else:
            self.time_left = self.time_set
            self.running = False  # whether timer is running or not
            self.stop = False  # whether timer should stop

Monitor = {
    'Network': 'net',
    'CPU': 'cpu',
    'RAM': 'ram',
    'Sound': 'audio'

}

class ResourceChecker:
    def __init__(self, ):
        self.cpu_cores = os.cpu_count() # https://docs.python.org/3/library/os.html#os.getloadavg
        # read from /proc/meminfo
        self.total_ram = -1
        with open('/proc/meminfo', 'rt') as file:
            total_ram = [line for line in file.readlines() if 'MemTotal:' in line]
            if total_ram:
                self.total_ram = int(total_ram[0].split('\t')[-1][:-1])

        self.network_interfaces = os.listdir('/sys/class/net/')
        self.time = -1
        self.monitor = None
        self.path = None
        self.action = None
        self.running = False
        self.stop = False

    def do_action(self):
        assert  self.time_left != 0
        action = Actions.get(self.action)
        assert action is not None
        if self.path:  # TODO maybe check if exist
            os.system(self.path)
        if action:
            os.system(action)
        else:
            self.time_left = self.time_set
            self.running = False  # whether timer is running or not
            self.stop = False  # whether timer should stop

    def set_action(self, action: str):  # TODO check
        self.action = action

    def set_script(self, path: str, parameters):  # TODO check
        self.path = path
        assert isinstance(parameters, list) or parameters is None
        if parameters:
            for parameter in parameters:
                self.path += parameter
    
    def set_monitor(self):
        ... # TBA

    def start_monitor(self):
        ... # TODO check