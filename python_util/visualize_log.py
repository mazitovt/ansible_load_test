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


fig, ax = plt.subplots(1, 1, figsize=(10,6)) 
fig.suptitle('Зависимость нагрузки процессора от количество клиентов (по времени)')

plt_lines = []
line_labels = []

for k, v in test_cases.items():
    xAxis = list(range(1,len(v)+1))
    yAxis = v
    plt_lines.append(ax.plot(xAxis, yAxis, label = k)[0])
    line_labels.append(k)
    
plt.ylabel('Использование ЦП, %')
plt.xlabel('Время с начала теста, сек')

fig.legend(plt_lines,             
           labels= line_labels,      
           loc="center right",        
           borderaxespad=0.1,        
           title="Legend Title")    

plt.subplots_adjust(right=0.85)

plt.savefig('./img/cpu_usage_to_time.png')
