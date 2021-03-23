import sys

class Crypt:
    def __init__ (self,key):
        self.key = key

    def encrypt (self,msg):
        keyList = list(self.key)
        msgList = list(msg)
        keyLen = len(keyList)
        msgLen = len(msgList)
        cipherText = ['']*msgLen
        for i in range(msgLen):
            cipherText[i] = msgList[i] ^ keyList[i%]

    def decrypt (self,msg):
        keyList = list(self.key)
        msgList = list(msg)
        keyLen = len(keyList)
        msgLen = len(msgList)
        cipherText = ['']*msgLen
        for i in range(msgLen):
            cipherText[i] = chr(ord(msgList[i] ^ keyList[i% keyLen]))
if __name__=="__main__":

    print(sys.argv)
    if len(sys.argv) > 2:
        if sys.argv[1]=='-e':
            c=Crypt(sys.argv[2])
            c.encrypt(sys.argv[3])
        elif sys.argv[1]=='-d':
            c=Crypt("123")
            c.decrypt("aaaaa")
