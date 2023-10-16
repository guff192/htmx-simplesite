from pprint import pprint
from random import randint

from tinydb import Query, TinyDB

from app.config import Settings


settings = Settings()


class CRUD:
    '''Base class for CRUD operations with TinyDB'''
    _db_instance: TinyDB | None = None
    
    @classmethod
    def _get_db_instance(cls) -> TinyDB:
        if not cls._db_instance:
            cls._db_instance = TinyDB(settings.DATA_DIR / 'data.json')

        return cls._db_instance

    def __init__(self, table_name: str):
        self._db = self._get_db_instance()
        self.table = self._db.table(table_name)

    @classmethod
    def with_table(cls, table_name: str) -> 'CRUD':
        '''Create a class instance with a specific table name'''
        return cls(table_name)

    def get_all(self):
        return self.table.all()

    def get_by_id(self, id: int):
        return self.table.get(doc_id=id)

    def get_random(self):
        return self.table.all()[randint(0, len(self.table) - 1)]

    def search_by_name(self, query: str):
        return self.table.search(Query()['name'].search(query))

    def create(self, data: dict) -> int:
        return self.table.insert(data)

    def create_many(self, data: list[dict]) -> list[int]:
        return self.table.insert_multiple(data)

    def update(self, id: int, fields: dict):
        self.table.update(fields=fields, doc_ids=[id])
    

if __name__ == '__main__':
    artist_details = CRUD.with_table('artist_info')
    all_artists = artist_details.search_by_name('Decemberists')
    pprint(all_artists)

