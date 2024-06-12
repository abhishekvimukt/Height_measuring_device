import subprocess

output = subprocess.check_output(['project'])
result = subprocess.check_output(['proj2','-1'], input=output)

print(result.decode())
