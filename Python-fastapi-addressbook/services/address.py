from services.base import BaseDataManager, BaseService
from models.address import Address
from sqlalchemy import select, update, delete


class AddressService(BaseService):
    def convert_data_into_obj(self, input_data: dict):
        res = AddressDataManager(self.session).insertData(Address(input_data))
        return res

    def convert_updated_data_into_obj(self, input_data: dict, rec_id: int):
        res = AddressDataManager(self.session).insertData(Address(input_data))
        return res


class AddressDataManager(BaseDataManager):

    def insertData(self, data: Address) -> Address:
        return self.add_one(data)

    def update_address(self, input_data: dict, rec_id: int) -> Address:
        stmt = update(Address).where(Address.id == rec_id)
        return self.update_one(stmt)

    def get_addresses(self):
        stmt = select(Address)
        return self.get_all(stmt)

    def remove(self, rec_id) -> bool:
        stmt = delete(Address).where(Address.id == rec_id)
        return self.delete(stmt)
