from fastapi import APIRouter, HTTPException, Request, status
from fastapi.responses import JSONResponse
import logging
from models import User
from service import UserService

logger = logging.getLogger(__name__)

router = APIRouter()

service_user = UserService()


class Controller:
    @router.get("/", response_class=JSONResponse)
    async def list_user():
        users = service_user.list_all()
        return JSONResponse(content=users)

    @router.post("/", status_code=status.HTTP_201_CREATED)
    async def create_user(request: Request):
        payload = await request.json()
        name = payload.get("name")
        password = payload.get("password")
        if not name or not password:
            raise HTTPException(
                status_code=400, detail="name and password required")
        user = User()
        user.name = name
        user.password = password
        try:
            new_id = service_user.create(user)
            return JSONResponse(content={"id": new_id, "name": name}, status_code=201)
        except Exception:
            logger.exception("api_create_user error")
            raise HTTPException(
                status_code=500, detail="failed to create user")

    @router.get("/{user_id}")
    async def get_user(user_id: int):
        user = service_user.get_by_id(user_id)
        logger.debug("api_get_user user=%s", user)
        if not user:
            raise HTTPException(status_code=404, detail="not found")
        return JSONResponse(
            content={"id": user.id, "name": user.name,
                     "password": user.password}
        )

    @router.put("/{user_id}")
    @router.patch("/{user_id}")
    async def update_user(user_id: int, request: Request):
        payload = await request.json()
        name = payload.get("name")
        password = payload.get("password")
        if not name and not password:
            raise HTTPException(
                status_code=400, detail="name or password required")
        user = User()
        user.name = name
        user.password = password
        try:
            updated = service_user.update_by_id(user_id, user)
            if updated:
                return JSONResponse(content={"updated": updated})
            raise HTTPException(
                status_code=404, detail="not found or not updated")
        except Exception:
            logger.exception("api_update_user error")
            raise HTTPException(
                status_code=500, detail="failed to update user")

    @router.delete("/{user_id}")
    async def delete_user(user_id: int):
        try:
            deleted = service_user.delete_by_id(user_id)
            if deleted:
                return JSONResponse(content={"deleted": deleted})
            raise HTTPException(status_code=404, detail="not found")
        except Exception:
            logger.exception("api_delete_user error")
            raise HTTPException(
                status_code=500, detail="failed to delete user")
