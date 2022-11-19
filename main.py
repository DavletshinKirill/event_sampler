from app import create_app
from flask import template_rendered, got_request_exception, before_render_template

app = create_app()


@template_rendered.connect_via(app)
def when_template_rendered(*args, **extra):
    print("template_rendered.")


@got_request_exception.connect_via(app)
def when_template_rendered():
    print("got_request_exception")


@app.before_request
def when_template_rendered():
    print("before_request")


@before_render_template.connect_via(app)
def when_template_rendered(sender, template, context, **extra):
    print("before_render_template")


if __name__ == "__main__":
    app.run()
