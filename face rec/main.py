import face_recognition
from PIL import Image, ImageDraw


def face_rec():
    mendale = face_recognition.load_image_file(r"C:\Users\evgen\OneDrive\Рабочий стол\пайтон\AppHub\AppHub\face rec\imgs\Mendale.jpg")
    mendale_file_loc = face_recognition.face_locations(mendale)

    print(mendale_file_loc)

    men_pil = Image.fromarray(mendale)
    draw_m = ImageDraw.Draw(men_pil)

    for(top, right, bottom, left) in mendale_file_loc:
        draw_m.rectangle(((left, top), (right, bottom)), outline=(255, 0, 255), width=4)
    del draw_m

    men_pil.save(r"C:\Users\evgen\OneDrive\Рабочий стол\пайтон\AppHub\AppHub\face rec\imgs\Mendale_new.png")

def main():
    face_rec()

if __name__ == '__main__':
    main()
