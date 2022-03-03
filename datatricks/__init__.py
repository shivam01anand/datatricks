__version__ = '0.1.0'

import datetime
import mimetypes
import pandas as pd
from typing import AnyStr, Callable, Union
from PIL import Image
import json

def vertica_sql(conn_dict: dict,sql: str)-> list[list]: 
    
    """
    Fn to SQL Query any Vertica DB.

    DB rows are returned as list of lists.  
    """

    with vertica_python.connect(conn_dict) as conn:
        cur = conn.cursor()
        cur.execute(sql)
        return cur.fetchall()

def t(**arg: int) -> Union[pd.Timestamp,datetime.datetime]:

    """
    Add func to any date & transform its params 

    For ex,
    
    t1 = 10 Mar 22

    t1 + t(days=1) -> 11 Mar 22 #increment

    t1 + t(day=1) -> 2nd Jan 22 #assign

    t1 + t(days=1,month=10,year....)

    """
    
    return pd.DateOffset(**arg)

def print_func(n: int = 0) -> str:
    
    ''' 
    prints fn name under which it ran
    
    for current func name, specify 0 or no argument.
    for name of caller of current func, specify 1.
    for name of caller of caller of current func, specify 2. etc.
    '''
    
    print(f"{sys._getframe(n + 1).f_code.co_name} OK")
    return sys._getframe(n + 1).f_code.co_name

def image_to_b64(file: str) -> str: 
    """
    Opens img -> base64 encode -> decode (return decoded) 
    """
    with open(file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    return encoded_string.decode()

def file_type(f: str):
    
    """
    returns file type for a file(path).
    Uses guess_type instead of less reliable magic.

    For ex,

    file_type("you_got_rick_rolled.mp4")
    
    'video/mp4'
    
    """

    return mimetypes.guess_type(f)[0]

def img_dim(img):    

    """
    returns (width, height) of image file
    """

    im = Image.open(f'{img}')
    return im.size

def pp(json_obj):

    """
    return indented json string.
    alternative to needing pprint library
    """
    print(json.dumps(json_obj, indent=4))
