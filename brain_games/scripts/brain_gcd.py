#!/usr/bin/env python3

from brain_games import brain_engine
from brain_games.games import gcd


def main():
    brain_engine.run_engine(gcd)


if __name__ == '__main__':
    main()
