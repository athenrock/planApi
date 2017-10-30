# coding:utf-8
import os

ServerConfig = dict(
    port=8000
)

print ("path ", os.path.dirname(__file__))
app = dict(
    template_path=os.path.join(os.path.dirname(__file__), '../views'),
    static_path=os.path.join(os.path.dirname(__file__), '../static'),
    debug=True
)