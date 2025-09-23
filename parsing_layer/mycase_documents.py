import os
from pathlib import Path
from playwright.sync_api import Page
from config.settings import BASE_CASE_URL, DOWNLOAD_DIR

def download_case_pdfs(page: Page, case_id: int,  subfolder: str):
    """
    Visita la página de documentos de un caso en MyCase,
    encuentra todos los PDFs y los descarga en DOWNLOAD_DIR.
    """
    url = f"{BASE_CASE_URL}/{case_id}/documents#documents"
    print(f"➡️  Abriendo: {url}")
    page.goto(url)

    # Asegurar que la tabla de archivos esté cargada
    page.wait_for_selector("table.files-table", timeout=15000)

    # Crear carpeta de descarga: DOWNLOAD_DIR/subfolder
    target_dir = Path(DOWNLOAD_DIR) / subfolder
    target_dir.mkdir(parents=True, exist_ok=True)

    # Capturar los textos y selectores de descarga en una lista estática
    pdf_rows = page.query_selector_all("table.files-table tr:has(a.file-column-name-text)")
    print(f"📂 Se encontraron {len(pdf_rows)} archivos PDF.")

    # Capturar los enlaces de documento en una lista estática
    links = page.eval_on_selector_all(
        "a.file-column-name-text",
        "els => els.map(e => ({text: e.textContent.trim(), href: e.getAttribute('href')}))"
    )

    print(f"📂 Se encontraron {len(links)} archivos para descargar en '{subfolder}'.")

    for link in links:
        file_name = link["text"]
        doc_url = link["href"]

        if doc_url.startswith("/"):
            doc_url = f"https://the-mendoza-law-firm.mycase.com{doc_url}"

        print(f"⬇️  Abriendo documento: {file_name}")

        # Abrir el documento en una nueva pestaña
        doc_page = page.context.new_page()
        doc_page.goto(doc_url, wait_until="domcontentloaded")

        try:
            # Esperar el enlace de descarga con timeout de 10 segundos
            doc_page.wait_for_selector('a[href*="download"]', timeout=10000)

            # Esperar la descarga y guardarla
            with doc_page.expect_download() as download_info:
                doc_page.click('a[href*="download"]')
            download = download_info.value

            safe_path = target_dir / file_name
            download.save_as(str(safe_path))
            print(f"✅ Guardado en {safe_path}")
        except Exception:
            # Si no aparece el botón dentro de 10s, continuar con el siguiente
            print(f"⚠️  No se encontró botón de descarga para {file_name}. Se omite.")
        finally:
            doc_page.close()

    
