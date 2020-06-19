from django.db import models
import random
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Tweet(models.Model):
    # Maps to SQL data
    # id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE) # many users can have many tweets , one tweet can just have one User its why we use ForeinKey itself
    #ForeingKey -> creating the relationships between these two tables
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='images/', blank=True, null=True)

    class Meta:
        ordering = ['-id']

    def serialize(self):
        return {
            "id": self.id,
            "content": self.content,
            "likes": random.randint(0, 200)
        }
