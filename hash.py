
# 利用平方取中法获得16位消息摘要

class hash:
    message = ""
    abstract = 0
    
    def makehash(self):
        binary_converted = int(''.join(format(ord(c), 'b') for c in self.message),2)
        binary_converted = binary_converted % 65536
        binary_converted = binary_converted*binary_converted
        binary_converted = binary_converted % 16777216 #2^24 = 16777216
        self.abstract = binary_converted // 256
#         print(bin(self.abstract))
#         print(self.abstract)



if __name__ == "__main__":
    a = hash()
    a.message = "here is an example"
    print("message:",a.message)
    print("abstract:")
    a.makehash()
