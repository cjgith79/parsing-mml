#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Usage: ./parser_mml.py [-h] input

import argparse

from result_mml import ResultMML

def mml_parser(file_path):
    '''
    This program receives a MML file that contains the results
    of commands executed over U2020 and print all ResultMML
    objects found.
    '''
    # print(file_path)
    # count = 0
    result_mml = ResultMML(None)
    with open(file_path) as fp:
        for line in fp:
            command_ = result_mml.command_search(line)
            if command_:
                if result_mml.command:
                    print(result_mml) # yield maybe
                result_mml = ResultMML(command_)
            result_mml.fields_search(line)
            # count += 1
            # print("Line{}: {}".format(count, line.strip()))
    if result_mml.command:
        print(result_mml) # yield maybe

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='File to process')
    parser.add_argument('input', type=str, help='Input file')
    # parser.add_argument('output', type=str, help='Output file')
    args = parser.parse_args()

    mml_parser(args.input)
