#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Usage: ./parser_mml.py [-h] input

import argparse

from result_mml import ResultMML

def mml_parser(file_path):
    # print(file_path)
    count = 0
    # ----------------------
    resul_mml = ResultMML()
    # ----------------------
    with open(file_path) as fp:
        for line in fp:
            # -------------------------------------------------------
            resul_mml.command_search(line)
            if resul_mml.command:
                print(f"command[{resul_mml.command}]")
            # -------------------------------------------------------
            count += 1
            print("Line{}: {}".format(count, line.strip()))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='File to process')
    parser.add_argument('input', type=str, help='Input file')
    # parser.add_argument('output', type=str, help='Output file')
    args = parser.parse_args()

    mml_parser(args.input)
