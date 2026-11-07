from setuptools import find_packages, setup

package_name = 'dcmotor_control'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='weijun',
    maintainer_email='weijun957@gmail.com',
    description='DC Motor Control with a motor driver and onboard GPIO Pins',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'run_motor = dcmotor_control.motor_control:main',
        ],
    },
)
