import textile
import tornado.escape as tornado

if __name__ == '__main__':


    with open('x.text', 'r') as f:
        lines = f.readlines()

    s = "".join(lines)
    print(s)

    """
    with open('textile.html', 'w') as f:
        f.write(textile.textile(s))
    """
    print(tornado.xhtml_unescape(tornado.linkify(s).replace("\n", "\n<br>")))
