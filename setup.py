from setuptools import setup, find_packages

setup(name='data-analysis',
      version='1.0',
      description='Python Twitter Data Analysis',
      author='Awadhesh Pathak',
      license='MIT',
      url='https://www.github.org/pathakaw/data-analysis',
      packages=find_packages(),
      install_requires=['PyQt5',
                        'pandas',
                        'sqlalchemy',
                        'nltk',
                        'numpy',
                        'jupyter',
                        'python-twitter',],
      entry_points={},
      extras_require={'dev': ['flake8,]},
     )
