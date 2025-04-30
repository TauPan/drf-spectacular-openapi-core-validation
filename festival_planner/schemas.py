import logging
import os

from drf_spectacular.openapi import AutoSchema as SpectacularAutoSchema

LOGLEVEL = os.environ.get('LOGLEVEL', 'WARNING').upper()

logging.basicConfig(level=LOGLEVEL)
log = logging.getLogger(__name__)


class AutoSchema(SpectacularAutoSchema):
    def _insert_field_validators(self, field, schema):
        for v in field.validators:
            if hasattr(v, 'get_schema'):
                log.debug(f'BEFORE: {schema}')
                # Remove every key in schema and then replace the
                # whole dictionary as an alias.
                for k in list(schema.keys()):
                    if k not in ['description']:
                        del schema[k]
                schema.update(v.get_schema())
                log.debug(f'AFTER: {schema}')
        super()._insert_field_validators(field, schema)
