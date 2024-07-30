# models.py
from sqlalchemy import Column, Integer, String, Text, Date, Boolean, DECIMAL, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Customer(Base):
    __tablename__ = "Customer"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    phone = Column(String(20), nullable=False)
    address = Column(Text, nullable=False)
    preferred_contact = Column(String(20), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default="CURRENT_TIMESTAMP")
    updated_at = Column(TIMESTAMP, nullable=False, server_default="CURRENT_TIMESTAMP")

class Carriers(Base):
    __tablename__ = "Carriers"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), nullable=False, unique=True)
    contact_number = Column(String(20), nullable=False)
    address = Column(Text, nullable=False)
    website = Column(String(255))
    created_at = Column(TIMESTAMP, nullable=False, server_default="CURRENT_TIMESTAMP")
    updated_at = Column(TIMESTAMP, nullable=False, server_default="CURRENT_TIMESTAMP")

class Shipments(Base):
    __tablename__ = "Shipments"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey("Customer.id"))
    carrier_id = Column(Integer, ForeignKey("Carriers.id"))
    tracking_number = Column(String(255), nullable=False, unique=True)
    origin_address = Column(String(255), nullable=False)
    destination_address = Column(String(255), nullable=False)
    shipment_date = Column(Date, nullable=False)
    expected_date = Column(Date, nullable=False)
    approval_to_sms = Column(Boolean, nullable=False, default=False)
    presign_leave_door = Column(Boolean, nullable=False, default=False)
    delivery_instructions = Column(Text)
    insurance_amount = Column(DECIMAL(10, 2), nullable=False, default=0.00)
    fragile = Column(Boolean, nullable=False, default=False)
    perishable = Column(Boolean, nullable=False, default=False)
    weight = Column(DECIMAL(10, 2), nullable=False)
    dimensions = Column(String(50), nullable=False)  # Format: LxWxH
    hazardous_material = Column(Boolean, nullable=False, default=False)
    special_handling = Column(Text)
    created_at = Column(TIMESTAMP, nullable=False, server_default="CURRENT_TIMESTAMP")
    updated_at = Column(TIMESTAMP, nullable=False, server_default="CURRENT_TIMESTAMP")

class ShipmentStatuses(Base):
    __tablename__ = "ShipmentStatuses"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    shipment_id = Column(Integer, ForeignKey("Shipments.id"))
    status = Column(String(255), nullable=False)
    location = Column(String(255), nullable=False)
    timestamp = Column(TIMESTAMP, nullable=False, server_default="CURRENT_TIMESTAMP")
    description = Column(Text)
