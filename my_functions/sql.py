import sqlite3

def connect_db(db_name: str):
    """_summary_
      Connect to an existent data base
      If not exist, it will create one.
    Args:
        db_name (str): A database name.

    Returns:
        _type_: _description_
    """ 

    conn = sqlite3.connect(db_name)

    return conn 