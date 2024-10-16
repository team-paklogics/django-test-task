from django.db import models

class Slot(models.Model):
    day = models.CharField(max_length=9, choices=[
        ('monday', 'Monday'), ('tuesday', 'Tuesday'), ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'), ('friday', 'Friday'), ('saturday', 'Saturday'),
        ('sunday', 'Sunday')
    ])
    start = models.TimeField()
    stop = models.TimeField()
    ids = models.JSONField()  # Storing list of IDs as a JSON field

    def __str__(self):
        return f"{self.day} {self.start}-{self.stop} IDs: {self.ids}"
