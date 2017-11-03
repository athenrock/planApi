# coding:utf-8
import os

ServerConfig = dict(
    port=8000
)

app = dict(
    template_path=os.path.join(os.path.dirname(__file__), '../views'),
    static_path=os.path.join(os.path.dirname(__file__), '../static'),
    debug=True
)