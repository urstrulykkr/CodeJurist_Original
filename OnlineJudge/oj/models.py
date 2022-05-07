from django.db import models

class Problems(models.Model):
    DIFFICULTY_LEVEL = (
        ('Hard', 'Hard'),
        ('Medium', 'Medium'),
        ('Easy', 'Easy'),
    )
    statement = models.CharField(max_length=1000)
    name = models.CharField(max_length=1000)
    code = models.CharField(max_length=10000)
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_LEVEL)

    def __str__(self):
        return self.name
    
    class Meta:
      verbose_name = "Problems"


class Solutions(models.Model):
    problem = models.ForeignKey(Problems, on_delete=models.CASCADE)
    verdict = models.CharField(max_length=50)
    submission_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.verdict

    class Meta:
      verbose_name = "Solutions"


class TestCases(models.Model):
    problem = models.ForeignKey(Problems, on_delete=models.CASCADE)
    TC_input = models.CharField(max_length=5000)
    TC_output = models.CharField(max_length=5000)

    def __str__(self):
        return "%s %s" % (self.TC_input, self.TC_output)
    
    class Meta:
      verbose_name = "Test Case"


