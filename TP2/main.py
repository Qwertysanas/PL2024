import sys
import re

h1 = (r"^#{1} ([^\n]*)")
h2 = (r"^#{2} ([^\n]*)")
h3 = (r"^#{3} ([^\n]*)")
b = (r"\*{2}([^*]*)\*{2}")
it = (r"\*{1}([^*]+)\*{1}")
li = r"(?:1. ([^\n]*))"
ln = r"(?:\d+. ([^\n]*))"
lb = False
l = r"\[([^\]]*)\]\(([^\)]*)\)"
im = r"!\[([^\]]*)\]\(([^\)]*)\)"


def replace(str):
    global lb
    if (re.match(li, str) and not lb):
        str = re.sub(li, lambda x: "<ol>\n<li>" + x[1] + "</li>", str)
        lb = True
    elif (re.match(ln, str) and lb): 
        str = re.sub(ln, lambda x: "<li>" + x[1] + "</li>", str)
    elif lb:
        str = "</ol>\n" + str
        lb = False
    str = re.sub(b, lambda x: "<b>" + x[1] + "</b>", str)
    str = re.sub(it, lambda x: "<i>" + x[1] + "</i>", str)
    str = re.sub(im, lambda x: '<img src="' + x[2] + '" alt="' + x[1] + '">', str)
    str = re.sub(l, lambda x: '<a href="' + x[2] + '">' + x[1] + "</a>", str)
    if re.match(h1, str) != None:
        return re.sub(h1, r"<h1>\1</h1>", str)
    if re.match(h2, str) != None:    
        return re.sub(h2, r"<h2>\1</h2>", str)
    if re.match(h3, str) != None:    
        return re.sub(h3, r"<h3>\1</h3>", str)    
    return str

def main(inp):
    if (len(inp) == 1):
        for l in sys.stdin:
            print(replace(l), end="")
    else:
        file = open(inp[1])
        for l in file:
            print(replace(l), end="")
    return

if __name__ == "__main__":
    main(sys.argv)