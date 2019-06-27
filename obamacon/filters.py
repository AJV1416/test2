from PIL import Image

def load_img(filename):
    img = Image.open(filename) 
    return img

def show_img(img_object):
    img_object.show() 

def save_img(img_object, save_name):
    img_object.save(save_name)

img_object = load_img("obama.jpg") 
load_img("obama.jpg")  
show_img(img_object) 
save_img(img_object, "flower.jpg") 
# def obamicon(img_object):
# orginial_pixels = img_object.getdata()


