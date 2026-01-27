import argon2

argon2Hasher = argon2.PasswordHasher(
    time_cost=3, 
    memory_cost=64 * 1024, 
    parallelism=2, 
    hash_len=32, 
    salt_len=16 
)

password1 = "VAIBHAW2906"
hash1 = argon2Hasher.hash(password1)

password2 = "VAIBHAW2906"
hash2 = argon2Hasher.hash(password2)

print("Hash + salt of password 1:", hash1)
print("Hash + salt of password 2:", hash2)

# verify password1 against hash1
verify_valid1 = argon2Hasher.verify(hash1, password1)

# verify password2 against hash2
verify_valid2 = argon2Hasher.verify(hash2, password2)

print("Password verification success 1:", verify_valid1)
print("Password verification success 2:", verify_valid2)
