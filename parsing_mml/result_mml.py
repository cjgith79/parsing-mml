#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

class ResultMML(object):
    """docstring for ResultMML"""
    pattern_command = re.compile('MML Command-----(.*)')
    pattern_ne = re.compile('NE : (.*)')
    # pattern_ne = re.compile('Report : +++    (.*)')
    # pattern_ne = re.compile('Report : +++    (.*?)')
    # 'Report : +++    (.*?)(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})')

    def __init__(self, command):
        super(ResultMML, self).__init__()
        # self.command_line_number = None
        self.command = command
        self.ne = None
        self.executed_time_stamp = None
        self.o_m_id = None
        self.result = None

    def command_search(self, line):
        '''
            If match
                returns command
            ELSE
                returns false
        '''
        # def command_search(self, line, line_number):
        match = ResultMML.pattern_command.search(line)
        if match:
            return match.group(1)
        return False

    def __str__(self):
        message = (
                f"command:[{self.command}]\n"
            )
        return message
