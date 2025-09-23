from service_layer.mycase_play_service import login_mycase, download_pdfs_for_case

def main():
    case_id = 41243317  # Ejemplo
    download_pdfs_for_case(case_id, "Caso_41243317")

if __name__ == "__main__":
    main()
