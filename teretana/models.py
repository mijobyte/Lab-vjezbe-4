from django.db import models

# Create your models here.

class Oznaka(models.Model):
    naziv = models.CharField(max_length=200)

    def __str__(self):
        return self.naziv

class Plan(models.Model):
    naziv=models.CharField(max_length=150)
    cijena=models.IntegerField()
    max_clanova=models.IntegerField(null=True)
    oznake=models.ManyToManyField(Oznaka, default=None, blank=True, related_name='oznake')

    def __str__(self):
        return self.naziv

class Korisnik(models.Model):
    ime=models.CharField(max_length=150)

    def __str__(self):
        return self.ime

class Trener(models.Model):
    ime=models.CharField(max_length=150)

    def __str__(self):
        return self.ime

class Pretplatnik(models.Model):
    korisnik=models.ForeignKey(Korisnik, on_delete=models.CASCADE, null=True)
    trener=models.ForeignKey(Trener, on_delete=models.CASCADE, related_name='pretplatnici')
    kontakt=models.CharField(max_length=20)
    adresa=models.CharField(max_length=150)

    def __str__(self):
        return str(self.korisnik)

class Pretplata(models.Model):
    pretplatnik=models.ForeignKey(Pretplatnik, on_delete=models.CASCADE, null=True)
    plan=models.ForeignKey(Plan, on_delete=models.CASCADE, null=True)
    cijena=models.IntegerField()

