from django.db import models

class Status(models.Model):
    status_id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.status}'


class ToDo(models.Model):
    choices = [
        ('High', 'High'), 
        ('medium',  'medium'),
        ('low', 'low'),
        ]
    todo_id = models.AutoField(primary_key=True)
    status_id = models.ForeignKey(Status, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    priority = models.CharField(max_length=255, choices=choices)
    details = models.TextField(blank=True)

    def __str__(self):
        return f'{self.name}'
