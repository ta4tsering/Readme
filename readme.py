import csv
import re
import yaml
from github import Github
from pathlib import Path


def update_repo(g, pecha_id, file_path, commit_msg, new_content):
    try:
        repo = g.get_repo(f"ta4tsering/{pecha_id}")
        contents = repo.get_contents(f"{file_path}", ref="main")
        repo.update_file(contents.path, commit_msg , new_content, contents.sha, branch="main")
        print(f'{pecha_id} update completed..')
    except:
        print('Repo not found')


def get_updated_readme(pecha_id, meta_title, meta_author, meta_bdrcid):
    opecha = f"|Openpecha | {pecha_id}"
    table = f"|---	   |---	"
    title = f"|Title:    |{meta_title}"
    if meta_author != None:
        author= f"|   Author:   |{meta_author}"
    else:
        author= f"|   Author:   |"
    bdrcid =f"|BDRC ID:  |{meta_bdrcid}"
    plain_text= f"|Plain Text:|![](https://img.icons8.com/color/20/000000/txt.png) <a href='https://github.com/ta4tsering/P008165/releases/download/v102/P008165_base.zip' class='button'>Download</a>"
    text_with_pagination = f"|Text with Pagination:|![](https://img.icons8.com/color/20/000000/txt.png) <a href='https://github.com/ta4tsering/P008165/releases/download/v102/P008165_hfml.zip' class='button'>Download</a>"
    in_editor = f'|Open in Editor:|[<img width="25" src="https://img.icons8.com/color/25/000000/edit-property.png"> Open in Editor](http://editor.openpecha.org/{pecha_id})'
    bdrc_link = f'|Images Link:|[<img width="25" src="https://library.bdrc.io/icons/BUDA-small.svg"> Images of text file open in BUDA](https://library.bdrc.io/show/bdr:{meta_bdrcid})'
    new_readme = f"{opecha}\n{table}\n{title}\n{author}\n{bdrcid}\n{plain_text}\n{text_with_pagination}\n{in_editor}\n{bdrc_link}\n"
    return new_readme

def get_metadata_info(metadata):
    meta_bdrcid = metadata['source_metadata']['id'][4:]
    if metadata['source_metadata']['author'] != '':
        meta_title = metadata['source_metadata']['title']
        meta_author = metadata['source_metadata']['author']
        return meta_title, meta_author, meta_bdrcid
    else:
        meta_title = metadata['source_metadata']['title']
        return meta_title, None, meta_bdrcid

def get_meta(g, pecha_id):
    try:
        repo = g.get_repo(f"ta4tsering/{pecha_id}")
        contents = repo.get_contents(f"{pecha_id}.opf/meta.yml")
        return contents.decoded_content.decode()
    except:
        print('Repo Not Found')
        return ''


if __name__=="__main__":
    file_path = "./README.md"
    commit_msg = 'bdrc link added in readme'
    token = "e1cb6529dac22e62efb1df93222e757e851721b4"
    g = Github(token)
    # with open("catalog.csv", newline="") as csvfile:
    #     pechas = list(csv.reader(csvfile, delimiter=","))
    #     for pecha in pechas[278:]:
            # pecha_id = re.search("\[.+\]", pecha[0])[0][1:-1]
    pecha_id = 'P008165'
    meta = get_meta(g, pecha_id)
    metadata = yaml.safe_load(meta)
    meta_title, meta_author, meta_bdrcid = get_metadata_info(metadata)
    new_content = get_updated_readme(pecha_id, meta_title, meta_author, meta_bdrcid)
    update_repo(g, pecha_id, file_path, commit_msg, new_content)
