from service_layer.mycase_play_service import login_mycase

def main():
    p, context, page = login_mycase()

    # Aquí continúa tu scraping ya autenticado
    print("Título actual:", page.title())

    input("Pulsa ENTER para cerrar...")
    context.close()
    p.stop()

if __name__ == "__main__":
    main()
