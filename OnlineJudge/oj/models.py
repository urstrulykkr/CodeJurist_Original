from django.db import models
from django.db.models import Model

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
      verbose_name = "Problem"


class Solutions(models.Model):
    FINAL_VERDICT = (
        ('SUCCESS', 'SUCCESS'),
        ('COMPILATION_ERROR', 'COMPILATION ERROR'),
        ('WRONG_OUTPUT', 'WRONG OUTPUT'),
        ('TIME_LIMIT_EXCEEDED', 'TIME LIMIT EXCEEDED'),
        ('RUNTIME_ERROR', 'RUNTIME ERROR')
    )
    problem = models.ForeignKey(Problems, on_delete=models.CASCADE)
    verdict = models.CharField(max_length=50, choices=FINAL_VERDICT)
    submission_timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.problem.id + "_" + self.verdict

    class Meta:
      verbose_name = "Solution"


class TestCases(models.Model):
    problem_tc_fk = models.ForeignKey(Problems, on_delete=models.CASCADE)
    TC_input = models.CharField(max_length=5000)
    TC_output = models.CharField(max_length=5000)

    def __str__(self):
        return "%s %s" % (self.TC_input, self.TC_output)
    
    class Meta:
      verbose_name = "Test Case"


class UserAdmission(models.Model):
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_id = models.EmailField()
    password = models.CharField(max_length=25)
    date = models.DateField()

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
      verbose_name = "User Admission"



