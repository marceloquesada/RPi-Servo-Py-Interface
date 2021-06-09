from setuptools import setup, find_packages
 
 
 
setup(name='rpy servo',
 
      version='0.1',
 
      url='https://github.com/marceloquesada/RPy-Servo',
 
      author='Marcelo Quesada',
 
      author_email='m.mergulhao@aluno.ufabc.edu.br',
 
      description='An easy way to manage servos in a RPi',
 
      classifiers=[
 
          'Development Status :: 1 - Alpha',
 
          'Programming Language :: Python :: 3.6',
 
          'Programming Language :: Python :: 3.7',
 
      ],
 
      packages=find_packages(include=['releases', 'releases.*']),
 
      long_description=open('README.md').read(),
      
      setup_requires=['pytest-runner'],
      
      tests_require=['pytest'],
 
      install_requires=['pigpio'])
