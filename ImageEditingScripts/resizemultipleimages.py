import PIL,  os
from tqdm import tqdm
from PIL import Image





# I was making an app and needed to resize alot of images
# so I made this ....
# Ill add more functionality later on
# you will be able to resize multiple images with the same 
# extension to your required size 

#       DISCLAIMER  ###
       
# No copies are saved so be sure to save the original copy in case you 
#  change your mind

# peace :)

class ImageEditor:
    
    def resize(self, image, newsize = (64,64)):
        image_name = image
        image = Image.open(image)
        new_image =  image.resize(newsize)
        new_image.save(image_name)
        
        
    def resize_multiple(self, list_of_images, newsize = (64,64)):
        print(f"resizing   {len(list_of_images)}    images  to   {newsize} ")
        print(os.getcwd())
        for img in  tqdm(list_of_images):
            self.resize(img)
            
        print("Done !")
            
            
            
            
    def resize_all_in_folder(self, path_to_folder, file_type  = ".png" , newsize =(64,64)):
        # resize all images with the said extension in a particular folder
        # be careful with this
        os.chdir(path_to_folder)
       
        all_file = os.listdir()
        files_to_edit = [file  for file in all_file if file[-4:] == ".png"]
    
      
        
        
        self.resize_multiple(files_to_edit)
        
        
ImageEditor().resize_all_in_folder("./data/images/charachter/")