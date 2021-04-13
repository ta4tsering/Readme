from antx import transfer
from pathlib import Path
from openpecha.serializers import HFMLSerializer
import re

def get_hfml(opf_path):
    serializer = HFMLSerializer(opf_path, layers=["Pagination"])
    serializer.apply_layers()
    results = serializer.get_result()
    return result
    

if __name__=="__main__":
    opf_path = Path(f"../P000005/P000005.opf")
    # hfml_path =Path(f"./hfml")
    hfml = get_hfml(opf_path,)
    Path(f"./hfml").write_text(hfml, encoding='utf-8')
    
