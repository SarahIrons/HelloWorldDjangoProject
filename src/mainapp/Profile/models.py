from django.db import models

TYPE_Prefix = (
    ('Mr.', 'Mr.'),
    ('Ms.', 'Ms.'),
    ('Mrs.', 'Mrs.'),
    ('Mx.', 'Mx.'),
)


class Profile(models.Model):
    prefix = models.CharField(max_length=10, choices=TYPE_Prefix)
    firstName = models.CharField(max_length=60, default="", blank=True, null=False)
    lastName = models.CharField(max_length=60, default="", blank=True, null=False)
    email = models.CharField(max_length=60, default="", blank=True, null=False)
    userName = models.CharField(max_length=60, default="", blank=True, null=False)

    objects = models.Manager()

    def __str__(self):
        return self.userName
