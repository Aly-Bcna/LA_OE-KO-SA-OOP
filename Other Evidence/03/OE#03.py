OE#03

class SocialMediaAccount():
    def __init__(self,username,password):
        self.username= username
        self.password= password

    def login():
        pass

    def post():
        pass
    
class InstagramAccount(SocialMediaAccount):
    def __init__(self, username, password, followers):
        super().__init__(username, password)
        self.followers= followers

    def share_story():
        pass
        
class TwitterAccount(SocialMediaAccount):
    def __init__(self, username, password, tweets):
        super().__init__(username, password)
        self.tweets= tweets

    def tweets():
        pass
    
user1= InstagramAccount("alybcna", "Cutie2004", 300)
user2= TwitterAccount("Alybcna", "Cutie2004", 5)
