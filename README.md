<p align="center">
    <img src="./neoclock.png" width="128" height="128" alt="neoclock logo"/>
</p>

## neoclock

**neoclock** is a stylish ASCII art terminal clock using **pyfiglet** and **termcolor**. It allows you to view the current time in a beautifully formatted ASCII style with customizable fonts, colors, and configurations.

---

## 🚀 Features

- **Real-time Clock**: Displays the current time in ASCII art.
- **Custom Fonts**: Choose from various fonts provided by **pyfiglet**.
- **Color Customization & Gradients**: Adjust the text with gradients.
- **Cross-Platform**: Works on whatever runs Python.
- **Persistent Configuration**: Your custom settings are saved in a config file, and you can easily adjust them at any time.

---

## 📜 Installation

You can install **neoclock** from source.

### **From Source**
Clone the repository and run the Python script (after installing dependencies):

```bash
git clone https://github.com/judeeey/neoclock.git
cd neoclock
pip install -r requirements.txt
python3 neoclock.py
```

---

## 🧰 Configuration

### Config File Location

neoclock uses a configuration file to store your preferences. The configuration file contains settings for the font, text color, and background color of the clock.

- **Linux**: `~/.config/neoclock/neoclock.conf`
- **Windows**: `%APPDATA%/neoclock/neoclock.conf`

### Default Configuration

When running neoclock for the first time, you will be prompted to create a config file. Here's the structure of the configuration file:

```ini
neoclock_font: <font_name>
neoclock_color1: <color_name>
neoclock_color2: <color_name>
```

You can change these settings at any time by manually editing the file or using the `--font`, `--color1`, `--color2` and `--bg` flags when launching neoclock.

### Example:

```ini
neoclock_font: slant
neoclock_color1: orange
neoclock_color2: yellow
```

---

## 🧑‍💻 Usage

Once installed, you can use **neoclock** in your terminal. Here are the available commands and options:

### 1. **Run neoclock**

Simply run the following command to start the clock:

```bash
python neoclock.py
```

### 2. **Available Commands:**

- `-c1`, `--color1`: Set the start color of the gradient.
- `-c2`, `--color2`: Set the end color of the gradient.
- `-f`, `--font`: Set the font of the figlet.
- `--list-fonts`: List all available fonts.
- `-i`, `--info`: Display neoclock version, release date, author, and GitHub page.
- `-rc`, `--reset-conifg`: Reset current configuration file, get prompted to set up like the first launch

### Examples:

- Start neoclock with the saved config:

    ```bash
    python neoclock.py
    ```

- Start neoclock with a blue-magenta gradient and slant font:

    ```bash
    python neoclock.py -c1 blue -c2 magenta -f slant
    ```

- Show the version and author info:

    ```bash
    python neoclock.py --info
    ```

---

## 💾 Dependencies

**neoclock** depends on the following Python libraries:

- **pyfiglet**: Used to generate ASCII art for the clock.
- **colorama**: Add color support & emoji support to the terminal, aditionally supplying gradients.

You can install them via `pip`:

```bash
pip install pyfiglet colorama
```
or with:
```bash
pip install -r requirements.txt
```

---

## 🛑 Restrictions

**neoclock** cannot be run as root (`sudo`). This is for security reasons and to avoid potential misconfigurations. If you attempt to run it with `sudo`, it will exit with an error message.

---

## 🛠️ Development

If you'd like to contribute to **neoclock**, follow these steps:

1. Fork the repository on GitHub.
2. Clone your fork locally:

    ```bash
    git clone https://github.com/yourusername/neoclock.git
    cd neoclock
    ```

3. Make your changes and commit them.

4. Push your changes and create a pull request.

---

## 🤖 Author

**neoclock** is developed and maintained by **[judeeey](https://judey.net)**.

---

## 📃 License

This project is licensed under the GNU GPL v3 License - see the [LICENSE](LICENSE) file for details.
