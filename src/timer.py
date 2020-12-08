#!/usr/bin/python3

import time
import os

from src.shared import Actions, shutdown_event


class Timer:
    def __init__(self, username: str):
        self.user = username
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
                self.path += ' ' + parameter

    def __call__(self):
        self.start()

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
        assert self.time_left != 0
        action = Actions.get(self.action)
        assert action is not None
        if self.path:  # TODO maybe check if exist
            os.system(f"/bin/su -s /bin/bash -c '{self.path}' {self.user}")
        if action:
            shutdown_event.set()
            os.system(action)
        else:
            self.time_left = self.time_set
            self.running = False  # whether timer is running or not
            self.stop = False  # whether timer should stop
