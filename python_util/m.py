import matplotlib.pyplot as plt
import re



lines = []
with open("/home/tim/ansible_load_test/logs/log", "r") as f:
    lines = f.readlines()

test_cases = dict()
user_load = 0   
for line in lines:
    if line.startswith("-"):
        user_load = int(line.split()[2])
        test_cases[user_load] = []
        continue
    test_cases[user_load].append(float(re.findall(r'(\d+.\d+%)', line)[0][:-1]))


plt_lines = []
line_labels = []



x = []
y = []
for k,v in test_cases.items():
    x.append(str(k))
    y.append(sum(v)/len(v))

plt.bar(x,y, color=['red', 'blue', 'green'])
plt.savefig('./img/cpu_usage_bar.png')
