import os

directory = "src/uix/elements"
init_file = "src/uix/elements/__init__.pyi" 

def create_init_file(directory, init_file):
    with open(init_file, "a+") as init:
        init.seek(0)  
        existing_content = init.read()
        for filename in os.listdir(directory):
            if filename.endswith(".py"): 
                file_path = os.path.join(directory, filename)
                with open(file_path, "r") as module_file:
                    file_content = module_file.read()
                    desc_start = file_content.find('description') 
                    desc_end = file_content.find('sample') 
                    init_start = file_content.find('def __init__')
                    init_end = file_content.find(':', init_start)
                    if desc_start != -1 and desc_end != -1 and init_start != -1 and init_end != -1:
                        description = file_content[desc_start + 13:desc_end].strip()
                        init_func = file_content[init_start:init_end].strip()
                        if description not in existing_content and init_func not in existing_content:
                            init.write("from uix.elements." + filename[:-3] + " import " + filename[:-3] + "\n")
                            init.write("class " + filename[1:-3] + "(Element):\n")
                            init.write("    " + description + "\n")
                            init.write("    " + init_func + "-> None: ..." + "\n")
               
             

create_init_file(directory, init_file)
