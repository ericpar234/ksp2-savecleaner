import json
import os
import argparse

def remove_extra_object_events(j):
    enc_list = []
    unique_items = []
    objects_removed = 0
    total_object_events = len(j["TravelLogData"]["ObjectEvents"])

    for idx, obj in enumerate(j["TravelLogData"]["ObjectEvents"]):
        enc = tuple(obj.items())
        if enc in enc_list:
            objects_removed = objects_removed + 1
        else:
            enc_list.append(enc)
            unique_items.append(obj)
            print("Unique ObjectEvent found {}".format(enc))
        
        if idx % 100000 == 0:
            print("{:.2f}% complete. Object Events removed: {}/{}".format((idx/total_object_events) * 100, objects_removed, total_object_events))

    print("Parsing Complete")
    print("Final Object Events removed: {}/{}".format(objects_removed, total_object_events))
    j["TravelLogData"]["ObjectEvents"] = unique_items
    return j

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Just an example",
                                    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("src", help="Source save file")
    parser.add_argument("dest", help="Destination save file")
    args = parser.parse_args()
    config = vars(args)

    print("Ericpar's KSP2 Save cleanser")

    starting_size = os.path.getsize(config["src"])
    print("Opening save: {}".format(config["src"]))
    with open(config["src"], 'r', encoding='utf-8') as f:
        j = json.load(f)
        remove_extra_object_events(j)

    print("Writing new save to: {}".format(config["dest"]))
    with open(config["dest"], 'w', encoding='utf-8') as f:
        f.write(json.dumps(j, indent=2))

    new_size = os.path.getsize(config["dest"])

    print("Old save size: {}".format(starting_size))
    print("New save size: {}".format(new_size))
    print("{} bytes removed from save!".format(starting_size - new_size))
    print("Fly Safe!")
