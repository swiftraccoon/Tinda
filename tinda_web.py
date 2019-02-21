# http://webpy.org/docs/0.3/tutorial

import web
from web import tinder_api

web.config.debug = False
render = web.template.render('templates', base='index')

urls = (
  '/(.*)', 'index'
)


class index:
    def GET(self, tinder_token):
        self_profile = tinder_api.get_self()
        return render.index(self_profile, tinder_token)


app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()
