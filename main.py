import os

for i in range(0, 50):
  os.system('touch a.txt')
  os.system('git add .')
  os.system('git commit -m "Update"')
  os.system('git push')
  os.system('rm -rf a.txt')
  os.system('git add .')
  os.system('git commit -m "Update"')
  os.system('git push')
