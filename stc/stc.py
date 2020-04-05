#!/usr/bin/env python3

import getopt
import sys

from tvchannels import TVChannels


def usage():
    print(
        '\nUsage:\n\n' +
        'stc.py <URL> [--config=config file] [--ofile=file]\n'
    )
    sys.exit()


def main(argv):
    try:
        opts, args = getopt.getopt(
            argv, 'hco:', ['help', 'config=', 'ofile=']
        )
    except getopt.GetoptError:
        usage()

    config_file = ''
    output_file = ''

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            usage()
        elif opt in ('-c', '--config'):
            config_file = arg
        elif opt in ('-o', '--ofile'):
            output_file = arg
        else:
            print(f'/nInvalid parameter: {opt}/n')
            usage()

    # Set defaults
    if config_file == '':
        config_file = 'iptv.yaml'
    if output_file == '':
        config_file = 'iptv.m3u8'

    TVChannels(sys.argv[1], config_file, output_file)


if __name__ == '__main__':
    if len(sys.argv) > 0:
        main(sys.argv[1:])
    else:
        usage()
