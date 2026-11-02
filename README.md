Random Password Generator

Project Description

The Random Password Generator is a Python-based application that creates strong and secure passwords according to user-selected criteria. It provides both a Command Line Interface (CLI) and a Graphical User Interface (GUI).

The application uses Python's "secrets" module to generate secure random passwords.

Objectives

- Generate strong and secure passwords.
- Allow users to select different character types.
- Validate password length and user selections.
- Display password strength.
- Allow users to copy passwords to the clipboard.
- Maintain a history of the last five generated passwords during the current session.

Technologies Used

- Programming Language: Python
- GUI Library: Tkinter
- Security Module: secrets
- String Module: string
- Clipboard Library: pyperclip
- IDE: Visual Studio Code

Features

Basic Features

1. Enter the desired password length (minimum 8 characters).
2. Select at least two character types:
   - Uppercase letters (A–Z)
   - Lowercase letters (a–z)
   - Numbers (0–9)
   - Special symbols (!, @, #, etc.)
3. Generate a password based on the selected criteria.
4. Validate invalid inputs.
5. Generate multiple passwords without restarting the application.

Advanced Features

1. Graphical User Interface using Tkinter.
2. Password length selection using a spinbox.
3. Checkboxes for selecting character types.
4. Password strength indicator (Weak, Medium, Strong).
5. Secure password generation using the "secrets" module.
6. Guarantee at least one character from each selected character type.
7. Automatically copy generated passwords to the clipboard.
8. Option to copy passwords manually.
9. Option to exclude ambiguous characters such as 0, O, 1 and l.
10. Maintain the last five generated passwords in session history.
11. Clear the current password or clear the entire history.

Project Structure

Random-Password-Generator/
│
├── password_generator.py
├── password_gui.py
└── README.md

Installation and Setup

Step 1: Install Python

Download and install Python from:
https://www.python.org/

Step 2: Install Required Library

Open the VS Code terminal and run:

pip install pyperclip

Step 3: Run the GUI Application

python password_gui.py

Step 4: Run the CLI Application

python password_generator.py

How to Use

1. Open the application.
2. Select the required password length.
3. Choose at least two character types.
4. Enable the exclude-similar-characters option if required.
5. Click Generate Password.
6. View the generated password and its strength.
7. Copy the password using the Copy Password button or use the automatic clipboard copy.
8. View the last five generated passwords in the history section.

Security

The application uses Python's "secrets" module instead of the ordinary "random" module because "secrets" is designed for security-sensitive random generation.

Password history is stored only in memory during the current application session. It is not saved permanently to a file or database.

Conclusion

The Random Password Generator is a useful Python project that helps users create secure passwords easily. It combines secure password generation, input validation, password strength checking, clipboard functionality and a user-friendly graphical interface.