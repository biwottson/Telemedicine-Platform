from django.contrib.auth.models import User

class Patient(User):
    date_of_birth = models.DateField(blank=True, null=True)
    medical_history = models.TextField(blank=True)

class Provider(User):
    specialization = models.CharField(max_length=255, blank=True)
    years_of_experience = models.IntegerField(blank=True, null=True)
