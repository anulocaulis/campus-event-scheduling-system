#!/bin/bash
#SBATCH --job-name=scalability-challenge
#SBATCH --output=alderaan-hpc/scalability-challenge.out
#SBATCH --error=alderaan-hpc/scalability-challenge.err
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=16
#SBATCH --mem=64G
#SBATCH --time=02:00:00
#SBATCH --partition=math-alderaan

# move to root dir
cd /storage/biology/projects/miller-lowry/beitner/campus-event-scheduling-system/

# activate the conda environment with numpy, matplotlib
source /home/beitnerm/miniforge3/etc/profile.d/conda.sh
conda activate dsa_env
export PYTHONPATH=$(pwd):$PYTHONPATH

echo "Running scalability challenge on Alderaan HPC..."
# run the scalability challenge script and save results to a file
python3 src/scalability-challenge.py | tee alderaan-hpc/scalability-results.txt

echo "Scalability challenge completed at $(date). Results saved to alderaan-hpc/scalability-results.txt"