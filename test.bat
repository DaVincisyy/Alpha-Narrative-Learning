@echo off
REM Windows批处理脚本 - 快速测试

if "%1"=="" (
    echo 使用方法:
    echo   test 1        测试第1章
    echo   test 2        测试第2章
    echo   test all      测试所有章节
    echo   test list     列出所有章节
    exit /b
)

python test_runner.py %*
