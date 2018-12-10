import hashlib, uuid, 

class Session():
    def __init__(self,user, pwd):
        if autheticate(self.user, self.pwd):
            return generate_session_Token(self.user, self.pwd)
        else:
            return error_response(1)
        
    def generate_session_Token(user, pwd):
        salt = get_salt(user)
        hashed_password = hashlib.sha512(pwd.encode('utf-8') + salt.encode('utf-8')).hexdigest()
        
        
