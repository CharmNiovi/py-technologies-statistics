import asyncio

from parsing.parse_dou import parse_and_save_dou


def main():
    asyncio.run(parse_and_save_dou())


if __name__ == '__main__':
    main()
