# Password Generator

A simple Python script to generate secure random passwords and save them to a file.

## Features

- Generates a random password using letters, digits, and punctuation
- Customizable password length (default: 15 characters)
- Appends generated passwords to `passwords.txt`

## Requirements

- Python 3.x

## Usage

1. Clone or download this repository.
2. Run the script:

   ```bash
   python src/password_generator.py
   ```

3. The generated password will be displayed in the terminal and saved to `passwords.txt`.

## Customization

To change the password length, edit the `generate_password` function call in `src/password_generator.py`:

```python
new_password = generate_password(length=20)
```

## License

This project is licensed under the MIT License.

