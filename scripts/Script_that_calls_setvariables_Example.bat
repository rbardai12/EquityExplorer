@echo off

call setvariables.bat

set AnaplanUser=%AnaplanUser%
set WorkspaceId=%Workspace%
set ModelId=%Model%

set ServiceUrl="https://api.anaplan.com"
set AuthUrl="https://auth.anaplan.com"

set FileName=%File%
set FilePath=%FileDir%
set ImportName=%ImportAction%
set ErrorDumpName=%ErrorDumpFile%
set Chunksize=1

set Operation=-debug -process %ProcessName% -execute -output %DumpName%

rem *** End of settings - Do not edit below this line ***

setlocal enableextensions enabledelayedexpansion || exit /b 1
cd %~dp0
if not %AnaplanUser% == "" set Credentials=-user %AnaplanUser%
set Command=.\AnaplanClient.bat %Credentials% -service %ServiceUrl% -auth %AuthUrl% -workspace %WorkspaceId% -model %ModelId% %Operation%
@echo %Command%
cmd /c %Command%
pause