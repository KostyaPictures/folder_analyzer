import os
import json

def get_size(start_path = '.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)
    return total_size

def compact(v) -> str:
    if v>1073741824: #gb
        return f"{v//1073741824} GB"
    if v>1048576: #mb
        return f"{v//1048576} MB"
    if v>1024: #kb
        return f"{v//1024} KB"
    else:
        return f"{v} bytes"

while True:
    p=False
    while not p:
        try:
            path = input("input path: ")
            all_list = os.listdir(path)
            p=True
        except (FileNotFoundError, OSError):
            print("no such directory!")
            p=False


    file_list=[f for f in all_list if os.path.isfile(path+"/"+f)]
    folder_list=[f for f in all_list if not os.path.isfile(path+"/"+f)]

    all_list=[fl for fl in file_list]+[fd for fd in folder_list]
    all_size_list=[os.path.getsize(path+"/"+fl) for fl in file_list]+[get_size(path+"/"+fd) for fd in folder_list]
    all_size=sum(all_size_list)

    #print(all_list)
    #print(all_size_list)

    with open('config.json', 'r', encoding='utf-8') as file:
        content = json.load(file)
        do_small_files=content["do_small_files"]
        min_=content["min_"]
        alw_in_bytes=content["alw_in_bytes"]

    #print(all_size)

    if alw_in_bytes: print(f"  All size: {all_size} bytes")
    else: print(f"  All size: {compact(all_size)}")

    for i in range(len(all_list)):
        if do_small_files: print(f"{all_list[i]}: {round(all_size_list[i]/all_size*100, 2)}%     ({compact(all_size_list[i])})")
        else:
            if all_size_list[i]/all_size>min_:
                print(f"{all_list[i]}: {round(all_size_list[i]/all_size*100, 2)}%     ({compact(all_size_list[i])})")

    inp=input("\nPress any key to continue... (0 for exit)")
    if inp=="0":
        break