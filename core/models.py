from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    name = models.CharField(max_length=100, unique = True)
    description = models.TextField()
    time_tracked = models.IntegerField() # in minutes
    estimated_time = models.IntegerField() # in minutes

    def __str__(self):
        return self.name


class Notification(models.Model):
    action = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.action + ' - ' + str(self.user.username) + ' - ' + str(self.project.name)


class Role(models.Model):
    role = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null = True)

    def __str__(self):
        return self.role + ' - ' + str(self.user.username) + ' - ' + str(self.project.name)


class Tasks(models.Model):
    task = models.CharField(max_length=100)
    descripton = models.TextField()
    time_tracked = models.IntegerField() # in minutes
    estimated_time = models.IntegerField() # in minutes
    project = models.ForeignKey(Project, on_delete=models.CASCADE, blank = True, null = True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.task + ' - ' + str(self.user.username) + ' - ' + str(self.project.name)

