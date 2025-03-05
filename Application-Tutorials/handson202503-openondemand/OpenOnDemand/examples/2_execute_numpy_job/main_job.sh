#!/bin/bash
#SBATCH -N 2
#SBATCH -n 2

RESULT_DIR=/home/ooduser/results
mkdir -p $RESULT_DIR

srun python3 ./my_script.py $RESULT_DIR

