from fastapi import FastAPI
from app.routers import transactions, products, locations, employees, jobsimg

app = FastAPI()
app.include_router(transactions.router)
app.include_router(products.router)
app.include_router(locations.router)
app.include_router(employees.router)
app.include_router(jobsimg.router)