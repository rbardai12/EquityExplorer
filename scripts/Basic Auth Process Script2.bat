Set User=""
set WorkspaceId=""
set ModelId=""
set ServiceUrl="https://api.anaplan.com"
set AuthUrl="https://auth.anaplan.com"
set FileName="TSLA Income Statement.csv"
set FilePath=""
set ProcessName="Load Income Statement" 
set Chunksize=1


set Operation= -debug -service %ServiceUrl% -auth %AuthUrl% -file %FileName% -put %FilePath% -process %ProcessName% -execute -output
set Credentials=-user %User%
 

rem *** End of settings - Do not edit below this line ***

setlocal enableextensions enabledelayedexpansion || exit /b 1
cd %~dp0              
set Command=.\AnaplanClient.bat %Credentials% -workspace %WorkspaceId% -model %ModelId% %Operation%
@echo %Command%
cmd /c %Command%
pause