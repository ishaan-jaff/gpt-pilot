from peewee import *

from playhouse.postgres_ext import BinaryJSONField

from database.models.components.base_models import BaseModel
from database.models.app import App


class DevelopmentSteps(BaseModel):
    id = AutoField()  # This will serve as the primary key
    app = ForeignKeyField(App, on_delete='CASCADE')
    hash_id = CharField(null=False)
    messages = BinaryJSONField(null=True)
    llm_response = BinaryJSONField(null=False)
    previous_step = ForeignKeyField('self', null=True, column_name='previous_step')

    class Meta:
        db_table = 'development_steps'
        indexes = (
            (('app', 'hash_id'), True),
        )