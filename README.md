# my-portfolio
A personal portfolio website showcasing scientific and computational projects through interactive visualizations and engaging user experiences.

- Example repo: https://github.com/lshriver/portfolio-original

## Project Structure
```aiignore
my-portfolio/
├── static/
│   ├── css/
│   │   ├── main.css
│   │   └── tech-icons.css
│   ├── images/
│   │   ├── favicon.png
│   │   ├── logo.png
│   │   └── wisp.jpg
│   ├── js/
│       └── common.js
├── templates/
│   └── base.html
├── LICENSE
├── README.md
├── app.py         # old flask application
└── index.html
```

## Features
- **Interactive project showcase:** Links to main projects (see below).
- **Responsive design:** Mobile-friendly layout with intuitive navigation.
- **Tech Icon Tooltips:** Hover effects showing technology icons used in each project.

## Main Projects
- 📜 **There and Back Again:** A personal Zettelkasten built using PreTeXt.
- 🎈 **Streamlit Projects:** Demonstrations of scientific streamlit projects with interactive elements.
  - Neural signals app
  - Kuramoto model app
  - Thermodynamics and PCA app
  - Bifurcation diagram app
- 🐈‍⬛ **Github:** Github repositories that demonstrate mathematical and computational abilities.
## Minimal Apps and Visualizations
- 🪐 **Kepler's Laws:** A fun javascript-powered visualization of Kepler's laws.
- 🔊 **Text-to-speech:** A simple text-to-speech app.

## Technical Implementation
- **Framework:** Flask (Python)
- **Frontend:** HTML5, CSS3, JavaScript
- **Math Rendering:** MathJax
- **Styling:** Custom CSS with gradient effects and responsive design.
- **Interactivity:** Vanilla JavaScript for animations and uer interactions.

## Running the Application
1. Ensure Python 3.10+ is installed.
2. Install required dependencies: `pip install -r requirements.txt`.
3. Run the Flask application: `python app.py`
4. Access site preview at http://localhost:5000/.
