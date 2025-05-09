# 🧠 MadLib Generator with Python + Flask

This project is a web-based MadLib-style random story generator built using `Python` and `Flask`, with `HTML/CSS` for the frontend and `JSON` as the data source. Users can dynamically fill in the blanks to generate fun, custom stories — all within a browser interface.

---

## 🚀 Features

🎲 Generates funny and dynamic stories using JSON-based templates <br>
📁 Reads placeholders and templates from external `.json` file <br>
🌐 Interactive form inputs built with HTML and styled using CSS <br>
🛠️ Easily customizable — just add new templates or words in the JSON file <br>
⚡ Runs locally in your browser using Flask

---

## 🖥️ Technologies Used

- Python 3.x
- Flask
- HTML5 / CSS3
- JSON for structured input
- PyCharm (recommended IDE)

---

## 📂 Project Structure

- **madlib.json**: Contains the MadLib templates and corresponding placeholders (e.g., `{{adjective}}`, `{{noun}}`, etc.) that will be filled in by the user. Each story template is represented as an object with a `templates` and `values` key.
- **main.py**: The main Python script for the Flask application. It loads the madlib.json file, serves the web pages (via Flask routes), collects user inputs via forms, and renders the final generated MadLib on a results page.
- **index.html**: Focused on a button to generate a MadLib story.
- **style.css**: Custom CSS for styling the webpage. This file will handle the look and feel of the input form, the results page, and overall design.
- **script.js**: Handles the dynamic creation of input fields based on the `.json` file and generate a madlib story.

---

## 🛠️ Setup

### Step 1: Clone the Repository

To get started, clone this repository to your local machine using the following command:

  `git clone https://github.com/your-username/Madlibs.git`

### Step 2: Dependencies

Make sure you have Python 3.x installed. You can check your version with:
  `python --version`

Install flask with:
 `pip install flask`

### Step 3: Run the project

Once you've installed the dependencies and set up the WebDriver, you can run the main Python script to generate and interact with MadLibs.
  `python3 main.py`
  
---

## 🤝 Contributing

Contributions are welcome! If you'd like to improve the project, feel free to:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to your branch (`git push origin feature-name`).
5. Submit a pull request.

If you find bugs or have feature requests, please [open an issue](https://github.com/ximenes13/Madlibs/issues).




