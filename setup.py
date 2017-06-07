from setuptools import setup, find_packages

dependencies = []

long_description = """A Python application for calculating taxes in the Democratic Republic of Hughland.
"""

setup(name=u'drhtaxes',
      version='0.1.0',
      description='A Python application tax calcuation in DRH.',
      long_description=long_description,
      classifiers=[],
      author=u'Hugh Sorby',
      author_email='h.sorby@auckland.ac.nz',
      url='https://github.com/For-Researchers-ABI-2017/DRH-Taxes',
      license='Apache',
      packages=find_packages('source', exclude=['tests', 'tests.*', ]),
      package_dir={'': 'source'},
      entry_points = {
        'console_scripts': ['drhtaxes=drhtaxes.application:main']
      },
      zip_safe=True,
      install_requires=dependencies,
      )
