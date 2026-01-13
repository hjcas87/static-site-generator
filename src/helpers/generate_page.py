import os

from src.helpers.extract_title import extract_title
from src.helpers.markdown_to_html_node import markdown_to_html_node


def generate_page(from_path, template_path, dest_path, basepath):
    print(f" * {from_path} {template_path} -> {dest_path}")

    with open(from_path, "r") as from_file:
        markdown_content = from_file.read()

    with open(template_path, "r") as template_file:
        template = template_file.read()

    node = markdown_to_html_node(markdown_content)
    html = node.to_html()

    title = extract_title(markdown_content)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)
    template = template.replace('href"=/', f'href="{basepath}')
    template = template.replace('src"=/', f'src="{basepath}')

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)

    with open(dest_path, "w") as to_file:
        to_file.write(template)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    paths = os.listdir(dir_path_content)
    for p in paths:
        if os.path.isdir(os.path.join(dir_path_content, p)):
            generate_pages_recursive(
                os.path.join(dir_path_content, p),
                template_path,
                os.path.join(dest_dir_path, p),
                basepath
            )
        else:
            if not p.endswith(".md"):
                continue
            name, _ = os.path.splitext(p)
            generate_page(
                os.path.join(dir_path_content, p),
                template_path,
                os.path.join(dest_dir_path, f"{name}.html"),
                basepath
            )
