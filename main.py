import os
import shutil

import aspose.zip as az


def create_zip_archives(origin_dir: str, dirs_for_compress=tuple()):
    """
    По переданному в "origin_dir" пути формируются .zip папки, а оригинальные папки удаляются:
        1) если не указан параметр "dirs_for_compress", то все папки, находящиеся в директории;
        2) если параметр указан, то указанные в нем папки.
    Файлы/папки с расширениями игнорируются программой, сжатие в .zip папку происходит только для папок.
    """

    for sub_dir in os.listdir(origin_dir):

        if ((dirs_for_compress and sub_dir in dirs_for_compress) or (not dirs_for_compress)) and '.' not in sub_dir:
            with az.Archive() as archive:
                archive.create_entries(f'{origin_dir}\\{sub_dir}')
                archive.save(f'{origin_dir}\\{sub_dir}.zip')
            shutil.rmtree(f'{origin_dir}\\{sub_dir}')


def main():

    path = r'C:\Username\Desktop\ExampleFolder'
    dirs_for_compress = ('Photos from vacation', 'Songs')

    create_zip_archives(path, dirs_for_compress=dirs_for_compress)


if __name__ == '__main__':
    main()
