import boto3
from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel, HttpUrl, validator
from typing import Optional
from dependencies.security import Security
from models.pydantic_models import URLInput, URLResponse
import secrets
import string

app = FastAPI()
security = Security()

# Initialize DynamoDB client
dynamodb = boto3.resource('dynamodb')
table_name = 'your_table_name'  # Dummy DynamoDB table name
table = dynamodb.Table(table_name)

# OAuth2 Password Bearer token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def generate_random_url(length=8):
    characters = string.ascii_letters + string.digits
    return ''.join(secrets.choice(characters) for _ in range(length))


@app.post("/shorten_url", response_model=URLResponse)
def shorten_url(url_data: URLInput, token: str = Depends(oauth2_scheme)):
    # Implement authentication and authorization logic here

    # Dummy authentication for demonstration purposes
    if token != "fake_token":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized access",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Check if the user provided a custom URL
    if url_data.short_url:
        # Use the provided custom URL
        shortened_url = url_data.short_url
    else:
        # Generate a random URL
        random_part = generate_random_url()
        shortened_url = f"https://example.com/{random_part}"

    # Store the URL in DynamoDB
    table.put_item(
        Item={
            'short_url': shortened_url,
            'original_url': url_data.url,
        }
    )

    return URLResponse(original_url=url_data.url, short_url=shortened_url)


@app.get("/list_urls")
def list_urls(token: str = Depends(oauth2_scheme)):
    # Implement authentication and authorization logic here

    # Dummy authentication for demonstration purposes
    if token != "fake_token":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized access",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Retrieve URLs from DynamoDB
    # Dummy DynamoDB query logic
    urls_db = table.scan()['Items']

    return urls_db


@app.get("/redirect/{short_url}")
def redirect(short_url: str, token: str = Depends(oauth2_scheme)):
    # Implement authentication and authorization logic

    # Dummy authentication for demonstration purposes
    if token != "fake_token":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized access",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Dummy DynamoDB query logic
    urls_db = table.scan()['Items']

    # Check if the short URL exists
    original_url = next((item['original_url']
                        for item in urls_db if item['short_url'] == short_url), None)

    if not original_url:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Shortened URL not found",
        )

    # Redirect to the original URL
    return {"original_url": original_url}
