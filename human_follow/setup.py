from setuptools import setup

package_name = 'human_follow'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='khj',
    maintainer_email='khj@robotis.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'object_information_subscriber = human_follow.ObjectInformationSubscriber:main' # '노드이름 = 패키지명.파일명:실행할_함수'
        ],
    },
)
