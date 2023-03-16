from __future__ import annotations

import json
from typing import List, Optional
from pydantic import BaseModel
class Thumbnail(BaseModel):
    id: int
    key: str
    url: str
    size: int
    client: str
    filename: str
    mimetype: str
    container: str
    isWriteable: bool

class Author(BaseModel):
    guid: str
    firstName: str
    lastName: str
    status: str

class Upvoter(BaseModel):
    guid: str

class Company(BaseModel):
    guid: str
    name: str
    content: str
    thumbnail: Thumbnail
    status: str
    tags: List[str]
    authors: List[Author]
    upvoters: List[Upvoter]
    campaignName: str
    votes: int
    feedbacks: int
    rating: int
    createdAt: str
    url: str

class Model(BaseModel):
    success: Optional[bool] = None
    offset: Optional[int] = None
    size: Optional[int] = None
    total: Optional[int] = None
    result: Optional[List[Company]] = None

def main() -> None:
    """Main function."""

    # Read data from a JSON file
    with open("response.json") as file: # /workspaces/codespaces-project-template-py/Jsonparser/response.json
        data = json.load(file)
        companies: List[Company] = [Company(**item) for item in data]
        # print(data)
        print(companies[1])
        #print(books[0].dict(exclude={"price"}))
        # print(books[1].copy())

if __name__ == "__main__":
    main()