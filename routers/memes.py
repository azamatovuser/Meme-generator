from fastapi import APIRouter

router = APIRouter()

@router.get("/get_memes")
async def get_memes():
    return {"message": "Hello world"}

