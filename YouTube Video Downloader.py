#"Aplicatie" de descărcat  videouri de pe internet(YouTube)

from pytube import YouTube

def descarca(url):
    yt = YouTube(url)                 
    yt = yt.streams.get_highest_resolution()  
    yt.download()    


print("Dati likul pt descarcare")
#print("Scrie 'STOP'ca sa inceapa descarcarea") 

url = input()
descarca(url)
