from setuptools import setup

long_description = '''\
Tools to monkeypatch - changing existing classes and modules in python.'''

setup(
    author="Chris Wilson",
    author_email="chrisw@aptivate.org",
    name='aptivate-monkeypatch',
    version='1.0',
    description='Monkeypatch tools',
    long_description=long_description,
    url='https://github.com/aptivate/aptivate-monkeypatch/',
    platforms=['OS Independent'],
    license='MIT License',
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ],
    include_package_data=True,
    zip_safe=False
)
