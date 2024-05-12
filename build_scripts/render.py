#
# cd C:\Users\Zainab\Desktop\transport-site\build_scripts && python render_home_page.py

from jinja2 import Environment, FileSystemLoader
from os import sep
import yaml


env = Environment(loader=FileSystemLoader(f"..{sep}templates"))


"""
YAML files containing the data have a entry with same name as file name
Loading it returns a list of dicts, which are then passed to the templates,
where they are shown as required.
The logic is simple and similar enough for all pages to be served 
by the same function.
"""


def render_save_template(template_name, data_yaml=None):

    template = env.get_template(template_name)

    if data_yaml:
        with open(f"..{sep}templates{sep}data{sep}{data_yaml}") as file:
            all_data = yaml.safe_load(file)

        data = all_data[data_yaml.rstrip(".yaml")]

        rendered_content = template.render(data=data)

    else:
        rendered_content = template.render()

    with open(f"..{sep}site{sep}" + template_name, "w", encoding="utf-8") as file:
        file.write(rendered_content)


## static pages from /templates to be rendered into /site

render_save_template("index.html")
render_save_template("404.html")
render_save_template("contact.html")
render_save_template("careers.html", "jobs.yaml")
render_save_template("services.html", "services.yaml")
