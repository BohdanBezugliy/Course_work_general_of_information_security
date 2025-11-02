class Crypto:
    __p = 400009
    __q = 700001
    __e = 100000000133
    __n = __p * __q
    __f = (__p - 1) * (__q - 1)
    __d = pow(__e, -1, __f)
    public_key = __e, __n
    __private_key = __d, __n

    def rsa_decrypt(txt):
        d,n = Crypto.__private_key
        decrypted_txt = ""
        for char in txt.split(" "):
            if char:
                decrypted_txt += chr(pow(int(char), d, n))
        with open("out.txt","w") as f:
            f.write(decrypted_txt)
        return decrypted_txt

    def rsa_encrypt(txt):
        e,n = Crypto.public_key
        encrypted_txt = ""
        with open("input.txt","w") as f:
            f.write(txt)
        for char in txt:
            encrypted_txt += str(pow(ord(char),e,n))+" "
        with open("close.txt","w") as f:
            f.write(encrypted_txt)
        return encrypted_txt