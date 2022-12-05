from parsers.lalafo_parser import LalafoParser


def main():
    pehe = LalafoParser()
    pehe.update()
    print(pehe.all_ads)


if __name__ == '__main__':
    main()
