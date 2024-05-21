# migKeyPoint

## Getting started
**Prerequisites**

0.0. If you don't already have [Anaconda](https://docs.anaconda.com/free/anaconda/install/) on your system, follow the instructions in the link to install it.

0.1. If you don't have git set up on your computer [follow these instructions for your system](https://www.atlassian.com/git/tutorials/install-git).

**Setting up the package**
1. Clone this repository. I've only ever used git in a command line interface, so open up a terminal and try

```bash
git clone git@github.com:<your_username>/migKeyPoint.git
```

For the above command to work, you have to add an ssh key [(instructions here)](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent?platform=linux) to your account which I would recommend doing (it makes editing git repos way easier). if this doesn't work try

```bash
git clone https://github.com/<your_username>/migKeyPoint.git
```

**Note: you need to replace <your_username> with your actual username (and no brackets)**

If neither of these work, you can download the zipped directory.

2. Navigate to the `migKeyPoint/` directory and use Anaconda to install the proper python environment (**this might take 10+ minutes, so feel free to grab a coffee while you wait**):
   
   ```sh
   conda env create -f environment.yml
   ```
   
3. Activate the Anaconda environment with
   
   ```sh
   conda activate test
   ```
   
4. This environment contains all packages you need except `PyTorch` and `Ultralyics`. Follow the instructions [here](https://pytorch.org/) to install pytorch (if you have an Nvidia graphics card on your system you can install one of the CUDA builds for GPU capabilities, otherwise click "CPU" as the Compute platform). Install ultralytics with `pip install ultralytics`
5. Download the zip file [here](https://drive.google.com/file/d/1khof-pr0RCnWILtT5D3njaNrtxZDrW-q/view?usp=sharing). This file contains all of the data you will need to run the tutorials. **Important: Do not unzip the file! I have an unzip script that will take care of moving the files properly**.
6. Move `zipped_files.zip` that you just downloaded to the `migKeyPoint/` directory you cloned. If you aren't familiar with using the command line, on a UNIX-based terminal (i.e. a Mac or linux machine) you can type
   
   ```bash
   mv ~/Downloads/zipped_files.zip /path/to/migKeyPoint
   ```

where `/path/to/` should be replaced with the directory path of migKeyPoint in your filesystem. In Windows Powershell the equivalent is

   ```powershell
   Move-Item -Path "$env:USERPROFILE\Downloads\zipped_files.zip" -Destination "C:\path\to\migKeyPoint"
   ```

7. In the `migKeyPoint` directory, run `python3 setup_environment.py`. This script will unzip the contents of `zipped_files.zip` and will move them to their appropriate directories.
8. Assuming all went well, you are now set up to run the tutorials! Navigate to the `tutorials` directory, open up a Jupyter notebook by typing `jupyter notebook` in your terminal, and you can start playing around!

# master_configuration.yaml instructions
### This is a global configuration file that controls several settings in the jupyter notebook tutorial scripts. You can edit the fields in your favorite text editor
The main variables that you will be editing as you go through these tutorials:

**noise**: Set this to True when you want to generate simulation with noise and train and/or evaluate YOLO models on simulation with noise. Otherwise set to False

**log_scale**: Set to True when you want to work with images on a logarithmic colorscale, otherwise set to False. I found that in the realistic simulation sample (with noise) that a linear colorscale performs better. That being said, if you start labeling real data with bounding boxes and key points, a logarithmic scale with Gaussian filtering is easiest to see, so there are tradeoffs to consider.

**numKeyPoints**: If you change this you must manually change this in each relevant `.yaml` file in the `configs/keypoint.yaml` folder. Unfortunately these aren't yet linked together but I'll hopefully change this in a future version.
