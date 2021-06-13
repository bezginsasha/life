import sys
import time

for i in range(50):
	sys.stdout.write(f'\r{i}')
	sys.stdout.flush()
	time.sleep(0.2)
