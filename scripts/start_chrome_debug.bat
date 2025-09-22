@echo off
setlocal

rem === Ruta al ejecutable de Chrome (ajústala si es distinta) ===
set CHROME_EXE="C:\Program Files\Google\Chrome\Application\chrome.exe"

rem === Directorio de datos NO-por-defecto (puede ser cualquiera que no sea ...\User Data) ===
set USER_DATA_DIR=C:\ChromeDebug\MyCaseUserData

rem === Perfil dentro de ese user-data-dir. La 1a vez será "Default" ===
set PROFILE_DIR=Default

rem === Puerto de depuración ===
set DEBUG_PORT=9222

rem Crear carpeta si no existe
if not exist "%USER_DATA_DIR%" mkdir "%USER_DATA_DIR%"

rem Cerrar Chrome por si hay alguno colgado
taskkill /IM chrome.exe /F >nul 2>&1

rem Lanzar Chrome en modo depuración y abrir el dashboard
start "" %CHROME_EXE% ^
  --remote-debugging-port=%DEBUG_PORT% ^
  --user-data-dir="%USER_DATA_DIR%" ^
  --profile-directory="%PROFILE_DIR%" ^
  --disable-first-run-ui --no-first-run --no-default-browser-check ^
  https://the-mendoza-law-firm.mycase.com/dashboard

echo Chrome iniciado con depuracion en 127.0.0.1:%DEBUG_PORT%
