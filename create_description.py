        
        - name: Set up Python ${{ matrix.python-version }}
          uses: actions/setup-python@v2
          with:
            python-version: ${{ matrix.python-version }}

        - name: Get readme title
          run: |
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
                pecha_id = Path.cwd().name
                meta_yml_content = Path(f"../{pecha_id}/{pecha_id}.opf/meta.yml").read_text(encoding="utf-8")
                meta_content = yaml.safe_load(meta_yml_content)
                title = get_title(meta_content)
                meta = create_json(title)
                json_object = json.dumps(meta, indent = 4)
                with open("metadata.json", "w") as outfile:
                    outfile.write(json_object)

          shell: python

        - name: get Path
          run: |
            from pathlib import Path

            if __name__=="__main__":
              path_name = Path.cwd()
              print(path_name)
            