from setuptools import setup, find_packages
setup(
    name = "sc_analysis",
    version = "0.1",
    packages = find_packages(),
    install_requires = [
        'scanpy',
        'numpy',
        'panadas',
        'matplotlib',
        'flask',
        'argparse'
    ],
    entry_points = {
        'console_scripts' : [
            'sc_analysis=sc_analysis.main:main'
        ]
    }
)