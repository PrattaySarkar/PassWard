# PassWard/cli.py

from .passward import passgen
import argparse
import pyperclip


def main():
    parser = argparse.ArgumentParser(description='Generate a random password.')
    parser.add_argument('--length', type=int, default=12, help='Password Length')
    parser.add_argument('--no-numbers', dest='use_numbers', action='store_false', help='Exclude numbers')
    parser.add_argument('--no-symbols', dest='use_symbols', action='store_false', help='Exclude symbols')

    args = parser.parse_args()
    password = passgen(args.length, args.use_numbers, args.use_symbols)

    print('Generated Password:', password)
    qs = input("Do you want to Capy This to Clipboard? (Y/N): ")

    if qs.upper() == "Y":
        pyperclip.copy(password)
        print('Password copied to clipboard.')
    else:
        quit(0)
