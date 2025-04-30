import datetime
from django.contrib import admin
from django.db import models
from django.utils.deconstruct import deconstructible
import jsonschema
import jsonschema.validators
import referencing
from rest_framework import serializers


ValidationError = jsonschema.ValidationError
sis_formats = jsonschema.FormatChecker()
ValidatorClass = jsonschema.Draft202012Validator
Validator = jsonschema.validators.extend(
    ValidatorClass,
    type_checker=ValidatorClass.TYPE_CHECKER.redefine(
        'timestamp', lambda checker, x: isinstance(x, datetime.datetime)))

def validate(instance, schema, retriever=None):
    registry = referencing.Registry(retrieve=retriever)
    validator = Validator(
        schema,
        format_checker=sis_formats,
        registry=registry)
    validator.validate(instance)


@deconstructible
class JSONSchemaValidator:
    """validates a JSONField according to a JSON schema"""

    def __init__(self, schema, retriever=None):
        self.schema = schema
        self.retriever = retriever

    def __call__(self, value):
        try:
            return validate(value, self.schema, self.retriever)
        except (jsonschema.SchemaError, ValidationError) as e:
            raise serializers.ValidationError(e)


# Create your models here.
class Mail(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    from_addr = models.EmailField()
    Subject = models.TextField(null=True)
    From = models.EmailField(null=True)
    To = models.JSONField(null=True, validators=[JSONSchemaValidator(
        {'type': 'array',
         'items': {
             'type': 'string',
             'format': 'email',
             'max_length': 254
         }}
    )])
    extra_headers = models.JSONField(null=True)
    mail_body = models.TextField(null=True)
    attachments = models.JSONField(null=True)


admin.site.register(Mail)
