# 🚀 LaravelDevStarter

**LaravelDevStarter** is a powerful yet simple Python GUI tool that allows you to easily start a Laravel development server directly from the project's root directory. Whether you want to serve on `localhost` or your machine's local IP address, this tool provides an intuitive way to launch your server with real-time log updates.

---

## 🎯 Key Features

- **Quick Start**: Start the Laravel development server on `localhost` or with your machine’s local IP address.
- **User-Friendly GUI**: Simple, clean, and easy-to-use interface powered by `Tkinter`.
- **Real-Time Logs**: See the Laravel server logs directly within the GUI in real time.

---

## 🛠 Prerequisites

Ensure you have the following installed on your system:

- **Python 3.x**
- **PHP** (required for running Laravel)
- **Laravel** installed in the project directory

---

## 📥 Installation

1. **Download the script**: Clone the repository directly into your Laravel project's root directory.

   ```bash
   git clone https://github.com/th3adittya/LaravelDevStarter.git
   ```

2. **Navigate to the project directory**:

   ```bash
   cd LaravelDevStarter
   ```

3. **Install the required Python packages** using the `requirements.txt`:

   ```bash
   pip3 install -r requirements.txt
   ```

---

## 🚀 Usage

1. **Run the script** from your Laravel project root directory:

   ```bash
   python3 LaravelDevStarter/command_runner.py
   ```

2. **Choose your option** from the GUI:

   - **Run Server on `localhost`**: Starts the Laravel development server on `localhost`.
   - **Run Server with Local IP**: Starts the Laravel development server using your machine’s local IP address.

3. **Real-time logs** will appear in the GUI window as you start the server.

---

## 🔧 Troubleshooting

- **Missing dependencies**: Make sure that both Python and PHP are installed and accessible from your system's PATH.
- **Tkinter errors**: If `tkinter` is not installed on Linux, you may need to install it manually:
  ```bash
  sudo apt-get install python3-tk
  ```

## 📄 License

This project is licensed under the **Apache 2.0 License**. See the [LICENSE](LICENSE) file for more details.

---

## 👨‍💻 Developer

Developed by **Adi Hasan**.

- **GitHub**: [th3adittya](https://github.com/th3adittya)

Feel free to contribute to the project or suggest improvements!

### Key Enhancements:

- Added headers and emoji icons for visual appeal.
- Divided sections with horizontal rules (`---`) for better readability.
- Used clear, direct language with a focus on user experience.
- Added more detailed troubleshooting information for common issues.

### Usage Instructions:

1. Clone the repository directly into the **Laravel project root**.
2. The script (`command_runner.py`) must reside in the Laravel root for the tool to work correctly, as it interacts with `php artisan serve` from there.

Let me know if this fits your needs or if you'd like further refinements!
