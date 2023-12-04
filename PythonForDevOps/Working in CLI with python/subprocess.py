import subprocess

cp = subprocess.run(['ls, -l'],
                    capture_output=True, universal_newline=True, check=True)
show = cp.stdout

