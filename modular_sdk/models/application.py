from pynamodb.attributes import UnicodeAttribute, BooleanAttribute, \
    MapAttribute
from pynamodb.indexes import AllProjection

from modular_sdk.models.base_meta import BaseMeta, TABLES_PREFIX
from modular_sdk.models.pynamodb_extension.base_model import BaseGSI
from modular_sdk.models.pynamodb_extension.base_role_access_model import \
    BaseRoleAccessModel

APPLICATION_ID = 'aid'
CUSTOMER_ID = 'cid'
TYPE = 't'
DESCRIPTION = 'descr'
IS_DELETED = 'd'
DELETION_DATE = 'dd'
META = 'meta'
SECRET = 'sec'

MODULAR_APPLICATIONS_TABLE_NAME = 'Applications'


class CustomerIdTypeIndex(BaseGSI):
    class Meta(BaseMeta):
        index_name = f"{CUSTOMER_ID}-index"
        read_capacity_units = 1
        write_capacity_units = 1
        projection = AllProjection()

    customer_id = UnicodeAttribute(hash_key=True, attr_name=CUSTOMER_ID)
    # type = UnicodeAttribute(range_key=True, attr_name=TYPE)


class Application(BaseRoleAccessModel):
    class Meta(BaseMeta):
        table_name = f'{TABLES_PREFIX}{MODULAR_APPLICATIONS_TABLE_NAME}'

    application_id = UnicodeAttribute(hash_key=True, attr_name=APPLICATION_ID)
    customer_id = UnicodeAttribute(attr_name=CUSTOMER_ID)
    type = UnicodeAttribute(attr_name=TYPE)
    description = UnicodeAttribute(attr_name=DESCRIPTION)
    is_deleted = BooleanAttribute(attr_name=IS_DELETED)
    deletion_date = UnicodeAttribute(attr_name=DELETION_DATE, null=True)
    meta = MapAttribute(default=dict, attr_name=META)
    secret = UnicodeAttribute(null=True, attr_name=SECRET)

    customer_id_type_index = CustomerIdTypeIndex()
