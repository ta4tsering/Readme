import os

from os.path import basename
from pathlib import Path
from zipfile import ZipFile


def create_base_zip(base_path):
    with ZipFile('base.zip', 'w') as zipObj:
        try:
            for folderName, subfolders, filenames in os.walk(base_path):
                for filename in filenames:
                    filePath = os.path.join(folderName, filename)
                    zipObj.write(filePath, basename(filePath))
                    print(filePath)
        except Exception as e:
            print(e)


if __name__=="__main__":
    base_path = Path(f'../P008165/P008165.opf/base')
    create_base_zip(base_path)
    
    


