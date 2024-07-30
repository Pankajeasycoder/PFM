# crud.py
from sqlalchemy.orm import Session
import models
import schemas

def create_customer(db: Session, customer: schemas.CustomerCreate):
    db_customer = models.Customer(**customer.dict())
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

def create_carrier(db: Session, carrier: schemas.CarrierCreate):
    db_carrier = models.Carriers(**carrier.dict())
    db.add(db_carrier)
    db.commit()
    db.refresh(db_carrier)
    return db_carrier

def create_shipment(db: Session, shipment: schemas.ShipmentCreate):
    db_shipment = models.Shipments(**shipment.dict())
    db.add(db_shipment)
    db.commit()
    db.refresh(db_shipment)
    return db_shipment

def create_shipment_status(db: Session, shipment_status: schemas.ShipmentStatusCreate):
    db_shipment_status = models.ShipmentStatuses(**shipment_status.dict())
    db.add(db_shipment_status)
    db.commit()
    db.refresh(db_shipment_status)
    return db_shipment_status
