import bcrypt

class Hash:
    @staticmethod
    def bcrypt(password: str):
        
        pwd_bytes = password.encode('utf-8')
        
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(pwd_bytes, salt)
       
        return hashed_password.decode('utf-8')

    @staticmethod
    def verify(hashed_password, plain_password):
        password_byte = plain_password.encode('utf-8')
        hashed_byte = hashed_password.encode('utf-8')
        return bcrypt.checkpw(password_byte, hashed_byte)