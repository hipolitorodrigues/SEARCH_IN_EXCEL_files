@echo off
cd /d "%~dp0"
if not exist "env01\Scripts\python.exe" (
    echo.
    echo ======================================================================
    echo ERRO: O ambiente virtual 'env01' nao foi encontrado nesta pasta!
    echo Certifique-se de executar este script na pasta raiz onde o env01 existe.
    echo ======================================================================
    echo.
    pause
    exit /b 1
)

start "" "env01\Scripts\pythonw.exe" main.py
