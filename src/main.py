from src.helpers.generate_page import generate_page
from src.helpers.extract_title import extract_title
from src.helpers.create_content_site import create_content_site

def main():
    # create_content_site()
    generate_page("content", "template.html", "public")

if __name__ == "__main__":

    main()
