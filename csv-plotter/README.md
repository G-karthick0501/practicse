# 📊 CSV Plotter - Interactive Data Visualization Tool

A Python-based desktop application for loading, analyzing, and visualizing CSV data with an intuitive graphical interface. Built using Tkinter and Matplotlib following SOLID principles and modular architecture.

---

## 🎯 Features

### Core Functionality
- ✅ **CSV File Loading** - Browse and load CSV files with validation
- ✅ **Data Preview** - View data in tabbed interface with adjustable row count
- ✅ **Statistics Dashboard** - Automatic calculation of mean, median, min, max, standard deviation
- ✅ **Multiple Chart Types** - Line charts and bar charts
- ✅ **Interactive Charts** - Zoom, pan, and save charts in multiple formats (PNG, PDF, JPG, SVG)
- ✅ **Column Selection** - Choose X and Y axes from available columns
- ✅ **Data Validation** - Automatic validation of file paths, data integrity, and numeric columns
- ✅ **Status Bar** - Real-time feedback on operations
- ✅ **Error Handling** - User-friendly error messages

### Technical Features
- 🏗️ **Modular Architecture** - Following SOLID principles for maintainability
- 🔧 **Loose Coupling** - Independent, testable modules
- 📦 **Package Structure** - Organized codebase with clear separation of concerns
- 🎨 **Configurable** - Centralized configuration for easy customization
- 💾 **Export Charts** - Save visualizations in high quality (300 DPI)

---

## 📋 Requirements

### Operating System
- **Windows**: Windows 10 or later
- **Linux**: Ubuntu 20.04+ or any modern distribution
- **macOS**: macOS 10.14+ (not tested but should work)

### Software Dependencies
- **Python**: 3.8 or higher
- **pip**: Python package installer

### Python Libraries
```
pandas>=2.0.0
matplotlib>=3.7.0
```

---

## 🚀 Installation

### Step 1: Clone or Download the Repository
```bash
git clone https://github.com/G-karthick0501/aeron-assignment.git
cd csv-plotter
```

Or download and extract the ZIP file.

### Step 2: Create Virtual Environment (Recommended)

**Windows:**
```bash
py -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run the Application
```bash
py main.py
```

---

## 📖 How to Use

### 1. **Launch Application**
```bash
py main.py
```

### 2. **Load CSV File**
- Click the **"Browse CSV File"** button
- Select your CSV file from the file dialog
- The application will validate and load the data

### 3. **Preview Data**
- Switch between **"📊 Data Preview"** and **"📈 Statistics"** tabs
- Adjust the number of rows to display using the spinbox (5-100 rows)
- View automatic statistics for all numeric columns

### 4. **Select Columns**
- Choose **X-axis Column** from the first dropdown
- Choose **Y-axis Column** from the second dropdown (must be numeric)

### 5. **Choose Chart Type**
- Select **Line Chart** for trends over time
- Select **Bar Chart** for comparisons

### 6. **Generate Chart**
- Click **"Generate Chart"** button
- A new window will open with your interactive chart
- Use the toolbar to zoom, pan, or reset the view

### 7. **Save Chart**
- Click **"💾 Save Chart"** button in the chart window
- Choose format: PNG, PDF, JPG, or SVG
- Select location and filename
- Chart saved at 300 DPI for publication quality

---

## 📂 Project Structure
```
csv-plotter/
├── main.py                          # Application entry point
├── requirements.txt                 # Python dependencies
├── README.md                        # This file
├── sample_data/                     # Sample CSV files
│   ├── sales_data.csv
│   ├── temperature_data.csv
│   └── student_scores.csv
└── src/
    ├── core/                        # Core business logic
    │   ├── config/                  # Configuration modules
    │   │   ├── app_config.py        # Application settings
    │   │   ├── chart_config.py      # Chart settings
    │   │   ├── ui_config.py         # UI colors and styles
    │   │   └── messages.py          # Error/status messages
    │   ├── charts/                  # Chart creation modules
    │   │   ├── chart_base.py        # Common chart utilities
    │   │   ├── chart_saver.py       # Chart export functionality
    │   │   ├── line_chart.py        # Line chart implementation
    │   │   └── bar_chart.py         # Bar chart implementation
    │   └── csv_handler.py           # CSV file operations
    ├── gui/                         # User interface
    │   ├── widgets/                 # Reusable UI components
    │   │   ├── buttons.py           # Button factory
    │   │   ├── labels.py            # Label factory
    │   │   ├── inputs.py            # Input widgets factory
    │   │   └── frames.py            # Frame factory
    │   ├── main_window.py           # Main application window
    │   ├── file_handler.py          # File operations handler
    │   ├── preview_panel.py         # Data preview component
    │   └── status_bar.py            # Status bar component
    └── utils/
        └── validators/              # Data validation
            ├── file_validator.py    # File path validation
            └── data_validator.py    # Data integrity validation
```

---

## 🤖 AI Tools Used

This project was developed with assistance from **Claude 3.5 Sonnet (Anthropic)** through the Claude.ai interface.

### AI-Generated Components
- Initial project structure and module organization
- Tkinter GUI layout and widget creation
- Matplotlib chart generation code
- Modular architecture refactoring
- Configuration management system
- Validation logic
- Error handling implementation
- Documentation structure

### Manual Modifications Made
1. **Import Path Fixes** - Corrected circular imports and package references
2. **Bug Fixes** - Fixed attribute ordering in `preview_panel.py` (`num_rows` initialization)
3. **File Organization** - Created proper package structure with `__init__.py` files
4. **Chart Window Design** - Modified to open charts in separate windows instead of embedding
5. **Save Chart Feature** - Enhanced with multiple format support (PNG, PDF, JPG, SVG)
6. **Statistics Tab** - Added comprehensive data statistics display
7. **Error Messages** - Refined user-facing error messages for clarity
8. **Testing and Debugging** - Tested with various CSV formats and fixed edge cases
9. **Code Review** - Reviewed and optimized generated code for performance
10. **Documentation** - Wrote comprehensive README with installation and usage instructions

### Development Workflow

**Typical interaction pattern:**
1. **Human:** Described desired functionality or problem
2. **AI:** Generated code implementation
3. **Human:** Tested, identified issues, requested fixes
4. **AI:** Provided corrected code
5. **Human:** Integrated, tested again, made final adjustments

**Example:**
- **AI generated:** Chart embedded in main window (cluttered UI)
- **Human decided:** Charts should open in separate windows
- **AI provided:** New implementation with `Toplevel` windows
- **Human added:** Save button with format selection

---

## 🎨 Customization

### Changing Colors

Edit `src/core/config/ui_config.py`:
```python
COLORS = {
    "line_chart": "#2196F3",  # Blue
    "bar_chart": "#4CAF50",   # Green
    "primary": "#4CAF50",     # Button color
    # ... modify as needed
}
```

### Adjusting Chart Size

Edit `src/core/config/chart_config.py`:
```python
CHART_SETTINGS = {
    "window_width": 1000,     # Chart window width
    "window_height": 700,     # Chart window height
    "figure_width": 12,       # Plot width in inches
    "figure_height": 7,       # Plot height in inches
    # ... other settings
}
```

---

## 🐛 Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'pandas'"
**Solution:** Install dependencies with `pip install -r requirements.txt`

### Issue: Charts not displaying
**Solution:** Ensure matplotlib backend is properly configured. Try: `pip install --upgrade matplotlib`

### Issue: "Invalid file path" error
**Solution:** Ensure the CSV file exists and you have read permissions

### Issue: "Y-axis must be numeric" error
**Solution:** Select a numeric column (not text) for the Y-axis

### Issue: Empty chart window
**Solution:** Check that your CSV has valid numeric data in the selected columns

---

## 📝 Sample Data Files

Three sample CSV files are included in the `sample_data/` folder:

1. **sales_data.csv** - Monthly sales revenue, expenses, and profit
2. **temperature_data.csv** - Daily temperature, humidity, and wind speed readings
3. **student_scores.csv** - Student names and test scores across subjects

Use these to test the application features.

---

## 🎓 Architecture & Design Principles

This project follows **SOLID principles**:

- **Single Responsibility**: Each module has one clear purpose
- **Open/Closed**: Easy to extend (add new chart types) without modifying existing code
- **Liskov Substitution**: Components are interchangeable
- **Interface Segregation**: Minimal, focused interfaces
- **Dependency Inversion**: Modules depend on abstractions, not concrete implementations

### Key Design Patterns Used
- **Factory Pattern**: Widget creation (`widgets/` package)
- **Strategy Pattern**: Chart type selection
- **Observer Pattern**: Status bar updates
- **Module Pattern**: Package-based code organization

---

## 📸 Screenshots

### Data Preview Tab
![Screenshot 1](screenshots/1.png)

### Statistics Tab
![Screenshot 2](screenshots/2.png)

### Line Chart Example
![Screenshot 3](screenshots/3.png)

### Bar Chart Example
![Screenshot 4](screenshots/4.png)

---

## 🔮 Future Enhancements

Potential features for future versions:
- [ ] Scatter plot support
- [ ] Data filtering capabilities
- [ ] Multiple Y-axis columns on same chart
- [ ] Export data after filtering
- [ ] Dark mode theme
- [ ] Recent files list
- [ ] Keyboard shortcuts
- [ ] Chart customization panel (colors, styles)
- [ ] CSV auto-delimiter detection
- [ ] Statistical tests and correlations

---

## 📄 License

This project was created as part of an AI Prototyping Intern assignment for Aeron Systems.

---

## 🙏 Acknowledgments

- **Open-Meteo API** - Inspiration for modular weather dashboard design
- **Anthropic Claude** - AI assistance in rapid prototyping
- **Matplotlib** - Powerful charting library
- **Pandas** - Data manipulation and analysis

---

## 📧 Contact

For questions or feedback about this assignment submission, please contact through the provided channels.

---

**Built with ❤️ using Python, Tkinter, and AI-assisted development**
