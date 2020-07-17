#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

class ResultMML(object):
    """docstring for ResultMML"""
    pattern_command = re.compile('MML Command-----(.*)')
    pattern_ne = re.compile('NE : (.*)')
    pattern_executed_time_stamp = re.compile(
        '(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})')
    pattern_o_m_id = re.compile('O&M    #(.*)')

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
        match = ResultMML.pattern_command.search(line)
        if match:
            return match.group(1)
        return False

    def ne_search(self, line):
        if not self.ne:
            match = ResultMML.pattern_ne.search(line)
            if match:
                self.ne = match.group(1)

    def executed_time_stamp_search(self, line):
        if not self.executed_time_stamp:
            match = ResultMML.pattern_executed_time_stamp.search(line)
            if match:
                self.executed_time_stamp = match.group(1)

    def o_m_id_search(self, line):
        if not self.o_m_id:
            match = ResultMML.pattern_o_m_id.search(line)
            if match:
                self.o_m_id = match.group(1)

    def fields_search(self, line):
        self.ne_search(line)
        self.executed_time_stamp_search(line)
        self.o_m_id_search(line)

    def __str__(self):
        message = (
                f"command:[{self.command}]\n"
                f"ne:[{self.ne}]\n"
                f"executed_time_stamp:[{self.executed_time_stamp}]\n"
                f"o_m_id:[{self.o_m_id}]\n"
                f"result:[{self.result}]\n"
            )
        return message
