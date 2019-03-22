@echo off
REM Launch Mission Planner
cd "C:\Program Files (x86)\Mission Planner"
start MissionPlanner.exe

REM Launch TCP Video Streams
cd C:\gstreamer\1.0\x86\bin
start tcpVidStreamRpi1.cmd
start tcpVidStreamRpi2.cmd
start tcpVidStreamRpi3.cmd

exit