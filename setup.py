import setuptools

import kformat


with open('README.md') as fp:
    long_description = f'\n{fp.read()}'


setuptools.setup(
    name='K-Format',
    version=kformat.__version__,
    description='Python Library for dealing with KCB K-Format',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    python_requires='>=3.7',
    url='https://github.com/Rainist/K-Format',
    author='Sunghyun Hwang',
    author_email='me' '@' 'sunghyunzz.com',
    maintainer='Rainist',
    maintainer_email='engineering' '@' 'rainist.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
    ],
    packages=setuptools.find_packages(exclude=['tests*']),
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)
