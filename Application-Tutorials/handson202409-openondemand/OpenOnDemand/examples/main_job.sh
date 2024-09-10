#!/bin/bash
#SBATCH -N 2
#SBATCH -n 4

RESULT_DIR=/home/ooduser/results
mkdir -p $RESULT_DIR

srun python3 /home/ooduser/my_script.py $RESULT_DIR

