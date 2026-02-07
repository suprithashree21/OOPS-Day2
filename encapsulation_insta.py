class InstagramAccount:
    def __init__(self, account_name, password):
        self.account_name = account_name          
        self._private_reels = []                  
        self.__archived_reels = []               
        self.__password = password                
    def add_private_reel(self, reel_name):
        self._private_reels.append(reel_name)
        print(f"Private reel '{reel_name}' added successfully.")
    def display_private_reels(self, is_follower):
        if is_follower:
            print("Private Reels:")
            for reel in self._private_reels:
                print("-", reel)
        else:
            print("Access Denied! Only followers can view private reels.")
    def add_archived_reel(self, reel_name):
        self.__archived_reels.append(reel_name)
        print(f"Archived reel '{reel_name}' added successfully.")
    def display_archived_reels(self, password):
        if password == self.__password:
            print("Archived Reels:")
            for reel in self.__archived_reels:
                print("-", reel)
        else:
            print("Access Denied! Only account holder can view archived reels.")
    def get_archived_reels(self, password):
        if password == self.__password:
            return self.__archived_reels
        else:
            return "Access Denied!"
    def set_password(self, old_password, new_password):
        if old_password == self.__password:
            self.__password = new_password
            print("Password updated successfully.")
        else:
            print("Incorrect old password! Cannot update.")
account1 = InstagramAccount("Supritha_tech", "1234")
account1.add_private_reel("Trip to Goa")
account1.add_private_reel("College Memories")
print()
account1.add_archived_reel("First Vlog")
print("\n Display Private Reels")
account1.display_private_reels(True)    
account1.display_private_reels(False)     
print("\nDisplay Archived Reels")
account1.display_archived_reels("1234")   
account1.display_archived_reels("0000")   
print("\n Update Password")
account1.set_password("1234", "5678")
print("\n Check Archived Reels with New Password")
account1.display_archived_reels("5678")