from django.utils import timezone
from django.db import models

class Pastor(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    image = models.ImageField(name="pastors/")
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return f"{self.name} added"

    class Meta:
        verbose_name = "Pastor"
        verbose_name_plural = "Pastor's"