import re
import json
raw_code = ""
with open("F:/python/challenge/reading.py","r") as python_file:
    data = python_file.read()
    for line in data.split("\n"):
        line = line + "\\n" +','
        line = re.sub('"','\\"',line)
        raw_code = raw_code + line
    

with open("yahoo_live_rl_test.py",'r') as python_file:
    data = python_file.read()    
    data_list = data.split("\n")
    raw_data = ""
    for i in data_list:
        x= re.search("^#",i)
        if x:
            data_list.remove(i)
        else:
            continue
    for line in data_list:
        raw_data= raw_data + line + "\n" +','    
    

with open("json_notebook.ipynb",'r+') as notebook:
    notebook_content = notebook.read()
    notebook_content.replace('"source": []','"source: [{0}]"'.format(raw_code))
    
    
