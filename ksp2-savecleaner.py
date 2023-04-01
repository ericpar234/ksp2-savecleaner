import json
import os

file_name = 'original.json'
new_file_name = 'edited.json'

starting_size = os.path.getsize(file_name)

def remove_extra_object_events_old(j):
    ut_list = []
    unique_object_events = []
    objects_removed = 0
    total_object_events = len(j["TravelLogData"]["ObjectEvents"])
    for idx, obj in enumerate(j["TravelLogData"]["ObjectEvents"]):
        if obj['UT'] in ut_list:
            #j["TravelLogData"]["ObjectEvents"].pop(idx)
            objects_removed = objects_removed + 1
        else:
            ut_list.append(obj['UT'])
            unique_object_events.append(obj)
            print("Unique ObjectEvent found {}".format(obj['UT']))
        
        if idx % 10000 == 0:
            print("Object Events removed: {}/{} {:.2f}%".format(objects_removed, total_object_events, (objects_removed/total_object_events) * 100))
    
    j["TravelLogData"]["ObjectEvents"] = unique_object_events
    print("Final Object Events removed: {}/{}".format(objects_removed, total_object_events))
    return j

def remove_extra_object_events(j):
    ut_list = []
    objects_removed = 0
    total_object_events = len(j["TravelLogData"]["ObjectEvents"])
    for idx, obj in enumerate(j["TravelLogData"]["ObjectEvents"]):
        if obj['UT'] in ut_list:
            j["TravelLogData"]["ObjectEvents"].pop(idx)
            objects_removed = objects_removed + 1
        else:
            ut_list.append(obj['UT'])
            print("Unique ObjectEvent found {}".format(obj['UT']))
        
        if idx % 10000 == 0:
            print("Object Events removed: {}/{} {:.2f}%".format(objects_removed, total_object_events, (objects_removed/total_object_events) * 100))

    print("Final Object Events removed: {}/{}".format(objects_removed, total_object_events))
    return j

if __name__ == "__main__":
    print("Ericpar's KSP2 Save cleanser")

    print("Opening save: {}".format(file_name))
    with open(file_name, 'r', encoding='utf-8') as f:
        j = json.load(f)
        remove_extra_object_events(j)

    print("Writing new save to: {}".format(new_file_name))
    with open(new_file_name, 'w', encoding='utf-8') as f:
        f.write(json.dumps(j, indent=2))

    new_size = os.path.getsize(file_name)

    print("Old save size: {}".starting_size)
    print("New save size: {}".new_size)
    print("{} bytes removed from save!".format(starting_size - new_size))
    print("Fly Safe!")
