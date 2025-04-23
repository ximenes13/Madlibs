# 🧠 MadLib Generator with Python + Selenium

This project is a **MadLib-style random story generator** written in Python, using `Selenium` to optionally **fill in a web form** with generated stories. Words are loaded from a structured `.json` file, and stories are assembled dynamically using templates.

---

## 🚀 Features

- 🎲 Generates random, funny stories from templates
- 📁 Reads words and templates from an external `JSON` file
- 🌐 Uses `Selenium` to automatically interact with webpages (e.g. fill out forms)
- 🛠️ Easily customizable: add your own templates or words

---

## 🖥️ Technologies Used

- Python 3.x
- Selenium WebDriver
- JSON for structured input
- (Optional) ChromeDriver or another browser driver for automation

---

## 📂 Project Structure

- **madlib.json**: Contains the MadLib templates and corresponding placeholders (e.g., `{{adjective}}`, `{{noun}}`, etc.) that will be filled in by the user. Each story template is represented as an object with a `template` and `filled` key.
- **main.py**: The main Python script for generating MadLibs. It loads the JSON file, prompts the user for input to fill in the placeholders, and displays the final story. If configured with Selenium, it can also automatically submit the story via a web form.

## 🛠️ Setup

### Step 1: Clone the Repository

To get started, clone this repository to your local machine using the following command:

  `git clone https://github.com/your-username/madlib-project.git`

### Step 2: Dependencies

Make sure you have Python 3.x installed. You can check your version with:
  `python --version`

Install selenium with:
 `pip install selenium`

### Step 3: Install WebDriver

To interact with the web using Selenium, you'll need a WebDriver for your browser (e.g., ChromeDriver or GeckoDriver). Download the appropriate version for your browser.

### Step 4:Run the project

Once you've installed the dependencies and set up the WebDriver, you can run the main Python script to generate and interact with MadLibs.
  `python main.py`

---

## 🤝 Contributing

Contributions are welcome! If you'd like to improve the project, feel free to:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to your branch (`git push origin feature-name`).
5. Submit a pull request.

If you find bugs or have feature requests, please [open an issue](https://github.com/your-username/madlib-project/issues).




