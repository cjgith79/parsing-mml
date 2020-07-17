#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Usage: ./parser_mml.py [-h] input

import argparse

from result_mml import ResultMML

def mml_parser(file_path):
    # print(file_path)
    count = 0
    # ----------------------
    result_mml = ResultMML(None)
    # ----------------------
    with open(file_path) as fp:
        for line in fp:
            # -------------------------------------------------------
            # result_mml.command_search(line, count)
            # if result_mml.command:
            #     print(f"command[{result_mml.command}]")

            # if not result_mml.command: # command not detected yet
            #     result_mml.command_search(line, count)
            #     if result_mml.command:
            #         print(f"command[{result_mml.command}]")
            # else:

            '''
            Siempre debo mirar por "MML Command-----"
            Si se detecta
                Si ya estaba lleno ->
                    devolver el objeto (yield ?)
                    reiniciar objeto con nuevo comando detectado
                Si objeto.ne está vacío
                    ver si se detecta ne
                ...
            '''
            command_ = result_mml.command_search(line)
            if command_:
                print(result_mml) # yield maybe
                result_mml = ResultMML(command_)

            # -------------------------------------------------------
            count += 1
            print("Line{}: {}".format(count, line.strip()))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='File to process')
    parser.add_argument('input', type=str, help='Input file')
    # parser.add_argument('output', type=str, help='Output file')
    args = parser.parse_args()

    mml_parser(args.input)
