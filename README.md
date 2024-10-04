
# Auto Clicker

A simple auto-clicker script with a GUI, allowing you to start and stop clicking at set intervals.

## Getting Started

To get started with this auto-clicker, follow these steps:

### 1. Set Up a Virtual Environment

It is recommended to create a virtual environment to keep your project dependencies isolated. To do this:

- Ensure you have **Python >= 3.12** installed on your system.
- Open a terminal or command prompt and navigate to your project directory.

#### Create the virtual environment:
```bash
python -m venv venv
```

This will create a virtual environment in a folder named `venv`.

#### Activate the virtual environment:

- **On Windows (Command Prompt)**:
    ```bash
    venv\Scripts\activate
    ```
    
- **On macOS**:
    ```bash
    source venv/bin/activate
    ```

After activation, you'll see `(venv)` in your terminal, indicating that the environment is active.

### 2. Install Dependencies

Once the virtual environment is activated, you can install the required dependencies using `pip`:

```bash
pip install pyautogui
pip install pyinstaller  # To compile the script into an executable
```

### 3. Ensure `tkinter` is Available

`tkinter` is usually included by default in Python installations. However, if you encounter issues, follow the instructions below:

- **On macOS**:
    ```bash
    brew install python-tk
    ```

- **On Windows**:
    `tkinter` should be included with the default Python installation. No additional steps are necessary.

### 4. Change the Text/Settings

You can customize the settings of the auto-clicker by editing the `main.py` file. Note the following variables:

```python
window_title = "Auto Clicker"  # The title of the window
clicker_interval = 3  # Interval between clicks in seconds
footer_text = "This text will be shown at the bottom of the window."  # Footer text
```

Modify these as needed to adjust the behavior or appearance of the application.

### 5. Running the Script

Once your environment is set up, you can run the auto-clicker with:

```bash
python main.py
```

This will open the GUI, allowing you to start and stop the auto-clicking process.

### 6. Compiling as an Executable

To compile the script into a standalone executable:

- **On Windows or macOS**, run:
    ```bash
    pyinstaller --onefile --windowed main.py
    ```

This will create an executable file:
- **On Windows**: You’ll get a `.exe` file located in the `dist/` directory.
- **On macOS**: You’ll get a `.app` file in the `dist/` directory.

If you're on macOS but need a Windows `.exe` file, you'll need to compile it on a Windows machine or use cross-compilation techniques (e.g., using a virtual machine or Docker).

### 7. Deactivating the Virtual Environment

Once you're done working in your virtual environment, you can deactivate it by running:

```bash
deactivate
```

This will return you to the system's default Python environment.

---

### Notes

- Make sure to test your compiled executable on the target operating system to ensure everything works as expected.
- PyInstaller may raise some warnings during the build process, but these are typically harmless unless there's a specific error that prevents the build.
