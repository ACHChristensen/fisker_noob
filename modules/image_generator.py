from tensorflow.keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img

datagenerator = ImageDataGenerator(channel_shift_range=20,
        rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest')

def image_mulitplier(image_path, image_name ,local_directory, qnty):
    i = 0
    print(image_path)
    image = load_img(image_path)
    array_image = img_to_array(image) #Numpy array with shape eg. (3, 150, 150)
    array_image = array_image.reshape((1,) + array_image.shape)  # this is a Numpy array with shape eg. (1, 3, 150, 150)
    for batch in datagenerator.flow(array_image, batch_size=1, save_to_dir= local_directory, save_prefix=image_name[12:-4], save_format='png'):
        i = i + 1
        if i >= qnty:
            break

if __name__ == '__main__':
    print("This is the image_generator module")