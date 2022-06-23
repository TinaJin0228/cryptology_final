from aes import aes
from rsa import rsa
from hash import hash


class client:
    pub = (0,0)
    pri = (0,0)
    aeskey = 0
    r = rsa()
    a = aes()
    h = hash()

    def __init__(self):
        self.pub,self.pri = self.r.generate_keyPairs()
        self.aeskey = self.a.calc_extend_key()



if __name__ == "__main__":
    alice = client()
    bob = client()

    # transmit key
    m1 = bob.r.encrypt(alice.aeskey,bob.pub)
    s1 = alice.r.encrypt(alice.h.makehash(alice.aeskey),alice.pri)

    tmp1 = bob.h.makehash(bob.r.decrypt(m1,bob.pri))
    tmp2 = alice.r.decrypt(s1,alice.pub)

    if(tmp1 == tmp2):
        print("successfully transmitted aes key")
        bob.aeskey = bob.r.decrypt(m1,bob.pri)
        print("aes key: ",bob.aeskey)


    # secure communication
    # M = "this is an example"
    alice.a.plainArray = M
    m2 = alice.a.encrypt()
    s2 = alice.r.encrypt(alice.h.makehash(alice.a.plainArray),alice.pri)

    tmp1 = bob.h.makehash(bob.a.decrypt(m2))
    tmp2 = alice.r.decrypt(s2,alice.pub)

    if(tmp1==tmp2):
        print("successfully commnunicated")
        bob.a.plainArray = bob.a.decrypt(m2)
        print("message: ",bob.a.plainArray)