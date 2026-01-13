from src.helpers.markdown_to_html_node import markdown_to_html_node


def extract_title(markdown: str):
    content = markdown.split("\n")
    for block in content:
        title = block.strip()
        if title.startswith("# "):
            title = title.split("# ", 1)
            return title[1].strip()
    raise Exception(
        "Header not found. Please ensure a header is present in the content."
    )
