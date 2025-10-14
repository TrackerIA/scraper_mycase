import polars as pl

from utils.logger import get_logger
from service_layer.mycase_play_service import login_mycase
from parsing_layer.mycase_text_messages import select_text_message

logger = get_logger(__name__)


def main():
    # Ruta al CSV con columnas: ID, MESSAGE
    csv_path = "messages.csv"

    # Leer el CSV (usa latin1 si viene de Excel/Windows)
    df = pl.read_csv(
        csv_path,
        encoding="utf-8",
        ignore_errors=True
    )

    # Validar que tenga las columnas esperadas
    expected_cols = {"ID", "MESSAGE"}
    if not expected_cols.issubset(df.columns):
        logger.error(f"❌ El CSV debe contener las columnas: {expected_cols}. Se encontraron: {df.columns}")
        return

    # Abrir una sola sesión y loguear
    p, context, page = login_mycase()

    # Iterar sobre cada fila
    for row in df.iter_rows(named=True):  # named=True devuelve un dict
        raw_id = str(row["ID"]).strip().lstrip("/")
        case_id = int(raw_id) if raw_id.isdigit() else None
        message = str(row["MESSAGE"]).strip() if row["MESSAGE"] else "hola"

        if not case_id:
            logger.warning(f"⚠️  ID inválido: {raw_id}. Se omite.")
            continue

        logger.info(f"\n========== Enviando mensaje al caso {case_id} ==========")
        try:
            select_text_message(page, case_id, message)
        except Exception as e:
            logger.error(f"❌ Error al enviar mensaje a {case_id}: {e}")

    # Cerrar sesión de Playwright al final
    context.close()
    p.stop()
    logger.info("✅ Proceso completado correctamente.")


if __name__ == "__main__":
    main()
