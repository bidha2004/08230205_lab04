from django.db import models

# ---------- About Me Page Models ----------

class Profile(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)

    def __str__(self):
        return self.name


class Skill(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=10, blank=True)  # e.g., emoji or icon symbol

    def __str__(self):
        return f"{self.name} ({self.profile.name})"


# ---------- Learning Journey Page Models ----------

class LearningJourney(models.Model):
    quote = models.CharField(max_length=255)
    experience = models.TextField()
    challenges = models.TextField()

    def __str__(self):
        return "My Learning Journey"


class TimelinePhase(models.Model):
    journey = models.ForeignKey(LearningJourney, on_delete=models.CASCADE, related_name='phases')
    phase_title = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.phase_title
