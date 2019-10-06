#!/usr/bin/env python

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import BaseHTTPServer
import ssl
#from bottle import route, run, template

#@route('/*')
#def index():
#  return '<b>Eric\'s GCP VM</b>!'

class myHandler(BaseHTTPServer.BaseHTTPRequestHandler):
  #Handler for the GET requests
  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type','text/html')
    self.end_headers()
    self.wfile.write('<b>Eric\'s GCP VM Python Server!</b>!')
    return

httpd = BaseHTTPServer.HTTPServer(('0.0.0.0', 443), myHandler)
#                                  handler_class=BaseHTTPServer.BaseHTTPRequestHandler)

httpd.socket = ssl.wrap_socket (httpd.socket,
        keyfile="./ssl_cert/server.key",
        certfile='./ssl_cert/server.crt', server_side=True)

httpd.serve_forever()
