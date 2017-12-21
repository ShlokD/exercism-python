def transform(legacy_data):
    new_data = dict()
    for x in legacy_data:
        new_data.update(dict(zip(list(map(lambda x: x.lower(), legacy_data[x])), [x]*len(legacy_data[x]))))

    return new_data
