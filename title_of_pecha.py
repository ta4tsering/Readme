import json
import yaml
from pathlib import Path

            
def get_title(meta):
    if meta['source_metadata']['title'] != None:
        title = meta['source_metadata']['title']
        return title
    else:
        return None
def create_json(title):
    meta = {
                "description": f"{title}",
                "homepage": "https://github.com/ta4tsering/P0081656",
                "keywords": [
                    "sync",
                    "repo",
                    "metadata",
                    "npm",
                    "nuget",
                    "description",
                    "homepage",
                    "website",
                    "topics",
                    "keywords"
                ]
            }
    return meta

if __name__=='__main__':
    pecha_id = 'P005633'
    meta_yml_content = Path(f"./{pecha_id}/{pecha_id}.opf/meta.yml").read_text(encoding="utf-8")
    meta_content = yaml.safe_load(meta_yml_content)
    title = get_title(meta_content)
    meta_path = Path(f"./metadata")
    meta_path.mkdir(exist_ok=True, parents=True)
    meta = create_json(title)
    with open(f'{meta_path}/meta.json', 'w') as f:
        json.dump(meta, f)