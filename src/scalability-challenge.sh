#!/bin/bash
#SBATCH --job-name=scalability-challenge
#SBATCH --output=alderaan-hpc/scalability-challenge.out
#SBATCH --error=alderaan-hpc/scalability-challenge.err
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=16
#SBATCH --mem=64G
#SBATCH --time=2-00:00:00
#SBATCH --partition=math-alderaan

## Logging and error handling setup
set -u

STAGE="job bootstrap"

log_stage() {
	STAGE="$1"
	echo "[$(date '+%Y-%m-%d %H:%M:%S')] STAGE: ${STAGE}"
}a

on_exit() {
	exit_code=$?
	if [ "$exit_code" -ne 0 ]; then
		echo "[$(date '+%Y-%m-%d %H:%M:%S')] FAILED at stage: ${STAGE} (exit code ${exit_code})"
	else
		echo "[$(date '+%Y-%m-%d %H:%M:%S')] COMPLETED successfully"
	fi
}

on_term() {
	echo "[$(date '+%Y-%m-%d %H:%M:%S')] RECEIVED SIGTERM at stage: ${STAGE}"
}

trap on_exit EXIT
trap on_term TERM

# move to root dir
log_stage "change directory"
cd /storage/biology/projects/miller-lowry/beitner/campus-event-scheduling-system/

# activate the conda environment with numpy, matplotlib
log_stage "activate conda environment"
source /home/beitnerm/miniforge3/etc/profile.d/conda.sh
conda activate dsa_env
export PYTHONPATH=$(pwd):$PYTHONPATH
export PYTHONUNBUFFERED=1

log_stage "run scalability workload"
echo "Running scalability challenge on Alderaan HPC..."
# run the scalability challenge script and save results to a file
python3 -u src/scalability-challenge.py 2>&1 | tee alderaan-hpc/scalability-results.txt

log_stage "finalize"
echo "Scalability challenge completed at $(date). Results saved to alderaan-hpc/scalability-results.txt"