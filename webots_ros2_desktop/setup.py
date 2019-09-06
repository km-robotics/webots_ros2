"""webots_ros2 package setup file."""

import os
import sys
import tarfile
import urllib.request

from setuptools import setup

package_name = 'webots_ros2_desktop'
data_files = []
# If 'WEBOTS_HOME' not set try to download latest package (only on linux)
if 'WEBOTS_HOME' not in os.environ: # TODO: only on linux
    #TODO: remove previous artifact
    urllib.request.urlretrieve('https://github.com/omichel/webots/releases/download/R2019b/webots-R2019b-x86-64.tar.bz2',
                               os.path.join(os.path.dirname(__file__), 'webots-R2019b-x86-64.tar.bz2'))
    tar = tarfile.open('webots-R2019b-x86-64.tar.bz2', 'r:bz2')
    tar.extractall()
    tar.close()
    os.environ['WEBOTS_HOME'] = os.path.join(os.path.dirname(__file__), 'webots')
# Add Webots in the package
if 'WEBOTS_HOME' in os.environ:
    for root, directories, files in os.walk(os.environ['WEBOTS_HOME']):
        for f in files:
            source = os.path.relpath(os.path.join(root, f))
            target = root.replace(os.environ['WEBOTS_HOME'], 'share/' + package_name + '/webots')
            data_files.append((target, [source]))
else:
    sys.stderr.write('WARNING: "WEBOTS_HOME" environment variable not set, ' +
                     'this package might be incomplete.')
data_files.append(('share/ament_index/resource_index/packages', ['resource/' + package_name]))
data_files.append(('share/' + package_name, ['package.xml']))


setup(
    name=package_name,
    version='0.0.2',
    packages=[package_name],
    data_files=data_files,
    install_requires=['setuptools', 'launch'],
    zip_safe=True,
    author='Cyberbotics',
    author_email='support@cyberbotics.com',
    maintainer='Cyberbotics',
    maintainer_email='support@cyberbotics.com',
    keywords=['ROS', 'Webots', 'Robot', 'Simulation'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='Interface between Webots and ROS2 including the Webots package.',
    license='Apache License, Version 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': ['webots_path = webots_ros2_desktop.webots_path:get_webots_home']
    }
)
