# CheckLink

![image](https://github.com/user-attachments/assets/ca003027-8aa1-468b-86d6-2a57f9bde43c)

CheckLink is a command-line tool designed to validate and verify various types of online links and addresses. From WhatsApp groups to social media profiles, CheckLink helps you confirm the validity and obtain information about various online resources.

## 📋 Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Available Options](#available-options)
- [Bulk Verifications](#bulk-verifications)
- [Contributions](#contributions)
- [License](#license)

## ✨ Features

- Validation of WhatsApp and Telegram groups
- Verification of Facebook and Instagram profiles
- Checking availability of DNS domains
- Website validation
- Email address verification
- Support for bulk verifications using TXT files

## 🛠 Prerequisites

- Python 3.6+
- pip (Python package manager)
- Git (optional, for cloning the repository)

## 💻 Installation

1. Clone the repository (or download as ZIP):
   ```
   git clone https://github.com/obed-tc/checkLink
   ```

2. Navigate to the project directory:
   ```
   cd checklink
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## ⚙️ Configuration

To use the email verification functions, you'll need API tokens from Abstract API and MailBox Validator. Follow these steps to set them up:

1. Sign up at [Abstract API](https://www.abstractapi.com/) and [MailBox Validator](https://www.mailboxvalidator.com/) to obtain your free API tokens.

2. Open the `checklink.py` file and look for the following lines:

   ```python
   keyAbstract = "YOUR TOKEN HERE"
   keyMailBox = "YOUR TOKEN HERE"
   ```

3. Replace the values of `keyAbstract` and `keyMailBox` with your own tokens.

## 🚀 Usage

To run CheckLink, use the following command in the terminal:

```
python checklink.py
```

![image](https://github.com/user-attachments/assets/42ffc5cd-d065-45d0-a79a-df4489e65ce1)

Follow the on-screen instructions to select the desired option and provide the necessary information.

## 🔍 Available Options

1. **WhatsApp Group**: Verify the validity of WhatsApp group links.
2. **Telegram Group**: Check the validity of Telegram group links.
3. **Email**: Validate email addresses.
4. **Phone Number**: (Coming soon) Verification of phone numbers.
5. **Facebook Profile**: Validate Facebook profiles.
6. **Instagram Profile**: Verify Instagram profiles.
7. **DNS**: Check the availability of DNS domains.
8. **Websites**: Verify website accessibility.
9. **Zoom URL**: (Coming soon) Validation of Zoom links.
10. **Google Meet URL**: (Coming soon) Verification of Google Meet links.

## 📊 Bulk Verifications

CheckLink allows for bulk verifications using TXT files. You'll find sample files for each type of verification in the repository. To use this feature:

1. Select the desired option in the main menu.
2. When prompted, choose the bulk verification option.
3. Enter the path to the TXT file (e.g., `examples/whatsapp_groups.txt`).

The results of bulk verifications will be saved in a new TXT file in the project directory.
> **Note:** This content is provided for educational purposes only. Please use it responsibly.

## 🤝 Contributions

Contributions are welcome. Please open an issue to discuss significant changes before creating a pull request.

## 📄 License

This project is under the MIT License. See the `LICENSE` file for more details.

---

Developed with ❤️ by obed-tc
