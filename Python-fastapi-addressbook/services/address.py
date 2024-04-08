from services.base import BaseDataManager, BaseService
from models.address import Address
from sqlalchemy import select, update, delete


class AddressService(BaseService):
    def convert_data_into_obj(self, input_data: dict):
        res = AddressDataManager(self.session).insertData(Address(input_data))
        return res

    def convert_updated_data_into_obj(self, input_data: dict, rec_id: int):
        input_data = input_data.__dict__
        res = AddressDataManager(self.session).update_address(
            input_data, rec_id
        )
        return res


class AddressDataManager(BaseDataManager):

    def insertData(self, data: Address) -> Address:
        return self.add_one(data)

    def update_address(self, input_data: dict, rec_id: int) -> Address | dict:
        #         {
        # "name": "Vijay nagar",
        # "latitude": 22.01,
        # "longitude": 75.33
        # }
        # stmt = (
        #     update(Address)
        #     .where(Address.id == rec_id)
        #     .values(
        #         name=input_data.get("name"),
        #         latitude=input_data.get("latitude"),
        #         longitude=input_data.get("longitude"),
        #     )
        # )
        # res = self.update_one(stmt)
        res = self.session.query(Address).filter(Address.id == rec_id).first()
        if res is None:
            return {"Error": "Invalid record id"}

        if (
            "latitude" in input_data
            or "name" in input_data
            or "longitude" in input_data
        ):
            if "name" in input_data:
                res.name = input_data.get("name")
            if "latitude" in input_data:
                res.latitude = input_data.get("latitude")
            if "longitude" in input_data:
                res.longitude = input_data.get("longitude")
            self.session.commit()
            return {"Success": "Record successfully updated"}
        else:
            return {"Error": "Invalid values."}

        return res

    def get_addresses(self):
        stmt = select(Address)
        return self.get_all(stmt)

    def remove(self, rec_id) -> bool:
        stmt = delete(Address).where(Address.id == rec_id)
        return self.delete(stmt)
