trigger:


- master



pool:


  vmImage: 'ubuntu-latest'


strategy:


  matrix:


    Python27:


      python.version: '2.7'



steps:


- task: UsePythonVersion@0


  inputs:


    versionSpec: '$(python.version)'


  displayName: 'Use Python $(python.version)'


- script: python "build.py"



- task: PythonScript@0


  inputs:


    scriptSource: 'inline'


    script: |


      print('Hello world 1')


      print('KLU')