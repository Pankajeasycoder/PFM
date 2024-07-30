# schemas.py
from pydantic import BaseModel, validator
from typing import Optional
from datetime import date

class CustomerCreate(BaseModel):
    name: str
    email: str
    phone: str
    address: str
    preferred_contact: str

    @validator('preferred_contact')
    def check_preferred_contact(cls, v):
        if v not in ('phone', 'email', 'sms'):
            raise ValueError('preferred_contact must be one of "phone", "email", or "sms"')
        return v

class CarrierCreate(BaseModel):
    name: str
    contact_number: str
    address: str
    website: Optional[str] = None

class ShipmentCreate(BaseModel):
    customer_id: int
    carrier_id: int
    tracking_number: str
    origin_address: str
    destination_address: str
    shipment_date: date
    expected_date: date
    approval_to_sms: bool = False
    presign_leave_door: bool = False
    delivery_instructions: Optional[str] = None
    insurance_amount: float = 0.00
    fragile: bool = False
    perishable: bool = False
    weight: float
    dimensions: str
    hazardous_material: bool = False
    special_handling: Optional[str] = None

class ShipmentStatusCreate(BaseModel):
    shipment_id: int
    status: str
    location: str
    description: Optional[str] = None
