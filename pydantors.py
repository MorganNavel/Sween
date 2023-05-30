# pip install pydantic
from typing import Optional
from pydantic import BaseModel, Field

class Blog(BaseModel):
    title: str 
    is_active: bool

Blog(title="My First Blog",is_active=True)
# Blog(title="My First Blog",is_active="yup!")

from pydantic import BaseModel

class Blog(BaseModel):
    title: str 
    description: Optional[str]=None
    is_active: bool

blog=Blog(title="My First Blog",is_active=True)
print(blog.title)
print(blog.description)
print(blog.is_active)

####################################################
from enum import Enum

class Languages(str,Enum):
    PY = "Python"
    JAVA = "Java"
    GO = "Go"

class Blog(BaseModel):
    title: str 
    language : Languages = Languages.PY
    is_active: bool
    


Blog(title="My First Blog",language="Java",is_active=True)
# Output: Blog(title='My First Blog', language=<Languages.JAVA: 'Java'>, is_active=True)

# Blog(title="My First Blog",language="C++",is_active=True)
# Output: ValidationError: 1 validation error for Blog language value is not a valid enumeration member; permitted: 'Python', 'Java', 'Go' 


import time
from datetime import datetime

class Blog(BaseModel):
    title: str 
    created_at: datetime = Field(default_factory=datetime.now)
    is_active: bool

print(Blog(title="Our First Blog",is_active=True))
time.sleep(5)
print(Blog(title="Our Second Blog",is_active=True))

#Output:
#title='Our First Blog' created_at=datetime.datetime(2022, 10, 7, 15, 52, 53, 748289) is_active=True
#title='Our Second Blog' created_at=datetime.datetime(2022, 10, 7, 15, 52, 53, 748289) is_active=True


from typing import List

class Comment(BaseModel):
    text: Optional[str]=None

class Blog(BaseModel):
    title: str 
    comment: Optional[List[Comment]]
    is_active: bool

print(Blog(title="Our First Blog",comment=[{'text':'My comment'},{'text':'Your comment'},],is_active=True))

#Output: title='Our First Blog' comment=[Comment(text='My comment'), Comment(text='Your comment')] is_active=True