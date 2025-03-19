from django.db import models

class Log(models.Model):
    serialno = models.IntegerField()
    version = models.IntegerField()
    account_id = models.CharField(max_length=50)
    instance_id = models.CharField(max_length=50)
    srcaddr = models.GenericIPAddressField()
    dstaddr = models.GenericIPAddressField()
    srcport = models.IntegerField()
    dstport = models.IntegerField()
    protocol = models.IntegerField()
    packets = models.IntegerField()
    bytes = models.BigIntegerField()
    starttime = models.BigIntegerField()
    endtime = models.BigIntegerField()
    action = models.CharField(max_length=10)
    log_status = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.srcaddr} -> {self.dstaddr} ({self.starttime} - {self.endtime})"
