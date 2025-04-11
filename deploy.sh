#!/bin/bash

# 현재 날짜와 시간 가져오기
now=$(date "+%Y-%m-%d %H:%M:%S")
# # Git 명령어 실행
 git add .
 git commit -m "Auto commit on $now"
 git push
#
