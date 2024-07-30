# main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models
import schemas
import crud
from database import  engine, get_db ,create_engine 

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/customers/", response_model=schemas.CustomerCreate)
def create_customer(customer: schemas.CustomerCreate, db: Session = Depends(get_db)):
    return crud.create_customer(db=db, customer=customer)

@app.post("/carriers/", response_model=schemas.CarrierCreate)
def create_carrier(carrier: schemas.CarrierCreate, db: Session = Depends(get_db)):
    return crud.create_carrier(db=db, carrier=carrier)

@app.post("/shipments/", response_model=schemas.ShipmentCreate)
def create_shipment(shipment: schemas.ShipmentCreate, db: Session = Depends(get_db)):
    return crud.create_shipment(db=db, shipment=shipment)

@app.post("/shipmentstatuses/", response_model=schemas.ShipmentStatusCreate)
def create_shipment_status(shipment_status: schemas.ShipmentStatusCreate, db: Session = Depends(get_db)):
    return crud.create_shipment_status(db=db, shipment_status=shipment_status)
