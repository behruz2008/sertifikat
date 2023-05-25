import math
from django.db import models


sex = (("Erkak","Erkak"),
       ("Ayol","Ayol")
       )

 
class IELTS (models.Model):
    image = models.ImageField(upload_to='IELTS_rasm')
    candidate_id = models.IntegerField()
    date = models.DateField()
    family_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    sex = models.CharField(choices=sex,max_length=200)
    region_address = models.CharField(max_length=200)
    nationally = models.CharField(max_length=200)
    first_language = models.CharField(max_length=200)
    speaking = models.FloatField()
    writing = models.FloatField()
    reading = models.FloatField()
    listening = models.FloatField()
    admission = models.TextField()
    test_number = models.FloatField()
    candidate_number = models.FloatField()
    @property
    def overal(self):
        arifmethic_mean = (self.speaking + self.writing + self.reading + self.listening) / 4
        if arifmethic_mean != int(arifmethic_mean):
            floor_plus_half = int(arifmethic_mean) + 0.5
            if (arifmethic_mean) <= floor_plus_half:
                return floor_plus_half
            else:
                return math.ceil(arifmethic_mean)
        else:
            return arifmethic_mean
                     
    def cefr_level(self):
        if 4 <=(self.overal) <=5:
            return "B1"
        if 5.5 <= (self.overal) <=6.5:
            return "B2"
        if 7 <= (self.overal) <= 8:
            return "C1"
        if 8 <= (self.overal) <= 9: 
            return "C2"

    def __str__(self):
        return f"{self.candidate_id} | {self.first_name} |"  
    
    
    
    class Meta:
        verbose_name = 'IELTS'
        verbose_name_plural = 'IELTS'