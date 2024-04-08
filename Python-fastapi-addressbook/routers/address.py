from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from backend.session import create_session
from typing import List
from schema.address import Address, ResponseAddress
from auth.auth_bearer import JWTBearer
from services.address import AddressService, AddressDataManager
from geopy.distance import geodesic
from math import radians, sin, cos, sqrt, atan2

router = APIRouter()


def validate_address(address: Address) -> None:
    """
    Validates latitude and longitude.
    """
    if not (-90 <= address.latitude <= 90) or not (
        -180 <= address.longitude <= 180
    ):
        raise HTTPException(
            status_code=400, detail="Invalid latitude or longitude values"
        )


def haversine_distance(lat1, lon1, lat2, lon2):
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = 6371 * c

    return distance


@router.post(
    "/addresses/",
    response_model=Address,
    dependencies=[Depends(JWTBearer())],
    tags=["Address"],
)
async def create_address(
    address: Address, session: Session = (Depends(create_session))
) -> Address:
    """IT Will create a records in database Table."""

    validate_address(address)
    add = AddressService(session).convert_data_into_obj(address)
    return add


@router.get(
    "/addresses/",
    response_model=List[ResponseAddress],
    dependencies=[Depends(JWTBearer())],
    tags=["Address"],
    status_code=status.HTTP_302_FOUND,
)
async def get_addresses_within_distance(
    latitude: float,
    longitude: float,
    distance: float,
    res: Response,
    session: Session = Depends(create_session),
) -> List[ResponseAddress]:
    """return address within the given distance."""

    addresses = []
    rows = AddressDataManager(session).get_addresses()
    for row in rows:
        row = row.__dict__
        del row["_sa_instance_state"]
        cal_distance = haversine_distance(
            row.get("latitude"), row.get("longitude"), latitude, longitude
        )
        print("Distance:", distance, "km")

        if cal_distance <= distance:
            addresses.append(
                {
                    "id": row.get("id"),
                    "name": row.get("name"),
                    "latitude": row.get("latitude"),
                    "longitude": row.get("longitude"),
                }
            )
    if addresses:
        return addresses
    else:
        res.status_code = status.HTTP_404_NOT_FOUND
        return addresses


@router.get(
    "/all_addresses/",
    response_model=List[ResponseAddress],
    dependencies=[Depends(JWTBearer())],
    tags=["Address"],
    status_code=status.HTTP_302_FOUND,
)
async def get_addresses_within_distance(
    res: Response,
    session: Session = Depends(create_session),
) -> List[ResponseAddress]:
    """return address within the given distance."""

    addresses = []
    rows = AddressDataManager(session).get_addresses()
    for row in rows:
        row = row.__dict__
        del row["_sa_instance_state"]
        addresses.append(
            {
                "id": row.get("id"),
                "name": row.get("name"),
                "latitude": row.get("latitude"),
                "longitude": row.get("longitude"),
            }
        )
    if addresses:
        return addresses
    else:
        res.status_code = status.HTTP_404_NOT_FOUND
        return addresses


@router.put(
    "/addresses/{address_id}/",
    response_model=dict,
    dependencies=[Depends(JWTBearer())],
    tags=["Address"],
    status_code=status.HTTP_200_OK,
)
async def update_address(
    address_id: int,
    address: Address,
    res: Response,
    session: Session = Depends(create_session),
) -> dict:
    """update the record based on the ID."""

    validate_address(address)
    add = None
    add = AddressService(session).convert_updated_data_into_obj(
        address, address_id
    )
    if "Success" in add:
        add.update({"values": address.__dict__})
        return add
    else:
        res.status_code = status.HTTP_400_BAD_REQUEST
        return add


@router.delete(
    "/addresses/{address_id}/",
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(JWTBearer())],
    tags=["Address"],
)
async def delete_address(
    address_id: int,
    res: Response,
    session: Session = Depends(create_session),
) -> dict:
    """Delete the record based on ID."""

    add = AddressDataManager(session).remove(address_id)
    if add:
        return {"message": "Address deleted successfully"}
    else:
        res.status_code = status.HTTP_404_NOT_FOUND
        return {"Message": "Invalid Address ID"}
