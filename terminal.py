import subprocess
import requests
from zipfile import ZipFile
import shutil
import os
import time

while True:
    con = '924'
    list_accont_li = 'you{}'.format(con)
    repository_url = 'https://github.com/theloveme1236/{}'.format(list_accont_li)
    destination_folder = 'file'

    if os.path.exists(destination_folder):
        shutil.rmtree(destination_folder)

    if os.path.exists(destination_folder):
        os.mkdir(destination_folder)

    zip_url = repository_url + '/archive/main.zip'


    response = requests.get(zip_url)
    zip_filename = os.path.join('repository.zip')

    with open(zip_filename, 'wb') as zip_file:
        zip_file.write(response.content)


    with ZipFile(zip_filename, 'r') as zip_ref:
        zip_ref.extractall(destination_folder)
    os.remove(zip_filename)

    os.chdir(r'{}/{}-main'.format(destination_folder, list_accont_li))
    time.sleep(2)
    python_file = "pinterest.py"
    command = f"lxterminal -e 'bash -c \"python {python_file}\"'"


    try:
        subprocess.run([command], shell=True, check=True)
    except subprocess.CalledProcessError:
     
        continue
    
