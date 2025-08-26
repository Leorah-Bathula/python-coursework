class Youtube:
    def playvideo(self):
        print("Video is running with....")
        print("ads will run")
        print("no background run")
        print("low quality")
        print("play back speed (upto 2x)")
        
    def youtubeMusic(self):
        print("No access")
    
    def likes(self):
        print("you can like")
        
    def share(self):
        print("you can share")
    def comments(self):
        print("you can comment")
    def subscribe(self):
        print("you can subscibe")
    def upload(self):
        print("you can upload")
    def watchhistory(self):
        print("you can view the watchhistory")
    
class PremiumYoutube(Youtube):
    def playvideo(self):
        print("Video is running with...")
        print("ads free")
        print("background run")
        print("high quailty")
        print("play back speed (upto 3x)")
        
    def youtubeMusic(self):
        print("Exclusive music")
    def downloads(self):
        print("you cna download all videos with high quality")
        
leo = PremiumYoutube()        
print("\nLeo- PremiumYoutube")
leo.playvideo()
leo.youtubeMusic()
leo.downloads()
leo.likes()
leo.comments()
leo.subscribe()
leo.upload()
leo.watchhistory()


jes = Youtube()        
print("\nJes- PremiumYoutube")
jes.playvideo()
jes.youtubeMusic()
jes.likes()
jes.comments()
jes.subscribe()
jes.upload()
jes.watchhistory()
        
'''

Leo- PremiumYoutube
Video is running with...
ads free
background run
high quailty
play back speed (upto 3x)
Exclusive music
you cna download all videos with high quality
you can like
you can comment
you can subscibe
you can upload
you can view the watchhistory

Jes- PremiumYoutube
Video is running with....
ads will run
no background run
low quality
play back speed (upto 2x)
No access
you can like
you can comment
you can subscibe
you can upload
you can view the watchhistory

=== Code Execution Successful ===
'''

