import requests 
from bs4 import BeautifulSoup 
import lxml
import os
  
''' 
URL of the archive web-page which provides link to 
all video lectures. It would have been tiring to 
download each video manually. 
In this example, we first crawl the webpage to extract 
all the links and then download videos. 
'''
  
# specify the URL of the archive here 
archive_url = "https://bookaudio.online/651-dune.html/"
  
def get_video_links(): 
      
    # create response object 
    r = requests.get(archive_url) 
      
    # create beautiful-soup object 
    soup = BeautifulSoup(r.content,'html5lib') 
      
    # find all links on web-page 
    links =  soup.find_all('li', {'class': "track"})
  
    # filter the link sending with .mp4 
    video_links = ["https:"+ link['data-url'] for link in links if link['data-url'].endswith('mp3')] 
  
    return video_links 
  
  
def download_video_series(video_links): 
  
    for link in video_links: 
  
        '''iterate through all links in video_links 
        and download them one by one'''
          
        # obtain filename by splitting url and getting 
        # last string 
        file_name = str(video_links.index(link)+1)+".mp3"

        if os.path.exists(file_name):
            print(file_name + " exists")
        else:

            print( "Downloading file:%s"%file_name) 
            
            # create response object 
            r = requests.get(link, stream = True) 
            
            #download started 
            with open(file_name, 'wb') as f: 
                for chunk in r.iter_content(chunk_size = 1024*1024): 
                    if chunk: 
                        f.write(chunk)
            
            print( "%s downloaded!\n"%file_name )
    
    print ("All videos downloaded!")
    return

video_links = get_video_links() 
  
    # download all videos 
download_video_series(video_links) 