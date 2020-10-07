import os
from pdf2image import convert_from_path

pdf_path = '/home/sourabh/PycharmProjects/geos/geos-pdfs'
new_images_folder_path = "/home/sourabh/PycharmProjects/geos/images/"

lst = os.listdir(pdf_path)

for pdf_p in lst:
    images = convert_from_path(os.path.join(pdf_path, pdf_p),
                                output_folder= new_images_folder_path,
                                fmt='jpg')

# renaming the image files
for i, filename in enumerate(os.listdir(new_images_folder_path)):
    os.rename(new_images_folder_path + "/"+ filename, new_images_folder_path + '/image_' +str(i+16) + ".jpg")
