import os


def load(name):
    """
    Loads or creates a journal object
    :param name: The name of the journal object
    :return: The journal object as a List.
    """
    data = []
    filename = get_full_pathname(name)

    if os.path.exists(filename):
        with open(filename) as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())

    return data


def save(name, journal_data):
    filename = get_full_pathname(name)
    print('.... Saving to {}'.format(filename))

    #fout = open(filename, 'w')

    with open(filename, 'w') as fout:
        for entry in journal_data:
            fout.write(entry + '\n')

def get_full_pathname(name):
    filename = os.path.abspath(os.path.join('.', 'journals', name + '.jrl'))
    return filename

def add_entry(data, journal_data):
    journal_data.append(data)