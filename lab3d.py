#!/usr/bin/env python3
#AuthorID: Ian Mills imills

import subprocess

def free_space():
    command = "df -h | grep '/$' | awk '{print $4}'"
    # create a subprocess.Popen object here
    p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    # run the df/grep/awk command here
    output = p.communicate()
    # capture the output using communicate()
    # decode the byte output using .decode('utf-8')
    # strip the newline using .strip()
    stdout = output[0].decode('utf-8').strip()
    # return the final string
    return stdout


if __name__ == '__main__':
    print(free_space())