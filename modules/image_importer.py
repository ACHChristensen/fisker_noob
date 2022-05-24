#from PIL import Image as im #Pillow library
#import glob
#from xml.dom import NotFoundErr

#def get_single_image(image_path):
#    for image in os.listdir(image_path):
#        if(image.endswith('.jpg')):
#            with im.open(image) as target_image:
#                return target_image.rotate(0).show()
#    raise NotFoundErr("No jpg pictures is found")

from mailbox import NotEmptyError
import requests
import bs4
import os

def loading_items(xml_file):
    r = requests.get(xml_file)
    if r.status_code == 200:
        soup = bs4.BeautifulSoup(r.content, 'xml')
        return soup.findAll('item')   
    #TODO - evt. exception her

def saving_image(directory,image,image_title):
    with open(directory+"/"+image_title+".png", 'wb') as f:
        f.write(image)

def loading_images(item, fish_directory):
    id = 0
    species = item.find('navn')
    if(len(os.listdir(fish_directory)) > 1):
        raise NotEmptyError('This folder is not empty')
    for image_url in item.findAll("billede"):
        r = requests.get(image_url.text)
        species_text = species.text
        spieces = species_text.replace("/","")
        if r.status_code == 200:
            with open(fish_directory+"/"+ spieces + str(id) + ".png", 'wb') as f:
                for image in r:
                    f.write(image)
            id = id + 1

def image_paths(path_folder_images):
    image_path = []
    for file in os.listdir(path_folder_images):
        if (file.endswith(".jpg") or file.endswith(".png")):
            print(file)
            image_path.append(path_folder_images + "/" + file)
    return image_path

if __name__ == '__main__':
    print("This is the image_handler module")