class LogginMixin:
    def log(self,message):
        print(f"[LOG]{message}")
class SerializationMixin:
    def to_dict(self):
        return self.__dict__
class user(LogginMixin,SerializationMixin):
    def __init__(self,username,email):
        self.username = username
        self.email = email
User = user("amit","amit@example.com")
User.log("user created")
print((User.to_dict()))