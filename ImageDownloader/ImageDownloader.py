
import requests,os, random, string, time
from tqdm import tqdm





# Author : Leting Victor Kipkemboi
# github : https://github.com/victhepythonista/

# a simple script to download images using the requests library
# it wil automatically save  images on  'Desktop/Image downloads'
# yes...its a windows script but you can  just tweek the directories and it should
# work on Ubuntu , Kali, MacOs etc

# enjoy ..

class ImageDownloader():
    
    def __init__(self):
        self.user = os.getlogin()
        dest = f"C:/Users/{self.user}/Desktop/Image downloads/"
        self.check_dir(dest)
        self.destination_dir = dest
        self.list_of_urls= []
        self.running = True
        
    
    def check_dir(self, directory):
        # create the directory if it does
        # not exist
        if  os.path.isdir(directory) == False:
            try:
                os.makedirs(directory)
            except:
                print('\nfailed to create !!')
                
    def get_name_from_url(self, url):
        # obtain a name for thwe image
        url = url.replace('/', '-')
        new_name = ''
        for char in url:
            if char in string.ascii_lowercase:
                new_name = new_name+char
        
        return new_name[5:20]

    
    def download_with_url(self, url, directory = '',extension =  '.jpg'):
        # download a single image  
        if directory == '':
            directory = self.destination_dir
        response = None
        try:
            response = requests.get(url, stream = True)
            package_size = int(response.headers.get('content-length',0))
            print('package size   ', package_size)
       
            if response.status_code == 200:
               # giving a random name to th eimages
            
                fname = self.get_name_from_url(url) + extension
                    
                os.chdir(self.destination_dir)
                with open(fname, 'wb') as f,tqdm(desc = fname,total = package_size,unit = 'iB', unit_scale = True,unit_divisor = 1024 ) as progress:
                        
                    for data in response.iter_content(chunk_size = 1024):
                        size = f.write(data)
                        progress.update(size)
                        time.sleep(.01)
                                        
                    print('downloaded ')
                
        except:
            print('invalid URL\n\nor maybe its your network \n : (')
        """
        unit size  is Kbyte

        """
       
            
            
                  
         
    def download_multiple_urls(self, list_of_urls):
        # download a list of urls
        print('total downloads  =  ', len(list_of_urls))
        for url in list_of_urls:
            self.download_with_url(url)

        
            
            
        
               
                
                
    def run_interface(self):
        print("""
    
    
    1   .   Download  a single image
    2   .   Download multiple images
    3   .   exit
    4   .   help info
    
    """)
        while self.running :
            choice = input(" _> ")
            if choice == '1':
               
               
                print('enter image url \n')
                url  = input("_> ")
                self.download_with_url(url)
                
            elif choice == '2':
                print('enter the urls and enter  OK to start download\n')
                multi_mode = True
                while multi_mode:
                    
                    inp = input('url >')
                    if inp == 'OK' :
                        
                        self.download_multiple_urls(self.list_of_urls)
                        
                        multi_mode = False
                        print('preparing to dowload ', self.list_of_urls )
                        
                    elif isinstance(inp, str):
                        self.list_of_urls.append(inp)
                    else:
                        continue
                    
            elif choice == "3":
                self.running = False
            elif choice == "4":
                help_info = f"""
     An image downloader

     You can choose [download a single image] or
                     [download multiple images]

    then just enter the images adress/url
    and you'll see it in the destination directory  is [ {self.destination_dir} ]
    
    """
                print(help_info)
                



if __name__ == '__main__':
    ImageDownloader().run_interface()
    
