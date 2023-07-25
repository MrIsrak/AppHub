import face_recognition
from PIL import Image, ImageDraw
import os

#Создание пути для открытия файла
def img_path(img_name):
    project_root = r"C:\Users\evgen\OneDrive\Рабочий стол\пайтон\AppHub\AppHub\face rec"
    image_path = os.path.join(project_root, "imgs", img_name)
    return image_path

#Распознование и обвод лиц
def face_rec():
    #Ввод имени файла
    img_name = input('img_name: ')

    #Загрузка изображения и получение координат
    photo = face_recognition.load_image_file(img_path(f'{img_name}.jpg'))
    photo_file_loc = face_recognition.face_locations(photo)

    #Отчет о количестве лиц
    print(f"I`ve found {len(photo_file_loc)} face(s)")
    
    # Добавляем "_new" перед расширением файла
    new_file_name = f"{img_name}_new.png"

    #Обведение лица
    photo_pil = Image.fromarray(photo)
    draw_m = ImageDraw.Draw(photo_pil)

    for (top, right, bottom, left) in photo_file_loc:
        draw_m.rectangle(((left, top), (right, bottom)), outline=(255, 0, 255), width=4)
    del draw_m

    #Сохранение в другю папку
    project_root = r"C:\Users\evgen\OneDrive\Рабочий стол\пайтон\AppHub\AppHub\face rec"

    new_file_path = os.path.join(project_root, "output", new_file_name)

    photo_pil.save(new_file_path)
 
    #Отчет о сохранении
    print(f"saved by {new_file_path} path")


def main():
    face_rec()

if __name__ == '__main__':
    main()
