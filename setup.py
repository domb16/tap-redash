from setuptools import setup

setup(name='tap-redash',
      version='0.0.1',
      description='Singer.io tap for extracting data from the Redash API',
      author='domb16',
      url='http://singer.io',
      classifiers=['Programming Language :: Python :: 3 :: Only'],
      py_modules=['tap_redash'],
      install_requires=[
          'singer-python>=2.1.4',
          'requests>=2.13.0',
          'pylint'

      ],
      entry_points='''
          [console_scripts]
          tap-redash=tap_redash:main
      ''',
      packages=['tap_redash'],
      package_data={
          'tap_redash/': ['tap_redash/*.json']
      },
      include_package_data=True
      )