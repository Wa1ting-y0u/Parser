from parser import Parser

if __name__ == '__main__':
    hrefs = Parser.get_hrefs()
    Parser.get_titles(hrefs)

    # titles = Parser.get_titles(hrefs)