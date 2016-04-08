from django.db import models


class Parent1(models.Model):
    title = models.CharField(max_length=100)


class Child1(models.Model):
    parent = models.ForeignKey(Parent1, related_name='children')


class Parent2(models.Model):
    title = models.CharField(max_length=100)


class Child2(models.Model):
    parent = models.ForeignKey(Parent2, related_name='+children')


class Parent3(models.Model):
    title = models.CharField(max_length=100)


class Child3(models.Model):
    parent = models.ForeignKey(Parent3)


class Parent4(models.Model):
    title = models.CharField(max_length=100)
    _orderaaaaa = models.IntegerField(default=0)