from setuptools import find_packages, setup
import glob, os

package_name = 'ros_venv_demo'
share_dir = os.path.join( "share", package_name )
data_files = []
data_files.append(( 'share/ament_index/resource_index/packages',  ['resource/' + package_name] ))
data_files.append(( os.path.join( share_dir, 'launch' ),          glob.glob( "launch/*.py" ) ))  
data_files.append(( share_dir, ['package.xml'] ))

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=data_files,
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='david',
    maintainer_email='david@somewebsite.co.uk',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'numpy_echo = ros_venv_demo.numpy_echo:main'
        ],
    },
)
