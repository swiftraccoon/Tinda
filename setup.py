from setuptools import setup

setup(name='Tinda',
      version='2019.2',
      description='Tinder API for Python',
      long_description=open('README.md').read().strip(),
      author='Swift Raccoon',
      # author_email='',
      url='https://github.com/swiftraccoon/Tinda',
      py_modules=['tinder_api'],
      install_requires=['requests',
                        'robobrowser',
                        'lxml',
                        'web.py'],
      license='MIT License',
      zip_safe=False,
      keywords=['tinder-api', 'tinder', 'python-3', 'robobrowser'],
      # classifiers=[]
     )
