from django.db import models
from consumer.models.timestamped import Timestamped
from consumer.utils.enum import ModelEnum


class ConsumerStatusType(ModelEnum):
    collected = "collected"
    in_progress = "In_progress"
    active = "active"


class Consumer(Timestamped):
    street = models.CharField(max_length=255)
    status = models.CharField(max_length=16, choices=ConsumerStatusType.choices(), default=ConsumerStatusType.active)
    previous_jobs_count = models.PositiveBigIntegerField()
    amount_due = models.IntegerField(default=0)
    lat = models.FloatField(default=0.0)
    lng = models.FloatField(default=0.0)
