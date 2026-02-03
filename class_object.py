class Instagram:
    
    def __init__(self, title, description, creator_name, location):
        self.title = title
        self.description = description
        self.creator_name = creator_name
        self.location = location
        self.likes = 0
        self.comments = []   
    
  
    def display_title(self):
        print("The title of the reel is:", self.title)
        
    def display_description(self):
        print("The description of the reel is:", self.description)
        
    def display_creator(self):
        print("Creator Name:", self.creator_name)
        
    def display_location(self):
        print("Location:", self.location)
        
    def display_likes(self):
        print("The likes of the reel is:", self.likes)
        
    def display_comments(self):
        print("Comments:")
        if not self.comments:
            print("No comments yet.")
        else:
            for comment in self.comments:
                print("-", comment)
    
   
    def liked(self):
        self.likes += 1
        
    def disliked(self):
        if self.likes > 0:
            self.likes -= 1
    
   
    def add_comment(self, comment):
        self.comments.append(comment)
    
    
    def delete_last_comment(self):
        if self.comments:
            removed = self.comments.pop()
            print("Removed comment:", removed)
        else:
            print("No comments to delete.")
reel1 = Instagram("Dancing", "Dancing with friends", 
                  "Bharath P", "Mysore")

reel1.add_comment("Awesome reel!")
reel1.add_comment("Nice energy!")
reel1.add_comment("Loved it!")

reel1.display_comments()

print("\nDeleting last comment...\n")
reel1.delete_last_comment()

reel1.display_comments()