def import_data(filePath, fileType):
    #import data from a file and return in a python list type
    if fileType == 'json':
        with open(filePath) as f:
            data = json.load(f)
    else:
        data = []
        with open(filePath) as f:
            for line in f:
                data.append(line.strip().split())
    return data



