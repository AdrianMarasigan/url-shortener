from pydantic import BaseModel, HttpUrl, validator


class URLInput(BaseModel):
    url: HttpUrl
    short_url: str

    @validator("short_url")
    def validate_short_url(cls, value):
        # Hold for logic
        return value


class URLResponse(BaseModel):
    original_url: str
    short_url: str
