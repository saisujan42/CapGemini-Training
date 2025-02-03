from abc import ABC, abstractmethod

class UserAuthentication(ABC):
    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def logout(self):
        pass

class GoogleAuth(UserAuthentication):
    def __init__(self):
        self.password = input("Set Your Password : ")

    def login(self):
        self.user_pwd = input("Enter Your Password : ")
        if(self.password == self.user_pwd):
            print("Google Authentication Successful.")
        else:
            print("Incorrect Password. Google Authentication Failed.")
    
    def logout(self):
        print("Successfully Logged out from Google Account.")

class FacebookAuth(UserAuthentication):
    def __init__(self):
        self.password = input("Set Your Password : ")
    
    def login(self):
        self.user_pwd = input("Enter You Password : ")
        if(self.password == self.user_pwd):
            print("Facebook Authentication Successful.")
        else:
            print("Incorrect Password. Facebook Authentication Failed.")
    
    def logout(self):
        print("Successfully Logged out from Facebook Account.")

def main():
    google = GoogleAuth()
    google.login()
    google.logout()
    
    facebook = FacebookAuth()
    facebook.login()
    facebook.logout()
main()