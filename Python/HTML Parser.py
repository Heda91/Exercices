import sys, re
from html.parser import HTMLParser

sys.stdin = open("HTML Parser.txt")  # to delete

data = str(sys.stdin.buffer.read(), 'utf-8').splitlines()


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for k, v in attrs:
            print(f"-> {k} > {v}")

    def handle_endtag(self, tag):
        print("End   :", tag)

    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        for k, v in attrs:
            print(f"-> {k} > {v}")

    def handle_comment(self, data):
        if re.search(r'\n', data) is None:
            print(">>> Single-line Comment")
        else:
            print(">>> Multi-line Comment")
        print(data)

    def handle_data(self, data):
        if re.fullmatch(r'[\n ]*', data) is None:
            sub = re.sub(r'^[\n ]*', '', data)
            sub = re.sub(r'(?<=[\n ])[\n ]+', '', sub)
            sub = re.sub(r'[\n ]*$', '', sub)
            print(">>> Data\n" + sub)


parser = MyHTMLParser()
parser.feed('\n'.join(data[1:]))
parser.close()
