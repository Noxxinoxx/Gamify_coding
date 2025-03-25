import json;
import config;
def read_from_database():
    """
    This function is ment to read from my json database that is saved on the users computer.
    function returnes a json object.
    
    """
    
    database_url = config.paths.get("database_url");

    print(database_url)
    database = open(database_url)

    return json.load(database);

def update_value_in_database(key, value):
    """
    This function takes a key somehting in the database to update with a value that you also choose.
    function returns true if it worked.
    """
    
    database = read_from_database();

    database[0][key] = value;

    print(database)
    #write the modified data to the file.
    
    write_database(database);


def write_database(data):
    """
    This function will write data to database
    """

    database = config.paths.get("database_url")

    with open(database, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def tranfrom_into_string(data):
    """
    Function takes in some kind of data and transforms it into a string.
    """
    return str(data);


def transform_string_into_bytes(data):
    """
    Transform string data into bytes to be sent over socket connection.
    """
    return data.encode("utf-8");








