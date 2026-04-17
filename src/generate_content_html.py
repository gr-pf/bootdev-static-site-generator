import re
from pathlib import Path

from markdown_blocks import markdown_to_html_node


def extract_title(markdown):
    pattern = r"^# .+$"
    matches = re.findall(pattern, markdown, re.MULTILINE)
    if not matches:
        raise Exception("There is no Title")
    if len(matches) > 1:
        raise Exception("Error: mutliple titles.")
    header = matches[0]

    return header[2:]


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r", encoding="utf-8") as file:
        md = file.read()
    with open(template_path, "r", encoding="utf-8") as file:
        template = file.read()
    content = markdown_to_html_node(md).to_html()
    title = extract_title(md)
    full_html = template.replace("{{ Title }}", title).replace("{{ Content }}", content)
    make_parent_dir(dest_path)
    with open(dest_path, "w", encoding="utf-8") as file:
        file.write(full_html)


def make_parent_dir(path_str):
    path = Path(path_str)
    if not path.parent.exists():
        make_parent_dir(path.parent)
        path.parent.mkdir()
