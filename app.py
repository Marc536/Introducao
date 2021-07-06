import web
import sys
from web import form

render = web.template.render('templates/')

urls = ('/', 'hello')
app = web.application(urls, globals())

myform = form.Form(
    form.Textbox("Input")
)

class hello:
    def __init__(self):
        self.model = ""
        self.stdout_console = sys.stdout

    def GET(self):
        form = myform()
        return render.World(form)

    def POST(self):
        form = myform()
        if not form.validates(): 
            return render.World(form)
        else:
            self.model = form['Input'].value
            self.stdout_console.write(form['Input'].value + "\n")
            return render.World(form)

if __name__ == "__main__":
    web.internalerror = web.debugerror
    app.run()
