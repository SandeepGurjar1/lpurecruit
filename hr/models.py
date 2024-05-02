from django.db import models
from django.contrib.auth.models import User

# Model for HR users


class Hr(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)

# Model for job postings


class JobPost(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=100)
    # Corrected typo from 'compnayName' to 'companyName'
    companyName = models.CharField(max_length=100)
    salaryLow = models.IntegerField(default=0)
    salaryHigh = models.IntegerField(default=0)
    applyCount = models.IntegerField(default=0)
    lastDateToApply = models.DateField()

    def __str__(self):
        return str(self.title)


# Status choices for the CandidateApplications model
STATUS_CHOICE = (
    ('pending', 'pending'),  # Corrected typo from 'pandding' to 'pending'
    ('selected', 'selected'),
)

# Model for candidate applications


class CandidateApplications(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    # Changed from OneToOneField to ForeignKey
    job = models.ForeignKey(to=JobPost, on_delete=models.CASCADE)
    passingYear = models.IntegerField()
    yearOfExperience = models.IntegerField(default=0)
    resume = models.FileField(upload_to='resume')
    # Default value corrected
    status = models.CharField(choices=STATUS_CHOICE,
                              max_length=20, default='pending')

    # def __str__(self):
    #     return f"{self.user.username} {self.job.title}"

# Model for selecting candidates for a job


class SelectCandidateJob(models.Model):
    job = models.ForeignKey(to=JobPost, on_delete=models.CASCADE)
    candidate = models.OneToOneField(to=CandidateApplications, on_delete=models.CASCADE)
