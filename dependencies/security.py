from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from typing import Optional

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class Security:
    def __init__(self):
        pass

    def get_user(self, token: str = Depends(oauth2_scheme)):
        # Perform authentication and return user details (e.g., user_id, roles)
        # Verify the token, check database, etc.
        # If authentication fails, raise an HTTPException with a 401 status code

        # Example: Dummy user details for demonstration purposes
        user_id = 1
        roles = ["user"]
        return {"user_id": user_id, "roles": roles}

    def is_user_authorized(self, user: dict = Depends(get_user)):
        # Placeholder for authorization logic
        # Check if the user has the necessary roles or permissions
        # If not authorized, raise an HTTPException with a 403 status code

        # Example: Dummy authorization logic for demonstration purposes
        if "admin" not in user["roles"]:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="User not authorized to perform this action",
            )
