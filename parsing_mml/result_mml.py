#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

class ResultMML(object):
    """docstring for ResultMML"""
    pattern_command = re.compile('MML Command-----(.*)')

    def __init__(self):
    # def __init__(self, line_number):
        super(ResultMML, self).__init__()
        # self.line_number = line_number
        self.command = None
        self.ne = None
        self.executed_time_stamp = None
        self.o_m_id = None
        self.result = None

    def command_search(self, line):
        match = ResultMML.pattern_command.search(line)
        if match:
            self.command = match.group(1)
