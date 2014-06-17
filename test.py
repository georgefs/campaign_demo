import jinja2
from jinja2 import Template
import os

loader_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
loader=jinja2.FileSystemLoader(loader_path)



template = Template('''
{% extends "layout.html" %}
{% from 'modules.html' import basecss, basejs, housecss, housejs %}

{% block css %}
    {{basecss()}} 
    {{housecss()}} 
{% endblock %}


{% block js %}
    {{basejs()}} 
    {{housejs()}} 
{% endblock %}
''')
template.environment.loader = loader
v = {}
print template.render(v)

