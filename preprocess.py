import json
import os
import os.path

data = {
    "classes": ["LOC"],
    "annotations": []
}

for file_number in range(0, 369):
    txt_file_path = f"DATA/{file_number}.txt"
    ann_file_path = f"DATA/{file_number}.ann"

    if os.path.isfile(txt_file_path) == False:
        continue


    with open(txt_file_path, "r") as inp_file:
        text = ""
        for line in inp_file:
            text += line

    with open(ann_file_path, "r") as ann_file:
        labels = []
        for line in ann_file:
            if line.startswith("T"):
                sus = line.split()
                if sus[1] == "Literal":
                    labels.append([int(sus[2]), int(sus[3]), "LOC"])

    annotation_entry = [text, {"entities": labels}]
    data["annotations"].append(annotation_entry)

                

with open("JSON/master.json", "w") as file:
    json.dump(data, file)