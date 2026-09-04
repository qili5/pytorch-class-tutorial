1. accessing HPC Class Partitions on Nova
https://research.it.iastate.edu/hpc-class#Accessing

2. Launching Interactive Jobs in Class Partitions 
https://research.it.iastate.edu/slurm#batch-vs-interactive

The following command will request 1 node for 60 minutes. (Terminal)

> salloc -p instruction -N 1 -t 60 -A f2026.coms.3710.01



For VS code
Interactive Apps, choose VS Code Tunnel
account: f2026.coms.3710.01
Slurm Partition: instruction
Submit
follow instructions from Nova OnDemand

All students in a class registered to use the cluster are given a file storage directory with the path /work/classtmp/<username>, where <username> is your ISU NetID. Do not use home directory, as it is tiny.
If you don't have your directory yet, then you need to create one first. To do so, open Terminal on VS code
> mkdir /work/classtmp/<username>
> cd /work/classtmp/<username>

You can copy demo code by the following command
> cp -r /work/classtmp/coms3710/pytorch-class-tutorial/* /work/classtmp/<username>

3. Set up Python virtual environments 
https://research.it.iastate.edu/python-virtual-environments 

This will create a virtual enviroment in direcotry "venv" in your current directory (if venv directory does not exit, the command will create one)
> python -m venv venv 

This will activate the venv
> source venv/bin/activate

This will upgrade the pip
>  python -m pip install --upgrade pip

This will install all required packages
> pip install -r requirements.txt --no-cache-dir

To deactivate, use the following command
> deactivate
