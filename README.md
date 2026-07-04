# 📂 Smart File Organizer

A Python automation project that automatically organizes files into categorized folders based on their extensions.

---

## ✨ Features

- 📁 Automatically organizes files into folders
- 🖼️ Supports Images, Documents, Videos, Music, Archives, Text Files, and Others
- 📂 Creates folders automatically if they don't exist
- 🔄 Handles duplicate filenames safely
- 📝 Logs every file movement
- ↩️ Undo organization using `undo.py`
- 🛡️ Cross-platform using Python's built-in libraries

---

## 🛠 Technologies Used

- Python 3
- os
- shutil
- logging

---

## 📁 Project Structure

```text
Smart-File-Organizer/
│
├── organizer.py
├── undo.py
├── config.py
├── utils.py
├── logger.py
├── organizer.log
├── README.md
├── requirements.txt
├── .gitignore
├── LICENSE
└── screenshots/
```

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/Shivanshbajaj1/Smart-File-Organizer.git
```

Go inside the folder

```bash
cd Smart-File-Organizer
```

---

## ▶️ Usage

### Organize Files

```bash
python organizer.py
```

Enter the folder path when prompted.

---

### Undo Organization

```bash
python undo.py
```

This restores files to their original locations using the generated log file.

---

## 📸 Screenshots

### Before

(Add screenshot here)

### After

(Add screenshot here)

---

## 📋 Supported File Types

| Extension | Category |
|-----------|----------|
| .txt | TextFiles |
| .pdf | Documents |
| .docx | Documents |
| .jpg | Images |
| .jpeg | Images |
| .png | Images |
| .mp4 | Videos |
| .mkv | Videos |
| .mp3 | Music |
| .zip | Archives |

---

## 📌 Future Improvements

- Command-line arguments
- Progress bar
- Colored terminal output
- JSON configuration
- GUI version
- Recursive folder organization
- Unit testing

---

## 👨‍💻 Author

**Shivansh Bajaj**

GitHub: https://github.com/Shivanshbajaj1

LinkedIn: https://www.linkedin.com/in/shivansh-bajaj-a433b7371/

---

## 📜 License

This project is licensed under the MIT License.
