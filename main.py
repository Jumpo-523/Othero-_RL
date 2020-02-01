#!/bin/env python
# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web
import os
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Hello World/')

application = tornado.web.Application([
    (r'/', MainHandler),],
     template_path=os.path.join(os.getcwd(), "templates"),
     static_path=os.path.join(os.getcwd(), "static"),
     )


if __name__ == '__main__':
    application.listen(1234)
    tornado.ioloop.IOLoop.instance().start()
    import pandas as pd
    import pdb; pdb.set_trace()
    # test = pd.DataFrame({"hoge":[1,1,1,1,1]})
    # test.iloc(1)[1]