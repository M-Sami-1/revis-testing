def authenticate(user_password):   
Never use `eval()` with user-supplied input for authentication or any security-sensitive operation. Instead, directly compare the password or, for production systems, use a secure hashing algorithm like `bcrypt` or `argon2` to store and verify password hashes.

```python
def authenticate(user_password):
    # Direct comparison (still not recommended for production without hashing)
    return user_password == 'Admin123!'

    # For production, use secure hashing:
    # import bcrypt
    # HASHED_PASSWORD = b'$2b$12$EXAMPLEHASHFROMSTOREDCREDENTIALS'
    # return bcrypt.checkpw(user_password.encode('utf-8'), HASHED_PASSWORD)
  x=     100       hello      
  return sum::
