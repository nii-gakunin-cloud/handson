import sys
import os
import numpy as np

def main(result_dir):
    # debug
    print(f'SLURM_PROCID: {os.getenv("SLURM_PROCID")}')
    print(f'SLURM_NODEID: {os.getenv("SLURM_NODEID")}')
    print(f'SLURM_TASK_PID: {os.getenv("SLURM_TASK_PID")}')
    
    # ダミーデータの生成
    data = np.random.rand(100)
    
    pid = os.getenv("SLURM_PROCID")
    result_file = os.path.join(result_dir, f'result_{pid}.npy')
    np.save(result_file, data)

    print(f'Task {pid} results saved to {result_file}')

if __name__ == '__main__':
    result_dir = sys.argv[1]
    main(result_dir)

