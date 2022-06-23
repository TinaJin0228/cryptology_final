import random

class rsa:
    n = 0
    q = 0
    p = 0
    phi = 0
    e = 0
    d = 0
    ctext = ""
    text = ""

    # 欧几里得算法，求a b的最大公因数
    def gcd(self,a,b):
        if(b==0):
            return a
        else:
            return self.gcd(b, a%b)


    # 广义欧几里得算法
    # 计算 ax + by = 1中的x与y的整数解（a与b互质）
    def ext_gcd(self, a, b):
        if b == 0:
            x1 = 1
            y1 = 0
            x = x1
            y = y1
            r = a
            return r, x, y
        else:
            r, x1, y1 = self.ext_gcd(b, a % b)
            x = y1
            y = x1 - a // b * y1
            return r, x, y



    def exp_mode(self, base, exponent, n):
        bin_array = bin(exponent)[2:][::-1]
        r = len(bin_array)
        base_array = []
        
        pre_base = base
        base_array.append(pre_base)
        
        for _ in range(r - 1):
            next_base = (pre_base * pre_base) % n 
            base_array.append(next_base)
            pre_base = next_base
            
        a_w_b = self.__multi(base_array, bin_array, n)
        return a_w_b % n

    def __multi(array, bin_array, n):
        result = 1
        for index in range(len(array)):
            a = array[index]
            if not int(bin_array[index]):
                continue
            result *= a
            result = result % n # 加快连乘的速度
        return result

    def egcd(self, a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = self.egcd(b % a, a)
            return (g, x - (b // a) * y, y)

    # 素性检验
    def is_prime(num):
        if num == 2:
            return True
        if num < 2 or num % 2 == 0:
            return False
        for n in range(3, int(num**0.5)+2, 2):
            if num % n == 0:
                return False
        return True

    def generateRandomPrim(self):
        while(1):
            ranPrime = random.randint(0,65536)
            if self.is_prime(ranPrime):
                return ranPrime

    def generate_keyPairs(self):
        self.p = self.generateRandomPrim()
        self.q = self.generateRandomPrim()
        
        self.n = self.p*self.q
        # print("n ",n)

        self.phi = (self.p-1) * (self.q-1) 
        # print("phi ",phi)
        
    
        self.e = random.randint(1, self.phi)
        g = self.gcd(self.e,self.phi)
        while g != 1:
            self.e = random.randint(1, self.phi)
            g = self.gcd(self.e, self.phi)
            
        # print("e=",e," ","phi=",phi)

        self.d = self.egcd(self.e, self.phi)[1]
        
        # 保证d是正的
        self.d = self.d % self.phi
        if(d < 0):
            d += self.phi
            
        return ((self.e,self.n),(d,self.n))
            
    def decrypt(self,private_key):
        try:
            key,n = private_key
            self.text = [chr(pow(char,key,n)) for char in self.ctext]
            return "".join(self.text)
        except TypeError as e:
            print(e)

    def encrypt(self,public_key):
        key,n = public_key
        self.ctext = [pow(ord(char),key,n) for char in self.text]
        return self.ctext




if __name__ == '__main__':
    a = rsa()
    public_key,private_key = a.generate_keyPairs()
    print("Public: ",public_key)
    print("Private: ",private_key)
    
    ctext = a.encrypt("Hello World",public_key)
    print("encrypted  =",ctext)
    plaintext = a.decrypt(ctext, private_key)
    print("decrypted =",plaintext)