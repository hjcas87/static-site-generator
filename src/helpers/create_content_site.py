import os
import shutil


def create_content_site(dir_path_docs):
    if os.path.exists(dir_path_docs):
        shutil.rmtree(dir_path_docs)
    os.mkdir(dir_path_docs)
    if os.path.exists("static"):
        r_static_gen("static", dir_path_docs)


def r_static_gen(src_dir_path: str, dest_dir_path: str):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)
    list_of_items = os.listdir(src_dir_path)

    for item_name in list_of_items:
        full_src_path = os.path.join(src_dir_path, item_name)

        full_dest_path = os.path.join(dest_dir_path, item_name)

        if os.path.isfile(full_src_path):
            shutil.copy(full_src_path, dest_dir_path)
            # print(
            #     f"Copiando archivo: {full_src_path} a {dest_dir_path}"
            # )
        elif os.path.isdir(full_src_path):
            os.mkdir(full_dest_path)
            r_static_gen(full_src_path, full_dest_path)
            # print(f"Creando directorio: {full_dest_path}")
