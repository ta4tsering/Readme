import git 
import re 

from git import Repo 
from github import Github 
from pathlib import Path
from openpecha.serializers import HFMLSerializer

config = {
    "OP_ORG": "https://github.com/Openpecha"
}


def get_branch(repo, branch):
    if branch in repo.heads:
        return branch
    return "master"


def download_pecha(pecha_id, out_path=None, needs_update=True, branch="master"):
    pecha_url = f"{config['OP_ORG']}/{pecha_id}.git"
    out_path = Path(out_path)
    out_path.mkdir(exist_ok=True, parents=True)
    pecha_path = out_path / pecha_id
    if pecha_path.is_dir():
        return pecha_path
    else:
        print(f"Downloading {pecha_id} ...")
        Repo.clone_from(pecha_url, str(pecha_path))
        repo = Repo(str(pecha_path))
        branch_to_pull = get_branch(repo, branch)
        repo.git.checkout(branch_to_pull)
        return pecha_url  

def write_hfml(content, hfml_path, vol_num):
    out_fn = Path(f"{hfml_path}/{vol_num}.txt")
    out_fn.write_text(content)
    print("Done")

def get_clean_hfml(lines):
    new_line = []
    new_content = ""
    for num, line in enumerate(lines,1):
        if  num % 2 != 0:
            new_line = re.sub(f"(\[\.\d+\])", "", line )
            new_content += new_line
            new_line = []
        else:
            new_content += "\n"
    return new_content

if __name__=='__main__':
    token = "e1cb6529dac22e62efb1df93222e757e851721b4"
    g = Github(token)
    pecha_id = 'P005633'
    hfml_path = Path(f"./output/publication")
    hfml_path.mkdir(exist_ok=True, parents=True)
    file_path = './'
    pecha_path = download_pecha(pecha_id, file_path)
    opf_path = Path(f'./{pecha_id}/{pecha_id}.opf')
    serializer = HFMLSerializer(opf_path, layers=["Pagination"])
    serializer.apply_layers()
    results = serializer.get_result()
    hfml = results
    for num, vol_num in enumerate(hfml,1):
        content = hfml[f'{vol_num}']
        lines = re.split(f"(\\\n)", content)
        new_hfml = get_clean_hfml(lines)
        write_hfml(new_hfml, hfml_path,vol_num)
    
