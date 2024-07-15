# README

## Overview

This repository contains a simple command-line encryption and decryption tool. The main functionality is implemented in `main.py`, and the supporting functions for input/output, encryption, and decryption are organized in `iofunc.py`, `encrypt.py`, and `decrypt.py` respectively.

## File Descriptions

### `main.py`

This is the main script that runs the encryption and decryption tool. It allows the user to choose between encrypting, decrypting, or exiting the program.

**Functions and Structure:**
- **reverseString**: A lambda function to reverse a given string.
- **Main loop**: Continuously prompts the user for an action until they choose to exit.

### `iofunc.py`

This script contains functions for handling input and output operations.

**Functions:**
- `takeInputString()`: Prompts the user to enter a string and returns it.
- `giveOutputString(S: str)`: Prints the provided string.

### `encrypt.py`

This script contains functions related to the encryption process.

**Functions:**
- `countChar(S: str) -> str`: Counts consecutive characters and returns a string where each character is followed by its count.
- `hexCount(S: str) -> str`: Converts the counts in the string to their hexadecimal equivalents.

### `decrypt.py`

This script contains functions related to the decryption process.

**Functions:**
- `decCount(S: str) -> str`: Converts hexadecimal counts back to decimal.
- `addChar(S: str) -> str`: Expands the character counts back to the original string.

## How to Run

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/your-repo.git
    cd your-repo
    ```

2. **Run the main script**:
    ```bash
    python main.py
    ```

3. **Follow the on-screen instructions**:
    - Enter `0` to encrypt a string.
    - Enter `1` to decrypt a string.
    - Enter `2` to exit the program.

## Example Usage

```plaintext
Encrypt - 0
Decrypt - 1
Exit - 2: 0
Enter string: hello
Encrypted string: o4l2e1h1

Encrypt - 0
Decrypt - 1
Exit - 2: 1
Enter string: o4l2e1h1
Decrypted string: hello
```

## Contributing

If you would like to contribute to this project, please fork the repository and create a pull request. For major changes, please open an issue first to discuss what you would like to change.

## Contact

For any questions or feedback, please open an issue or contact me at [jaimeenbhagat@outlook.com].