#!/usr/bin/env python

import os, shutil, json
"""from jinja2 import Environment, FileSystemLoader

PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    loader=FileSystemLoader(os.path.join(PATH, 'templates')),
    trim_blocks=False)

def render_template(template_filename, context):
    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)"""


def create_index_html():
    fname = "out/output.html"
    context = {}
    with open("json/projekte/projekte.json") as projectfile:
        context["projects"] = json.load(projectfile)
    with open("json/pictures/pictures_b.json") as projectfile:
        context["pictures"] = json.load(projectfile)
    with open("js/project.js") as tempfile:
        tmp = tempfile.read()
        tmp = tmp.replace("{{CONTEXT}}", json.dumps(context))
        with open("out/js/project.js", "w") as outfile:
            outfile.write(tmp)
    shutil.copy("templates/index.html", "out/output.html")

def prepare():
    if os.path.isdir("out"):
        shutil.rmtree("out")
    os.mkdir("out")

def copy_assets():
    shutil.copytree("css", "out/css")
    shutil.copytree("js", "out/js")

def main():
    prepare()
    copy_assets()
    create_index_html()


########################################

if __name__ == "__main__":
    main()