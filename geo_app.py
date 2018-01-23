# print("This is the geo app")
# Webserver stuff

import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')


def make_app():
    return tornado.web.Application([
        (r"/Users/Welison/desktop/welison1/projectgeo", MainHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8889)
    tornado.ioloop.IOLoop.current().start()
