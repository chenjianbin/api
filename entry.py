#!/usr/bin/env python
import flask

app = flask.Flask(__name__)
app.config.from_object('config.config.Database')

#if __name__ == '__main__':
#	APP.run()
