from django.db import models


class hannoi_lotto(models.Model):
    title = models.CharField(max_length=20)
    date = models.CharField(max_length=20)
    Four = models.CharField(max_length=20)
    Three = models.CharField(max_length=20)
    Two = models.CharField(max_length=20)

    def __str__(self):
        return self.title.date


class hannoi_special(models.Model):
    title = models.CharField(max_length=20)
    date = models.CharField(max_length=20)
    Four = models.CharField(max_length=20)
    Three = models.CharField(max_length=20)
    Two = models.CharField(max_length=20)

    def __str__(self):
        return self.title.date


class hannoi_vip(models.Model):
    title = models.CharField(max_length=20)
    date = models.CharField(max_length=20)
    Four = models.CharField(max_length=20)
    Three = models.CharField(max_length=20)
    Two = models.CharField(max_length=20)

    def __str__(self):
        return self.title.date
