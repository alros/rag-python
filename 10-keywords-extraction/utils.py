dataset = '../datasets/bio-single-file/bio.txt'

def read_file(file = dataset):
    with open(file, 'r') as file:
        return file.read()
