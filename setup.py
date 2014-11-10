import multiprocessing
from setuptools import setup, find_packages

setup(
    name='django-maintenance-in-progress',
    version='0.1-dev',
    description='Intercept possible 500 errors when site maintenance is in progress and display a friendly page.',
    long_description = open('README.rst', 'r').read() + open('AUTHORS.rst', 'r').read() + open('CHANGELOG.rst', 'r').read(),
    author='Hedley Roos',
    author_email='hedleyroos@gmail.com',
    license='BSD',
    url='http://github.com/praekelt/django-maintenance-in-progress',
    packages = find_packages(),
    install_requires = [
        'Django',
        'django-preferences'
    ],
    include_package_data=True,
    tests_require=[
        'django-setuptest>=0.1.4',
    ],
    test_suite="setuptest.setuptest.SetupTestSuite",
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        "Development Status :: 4 - Beta",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    zip_safe=False,
)
