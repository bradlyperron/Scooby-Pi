@echo off
REM launch UAVcast-pro Webpages
SET BROWSER=chrome.exe
SET WAIT_TIME=2
start chrome -new-window http://172.29.136.112
start chrome -new-window http://172.29.119.8
start chrome -new-window http://172.29.30.168

exit 
