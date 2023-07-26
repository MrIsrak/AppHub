import face_recognition
from PIL import Image, ImageDraw
import os
import numpy as np



def create_directory():
    project_root = os.path.dirname(os.path.abspath(__file__))
    dir_list = ["imgs", "output", "pcorpd"]
    for dir in dir_list:
        directory_path = os.path.join(project_root, dir)
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)
            print(f"Папка {directory_path} успешно создана.")
        else:
            print(f"Папка {directory_path} уже существует.")



#Создание пути для открытия файла
def img_path(img_name):
    project_root = os.path.dirname(os.path.abspath(__file__))
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
    project_root = os.path.dirname(os.path.abspath(__file__))

    new_file_path = os.path.join(project_root, "output", new_file_name)

    photo_pil.save(new_file_path)

    # image = Image.open(new_file_path)
    # image.show()
 
    #Отчет о сохранении
    print(f"saved by {new_file_path} path")

    return new_file_path, new_file_name

#Кроп лиц
def face_corp(new_file_path, new_file_name):
    #Открытие файла и нахождение лиц
    pil_img = Image.open(new_file_path)
    pil_img_np = np.array(pil_img)
    face_locations = face_recognition.face_locations(pil_img_np)

    project_root = os.path.dirname(os.path.abspath(__file__))

    
    #Перебор лиц в цикле
    for i, face_location in enumerate(face_locations):
        i = 1

        #Объявление крайних точек
        top, right, bottom, left = face_location

        #Проверка на принадлежность
        top = max(0, top)
        left = max(0, left)
        bottom = min(pil_img_np.shape[0], bottom)
        right = min(pil_img_np.shape[1], right)

        #Сохранение
        face_img = pil_img.crop((left, top, right, bottom))
        name, ext = new_file_name.split(".")
        new_face_file_name = f"{name}_corpd_{i}.png"  # Добавляем индекс для каждого лица
        new_face_file_path = os.path.join(project_root, "pcorpd", new_face_file_name)
        face_img.save(new_face_file_path)
    print(f"seved by '{new_face_file_path}'")
        


def main():
    create_directory()
    new_file_path, new_file_name = face_rec()
    face_corp(new_file_path, new_file_name)

if __name__ == '__main__':
    main()
