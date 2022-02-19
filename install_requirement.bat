@echo off
TITLE Requirement Installer Script 
echo ================================================================================
echo                               Requirement Installer Script
echo[
echo                           You Need Python-3 To Run This Program 
echo ================================================================================
echo[
echo[
powershell -command pip install pygame==2.0.1
echo[
echo ================================================================================
echo                                 Pygame Installed !
echo ================================================================================
echo                                Press Any Key To Exit 
echo ================================================================================
pause > nul

::Requirements
::----------------

::pygame==2.0.1