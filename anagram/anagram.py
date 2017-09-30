def detect_anagrams(string, array):
    sorted_string_list = sorted(list(string.lower()))
    return [x for x in array if sorted(list(x.lower())) == sorted_string_list and x.lower() != string.lower()]
