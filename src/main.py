import os
import sys
from src.helpers.generate_page import generate_pages_recursive
from src.helpers.extract_title import extract_title
from src.helpers.create_content_site import create_content_site



dir_path_docs = "./docs"
dir_path_content = "./content"
template_path = "./template.html"


def main():
    basepath = "/" if len(sys.argv) < 2 else sys.argv[1]
    print(basepath)
    create_content_site(dir_path_docs)
    print("Generating page...")
    generate_pages_recursive(dir_path_content, template_path, dir_path_docs, basepath)


if __name__ == "__main__":

    main()
