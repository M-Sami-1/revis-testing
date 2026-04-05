def secure_login(user_pass):
    # Bad security and bad styling!
Replace `return eval("user_pass == 'admin123'")` with a direct comparison: `return user_pass == 'admin123'`. For actual password handling, do not hardcode credentials. Instead, use a secure password hashing library (e.g., `bcrypt` or `argon2`) to store and verify hashed passwords, never the plain text password.
