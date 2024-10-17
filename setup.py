from setuptools import setup, find_packages

setup(
    name='diyblog',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    license='BSD License',  # Example license
    description='A Django app to manage blogs with posts, categories, tags, and comments.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/djangodiy_blogapp',
    author='Pardeep Singh',
    author_email='ipardeepsingh13@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 5.0.1',  # Replace with your version
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.10',  # Replace with your Python version
        'Programming Language :: Python :: 3.11',
    ],
    install_requires=[
        'Django>=5.0.1',  # Make sure to specify the minimum Django version
    ],
)