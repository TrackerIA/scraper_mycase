import subprocess
import re
from webdriver_manager.chrome import ChromeDriverManager

from typing import Optional

from utils.logger import get_logger

logger = get_logger(__name__)

def get_chrome_version() -> Optional[str]:
    """
    Obtiene la versión de Google Chrome instalada.
    Retorna solo el número mayor (major).
    """
    try:
        # Opción 1: Comando en Windows
        result = subprocess.run(
            r'reg query "HKEY_CURRENT_USER\Software\Google\Chrome\BLBeacon" /v version',
            capture_output=True, text=True, shell=True
        )
        match = re.search(r"(\d+)\.", result.stdout)
        return match.group(1) if match else None
    except Exception as e:
        logger.error(f"⚠️  No se pudo obtener la versión de Chrome. Error: {e}")
        return None

def get_chromedriver_version() -> Optional[str]:
    """
    Usa webdriver_manager para obtener la versión recomendada de ChromeDriver.
    Retorna solo el número mayor (major).
    """
    try:
        driver_path = ChromeDriverManager().install()
        result = subprocess.run([driver_path, '--version'], capture_output=True, text=True)
        # Output example: "ChromeDriver 114.0.5735.90 ..."
        match = re.search(r"ChromeDriver (\d+)\.", result.stdout)
        return match.group(1) if match else None
    except Exception as e:
        logger.error(f"⚠️  No se pudo obtener la versión de ChromeDriver. Error: {e}")
        return None

def validate_versions() -> bool:
    chrome_ver = get_chrome_version() 
    driver_ver = get_chromedriver_version()
    logger.info(f"🔎 Chrome instalado: {chrome_ver}, ChromeDriver: {driver_ver}")
    return chrome_ver == driver_ver
