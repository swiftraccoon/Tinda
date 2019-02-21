# http://webpy.org/docs/0.3/tutorial

import web

render = web.template.render('templates/')

urls = (
  '/(.*)', 'index'
)


class index:
    def GET(self, tinder_token):
        return render.index(tinder_token)


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
