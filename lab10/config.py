from configparser import ConfigParser


def config(filename='database.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)

    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for a in params:
            db[a[0]] = a[1]
    else:
        raise Exception("Error")
    return db
