def rsa(txt):
    p = 59969537
    q = 193877777
    e = 2345637457
    n = p * q
    f = (p-1) * (q-1)
    d = pow(e,-1,f)
    public_key = e,n
    private_key = d,n
    print(f"Публічний ключ:{public_key}")
    print(f"Приватний ключ:{private_key}")
    print(f"Вхідний текст:{txt}")
    encrypted_message = [pow(ord(char),e,n) for char in txt]
    print(f"Зашифроване повідомлення:{encrypted_message}")
    decrypted_message = [chr(pow(char, d, n)) for char in encrypted_message]
    decrypted_message = "".join(decrypted_message)
    print(f"Розшифроване повідомлення:{decrypted_message}")