from django.db import models


class Events(models.Model):
    title = models.CharField(max_length=120)
    event_start = models.DateTimeField()
    event_end = models.DateField()
    description = models.TextField()
    # created_by -> polaczyc rekord z uzytkownikiem
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title


class Comments(models.Model):
    content = models.TextField()
    # created_by -> link do uzytkownika
    event = models.ForeignKey(Events, on_delete=models.CASCADE, related_name='event_comments')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"Comment for {self.event.title}"
