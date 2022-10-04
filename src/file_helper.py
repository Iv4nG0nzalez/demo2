from datetime import date
import os
from pathlib import Path

def search_asset_by_status(path, extension):
    output = []
    for root, dirs, files  in os.walk(path):
        files_full_name = [ os.path.join(root, f) for f in files if f.endswith(extension) ]
        output.extend(files_full_name)
    return output


def read_attendance_report_file(path_list):
    ## it defines a block of code where file is valid
    file = None
    datas = []

    for path in path_list:
        try:
            with open(path, 'r') as file:
                data = file.readlines()
        # todo 
                datas.append(data) 
        ## in the happy path escenario outside of with block file is "closed" already; with block guarantees that
        except Exception as exception:
            print(f'Error while reading file {path}: {exception}')
            return 

    if datas is None:
        return []
    else:
        return datas            

Path = "/home/oem/workspace/jala-python/dev_demos/demo2/test_files"


list_path = search_asset_by_status(Path, "json")

lista = read_attendance_report_file(list_path)

print(lista)