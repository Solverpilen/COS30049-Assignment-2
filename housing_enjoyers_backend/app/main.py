from fastapi import FastAPI, HTTPException, Request, BackgroundTasks, Depends
from pydantic import BaseModel
from pickle import load

app = FastAPI()

filehandler = open("LinearRegModel.sav", "rb")
linearRegModel = load(filehandler)