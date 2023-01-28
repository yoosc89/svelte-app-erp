from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from customer import customer_router
from customerdetail import customerdetail_router
from user import user_router
from noticefile import notice__router


app = FastAPI()

origins = [
    'http://localhost:8080', 'http://localhost:3000', 'http://localhost', 'http://127.0.0.1', 'http://192.168.0.4', 'https://192.168.0.4'

]

app.add_middleware(CORSMiddleware, allow_origins=origins,
                   allow_credentials=False, allow_methods=['*'], allow_headers=['*'])


app.include_router(customer_router.router)
app.include_router(customerdetail_router.router)
app.include_router(user_router.router)
app.include_router(notice__router.router)
