from parsing_layer.mycase_text_messages import select_text_message
from service_layer.mycase_play_service import login_mycase

if __name__ == "__main__":
    # Abrir una sola sesión y loguear
    p, context, page = login_mycase()
    select_text_message(page, 41243317, "Hola, este es un mensaje de prueba.")
    