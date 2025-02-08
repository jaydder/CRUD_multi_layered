import os
import uvicorn
from fastapi import FastAPI
from utils.custom_logger import configure_logging
from controller.user_controller import router as user_router


configure_logging()

app = FastAPI(title='CRUD Multi Layered - FastAPI')

app.include_router(user_router)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    uvicorn.run('app:app', host='0.0.0.0', port=port, reload=True)
