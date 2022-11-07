from setuptools import setup, find_packages

setup(
    name='Challenge_ReportMetric',
    version='1.1',
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    url='https://github.com/MuneebZ/Challenge_ReportMetric',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Internationalization",
        "Topic :: Software Development :: Localization",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
    ],
    author='Muneeb Zafar',
    author_email='muneeb-zafar@outlook.com',
    description='Suade Labs Python Challange Solution 2022'
)
