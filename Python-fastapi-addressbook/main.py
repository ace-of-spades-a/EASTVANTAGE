from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from geopy.distance import geodesic
import sqlite3
from routers.user import router as user_router

app = FastAPI()
app.include_router(user_router)

# def DbConfig():
#     """Return cursor object."""
#     # DB Configurations.
#     conn = sqlite3.connect("address_book.db")
#     c = conn.cursor()

#     # It will Create address table if not exists.
#     c.execute(
#         """CREATE TABLE IF NOT EXISTS addresses
#                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 name TEXT NOT NULL,
#                 latitude REAL NOT NULL,
#                 longitude REAL NOT NULL)"""
#     )
#     conn.commit()

#     return conn, c


# # Request and response schema.
# class Address(BaseModel):
#     name: str
#     latitude: float
#     longitude: float


# def validate_address(address: Address) -> None:
#     """
#     Validates latitude and longitude.
#     """
#     if not (-90 <= address.latitude <= 90) or not (
#         -180 <= address.longitude <= 180
#     ):
#         raise HTTPException(
#             status_code=400, detail="Invalid latitude or longitude values"
#         )


# app = FastAPI()
# conn, c = DbConfig()


# @app.post("/addresses/", response_model=Address)
# async def create_address(address: Address) -> Address:
#     """IT Will create a records in database Table."""

#     validate_address(address)
#     with conn:
#         c.execute(
#             "INSERT INTO addresses (name, latitude, longitude) VALUES (?, ?, ?)",
#             (address.name, address.latitude, address.longitude),
#         )
#         address_id = c.lastrowid
#     return {"id": address_id, **address.model_dump()}


# @app.put("/addresses/{address_id}/", response_model=Address)
# async def update_address(address_id: int, address: Address) -> Address:
#     """update the record based on the ID."""

#     validate_address(address)
#     with conn:
#         c.execute(
#             "UPDATE addresses SET name = ?, latitude = ?, longitude = ? WHERE id = ?",
#             (address.name, address.latitude, address.longitude, address_id),
#         )
#         if c.rowcount == 0:
#             raise HTTPException(status_code=404, detail="Address not found")
#     return {"id": address_id, **address.model_dump()}


# @app.delete("/addresses/{address_id}/")
# async def delete_address(address_id: int) -> dict:
#     """Delete the record based on ID."""

#     with conn:
#         c.execute("DELETE FROM addresses WHERE id = ?", (address_id,))
#         if c.rowcount == 0:
#             raise HTTPException(status_code=404, detail="Address not found")
#     return {"message": "Address deleted successfully"}


# @app.get("/addresses/", response_model=List[Address])
# async def get_addresses_within_distance(
#     latitude: float, longitude: float, distance: float
# ) -> List[Address]:
#     """return address within the given distance."""

#     addresses = []
#     with conn:
#         c.execute("SELECT id, name, latitude, longitude FROM addresses")
#         rows = c.fetchall()
#         for row in rows:
#             address_id, name, lat, lon = row
#             if geodesic((latitude, longitude), (lat, lon)).meters <= distance:
#                 addresses.append(
#                     {
#                         "id": address_id,
#                         "name": name,
#                         "latitude": lat,
#                         "longitude": lon,
#                     }
#                 )
#     return addresses
