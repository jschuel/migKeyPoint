import os
import migKeyPoint.utils.YAMLtools as yt

'''Get configuration'''
conf = yt.load_configuration('master_configuration.yaml')['yoloConf']

'''Get absolute path of project directory'''
project_path = conf['project_dir']

subdirs = ['configs','data','datasets','models','pretrained']

print('Setting up project %s'%(os.path.split(project_path)[1]))
for dir in subdirs:
    path = project_path+'/'+dir
    if not os.path.exists(path):
        print('Created directory %s'%(path))
        os.makedirs(path)

print('DONE!')

