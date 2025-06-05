import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[0])) 
sys.path.append(str(Path(__file__).resolve().parents[1])) 
sys.path.append(str(Path(__file__).resolve().parents[2])) 
sys.path.append(str(Path(__file__).resolve().parents[3])) 
sys.path.append(str(Path(__file__).resolve().parents[4])) 
sys.path.append(str(Path(__file__).resolve().parents[5])) 

from vicmil_pip.packages.cppBuild import *


def find_files_by_name(root_dir, filename):
    matching_files = []

    for dirpath, dirnames, filenames in os.walk(root_dir):
        for file in filenames:
            if file == filename:
                full_path = os.path.abspath(os.path.join(dirpath, file))
                matching_files.append(full_path)

    return matching_files


def include_font(build_setup: BuildSetup, font_name: str):
    # Find a file named font_name inside /data/*
    font_path = find_files_by_name(get_directory_path(__file__) + "/data", font_name)
    if len(font_path) != 1:
        print(f"Invalid font: {font_name}, expected 1, found {len(font_path)} instances")
        return

    include_path = get_directory_path(__file__) + "/data/include/"
    header_path = include_path + font_name.replace(" ", "_") + ".hpp"
    cpp_path = include_path + font_name.replace(" ", "_") + ".cpp"

    os.makedirs(include_path, exist_ok=True)

    build_setup.n2_cpp_files.append(cpp_path)

    if not os.path.exists(header_path):
        # Convert it to a header and store the result under data/headers
        convert_file_to_cpp(font_path[0], include_path)