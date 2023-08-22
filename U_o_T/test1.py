dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}


def merge_dictionaries(dict1,dict2):
    merged_dicts = {}
    for key in dict1:
        if key in merged_dicts:
            merged_dicts[key]+= dict1[key]
        else:
            merged_dicts[key]=dict1[key]
    for key in dict2:
        if key in merged_dicts:
            merged_dicts[key]+= dict2[key]
        else:
            merged_dicts[key]= dict2[key]
    return merged_dicts

print(dict1)
print(dict2)
print(merge_dictionaries(dict1,dict2))
