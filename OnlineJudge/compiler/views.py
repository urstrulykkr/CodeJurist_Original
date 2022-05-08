from django.shortcuts import render
import sys
import subprocess
from datetime import datetime
from oj.models import *

def compile_using_python(request, var_id):
    tests=TestCases.objects.filter(problem_tc_fk__id=var_id)
    code=request.POST['code']
    for test in tests:
        input_expected=test.TC_input
        output_expected=test.TC_output
        try:
            code_file = open('myCode.py', 'w')
            file.write(code)
            file.close()
            output = subprocess.run([sys.executable, 'myCode.py'], capture_output=True, encoding='ascii', input=input_expected, timeout=1)
            actual = output.stdout
            if(output.returncode != 0):
                verdict = Solutions.COMPILATION_ERROR
            elif actual = output_expected:
                verdict = Solutions.SUCCESS
            elif subprocess.TimeoutExpired:
                verdict = Solutions.TIME_LIMIT_EXCEEDED
            else:
                verdict = Solutions.WRONG_OUTPUT
        except Exception as e:
            verdict = Solution.RUNTIME_ERROR
    sol = Solutions(
        problem = Problems.objects.get(pk=var_id),
        verdict = verdict,
        submission_timestamp = datetime.now
    )
    sol.save()
    return verdict

def compile_with_c(request, var_id):
    code = request.POST['code']
    try:
        file = open('myCode.cpp', 'w')
        file.write(code)
        file.close()
        subprocess.run('g++ myCode.cpp')
        output = subprocess.run('a.exe', capture_output=True, text=True)
        output = output.stdout
    except Exception as e:
        output = e
    return output

def compile_java(request, variable_id):
    pass    




