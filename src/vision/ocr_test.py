from PIL import Image
import pytesseract
import os


def read_text_from_image(image_path):
    try:
        # Vérifier si l'image existe
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"L'image {image_path} est introuvable.")

        # Ouvrir l'image avec PIL
        image = Image.open(image_path)

        # Vous pouvez ajouter une conversion si nécessaire, par exemple:
        # image = image.convert('RGB')  # ou 'L' pour niveaux de gris

        # Utilisation de pytesseract pour extraire le texte
        pytesseract.pytesseract.tesseract_cmd = (
            r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        )
        text = pytesseract.image_to_string(image)
        print(text)
        return text
    except Exception as e:
        print(f"Erreur lors du traitement de l'image: {e}")
        return ""


if __name__ == "__main__":
    image_path = "D:\\Nv_FrigoSmart\\datasets\\A\\2e912dcd-4d97-494b-904f-c1c7a90c3a8f_jpg.rf.49d73c822758a63be25308b323346e4a.jpg"
    read_text_from_image(image_path)
