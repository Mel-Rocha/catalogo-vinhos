import uuid

from tortoise import fields, Model


class Wine(Model):
    id = fields.UUIDField(pk=True, default=uuid.uuid4())
    nation = fields.CharField(max_length=50, null=True, blank=True)
    type = fields.CharField(max_length=50, null=True, blank=True)
    grape_variety = fields.CharField(max_length=100, null=True, blank=True)
    region = fields.CharField(max_length=100, null=True, blank=True)
    production = fields.CharField(max_length=100, null=True, blank=True)
    area = fields.CharField(max_length=100, null=True, blank=True)
    vintage = fields.CharField(max_length=10, null=True, blank=True)
    format = fields.CharField(max_length=10, null=True, blank=True)
    gradation = fields.CharField(max_length=10, null=True, blank=True)
    service = fields.CharField(max_length=100, null=True, blank=True)
    temperature = fields.CharField(max_length=10, null=True, blank=True)
    combination = fields.CharField(max_length=200, null=True, blank=True)
    dosage = fields.CharField(max_length=50, null=True, blank=True)
    method = fields.CharField(max_length=50, null=True, blank=True)
    producer = fields.CharField(max_length=100, null=True, blank=True)
    tasting_notes = fields.TextField(null=True, blank=True)