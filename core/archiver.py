import os
import shutil

import aspose.zip as zp


def zip_files(
        origin_dir_path: str,
        delete_origin_non_zip_file: bool = False
):
    for sub_dir in os.listdir(origin_dir_path):
        if not sub_dir.endswith(".zip"):
            with zp.Archive() as archive:
                archive.create_entries(f"{origin_dir_path}\\{sub_dir}")
                archive.save(f"{origin_dir_path}\\{sub_dir}.zip")
                if delete_origin_non_zip_file:
                    shutil.rmtree(f"{origin_dir_path}\\{sub_dir}")

def unzip_file(
        origin_file_path: str,
        save_unzip_file_path: str,
        delete_origin_zip_file: bool = False
):
    print(origin_file_path)
    with zp.Archive(origin_file_path) as archive:
        archive.extract_to_directory(save_unzip_file_path)
    if delete_origin_zip_file:
        os.remove(origin_file_path)
