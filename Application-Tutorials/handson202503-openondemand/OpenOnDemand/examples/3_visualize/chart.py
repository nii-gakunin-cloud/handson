# ジョブ結果を可視化するスクリプト
# Jupyter Notebook のセルにコピーして実行する

import os
import numpy as np
import matplotlib.pyplot as plt

result_dir = '/home/ooduser/results'
result_files = [os.path.join(result_dir, f) for f in os.listdir(result_dir) if f.startswith('result_')]

data = [np.load(f) for f in result_files]

plt.figure(figsize=(10, 6))
for i, d in enumerate(data):
    plt.plot(d, label=f'Task {i}')
plt.xlabel('Index')
plt.ylabel('Value')
plt.title('Results from SLURM tasks')
plt.legend()
plt.show()

