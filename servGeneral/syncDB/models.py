from django.db import models


class SynchrodbConfig(models.Model):
    config_id = models.AutoField(primary_key=True)
    config_name = models.CharField(max_length=255)
    config_value = models.CharField(max_length=255)

    class Meta:
        managed = False