@echo off
chcp 65001
title Discord Logger
:start
cls
type menu
py main.py
pause
goto start
