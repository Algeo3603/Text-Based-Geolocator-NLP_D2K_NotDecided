import json

with open("DATA/257.txt", "r") as inp_file:
    # print(inp_text)
    res = ""
    for line in inp_file:
        res += line
print(res)


with open("DATA/257.ann", "r") as ann_file:
    my_list = []
    for line in ann_file:
        if line.startswith("T"):
            sus = line.split()
            if sus[1] == "Literal":
                # place = " ".join(sus[4:])
                # print(place)
                my_list.append([int(sus[2]), int(sus[3]), "LOC"])
                
print(my_list)

# annotation_entry = [respestive_text, {"entities": respective_list}]
# data["annotations"].append(annotation_entry)

data = {
    "classes": ["LOC"],
    "annotations": [
        [res,
         {
             "entities": my_list
         } 
         ], 
         
    ]
}

annotation_entry = [res, {"entities": my_list}]
data["annotations"].append(annotation_entry)

                

with open("JSON/master.json", "w") as file:
    json.dump(data, file)