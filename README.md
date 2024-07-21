# 🤖 Ano Transfer Bot

## 📜 Description

Ano Transfer Bot is a Telegram bot that handles video and photo messages. It echoes back any video or photo received in a private chat and sends a log of these messages to a designated surveillance group. The bot is intended to operate only in private messages, not in groups or channels.

## 🌟 Features

- **🔄 Echo Videos and Photos:** The bot will send back any video or photo it receives in a private chat.
- **🔍 Surveillance Logging:** All videos and photos sent to the bot are also forwarded to a private surveillance group with user information.
- **🔒 Private Chat Only:** The bot only functions in private chats and will notify users if added to a group or channel.

## 🛠️ Installation

1. **📥 Clone the Repository:**
    ```bash
    git clone https://github.com/AceModz/Ano-Transfer-Bot.git
    ```
2. **📂 Navigate to the Project Directory:**
    ```bash
    Ano-Transfer-Bot
    ```
3. **🌐 Create and Activate a Virtual Environment (optional but recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    ```
4. **📦 Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

5. **⚙️ Configure the Bot:**
   - Replace `YOUR_BOT_TOKEN_HERE` with your Telegram bot token.
   - Replace `YOUR_GROUP_ID_HERE` with your private group's ID.

6. **🚀 Run the Bot:**
    ```bash
    python ano_transfer_bot.py
    ```

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
