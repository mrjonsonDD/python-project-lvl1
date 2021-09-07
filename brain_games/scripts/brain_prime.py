#!/usr/bin/env python3

from brain_games import brain_engine
from brain_games.games import prime


def main():
    brain_engine.run_engine(prime)


if __name__ == '__main__':
    main()
