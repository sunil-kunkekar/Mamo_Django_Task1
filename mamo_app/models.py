from django.db import models


class Business_Contacts(models.Model):
    BC_ID = models.AutoField(primary_key=True)
    HS_ID = models.CharField(max_length=255)
    BC_FName = models.CharField(max_length=255)
    BC_LName = models.CharField(max_length=255)
    BC_Email = models.EmailField(max_length=255)
    BC_Company_Name = models.CharField(max_length=255)
    BC_Industry = models.CharField(max_length=255)
    BC_Active = models.BooleanField(default=True)
    BC_Job_Title = models.CharField(max_length=255)
    BC_Phone = models.CharField(max_length=20)
    BC_Post_Code = models.CharField(max_length=10)
    BC_Street_Address = models.CharField(max_length=255)
    BC_Created = models.DateTimeField(auto_now_add=True)
    BC_Last_Updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.BC_FName} {self.BC_LName} - {self.BC_Company_Name}"




class OLGA_matches(models.Model):
    OM_ID = models.AutoField(primary_key=True)
    PNM_ID = models.CharField(max_length=255)
    BC_ID = models.ForeignKey(Business_Contacts, on_delete=models.CASCADE)
    OLGA_MatchDate = models.DateTimeField()

    def __str__(self):
        return f"{self.OM_ID} - {self.PNM_ID} - {self.BC_ID} - {self.OLGA_MatchDate}"



class Premium_network_contacts(models.Model):
    PNM_ID = models.AutoField(primary_key=True)
    PNM_NumPicks = models.IntegerField(default=0)
    PNM_Active = models.BooleanField(default=True)

    def __str__(self):
        return f"PNM_ID: {self.PNM_ID}, Picks: {self.PNM_NumPicks}, Active: {self.PNM_Active}"
