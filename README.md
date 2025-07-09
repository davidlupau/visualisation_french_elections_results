# 🇫🇷 French Presidential Elections 2022: A Data Science Journey

*Uncovering voting patterns, political geography, and democratic engagement across France*

## 📊 Project Overview

What drives French voters? How do political preferences vary across departments? This project explores the 2022 French Presidential election through the lens of exploratory data analysis, revealing fascinating patterns hidden within electoral data.

Using Python's powerful data science ecosystem, this analysis transforms raw electoral data into compelling visual narratives that illuminate France's political landscape.

## 🎯 Key Discoveries

### 🏆 **The Fragmentation Effect**
While Marine Le Pen finished second individually (22.64%), the **far-right achieved the highest combined score** at 30.2% when accounting for vote fragmentation across multiple candidates.

### 🗺️ **Geographic Political Clustering**
French political preferences follow distinct regional patterns:
- **Far-right dominance** in southeastern and northeastern regions
- **Center strength** concentrated in western departments  
- **Far-left** primarily limited to urban areas like Île-de-France

### 📉 **The Abstention Challenge**
Abstention reached **25.9%** - a significant 4.6 percentage point increase from 2017, with striking geographical correlations:
- Overseas territories: up to **69% abstention**
- Smaller departments show higher variability in participation
- Political extremes correlate with higher abstention rates

## 🛠️ Technical Implementation

### **Data Pipeline**
```
Raw Electoral Data → Preprocessing → Statistical Analysis → Visualization → Insights
```

### **Technology Stack**
- **Python**: Core analysis language
- **Pandas**: Data manipulation and preprocessing
- **Matplotlib & Seaborn**: Statistical visualizations
- **Plotly**: Interactive choropleth maps
- **Excel Integration**: Automated analysis output

### **Code Architecture**
```
src/
├── constants.py          # Candidate mappings and configurations
├── data_processing.py    # Data loading and transformation functions
├── statistical_analysis.py # Core analytical computations
├── visualisations.py     # Plotting functions and map generation
└── main.py              # Orchestration and execution
```

## 🔍 Analytical Approach

This project demonstrates:

1. **Systematic Data Exploration**: From basic quality assessment to complex geographical patterns
2. **Multi-dimensional Analysis**: Individual candidates, political orientations, and geographical distributions
3. **Visual Storytelling**: Each visualization answers specific analytical questions
4. **Statistical Rigor**: Applying established methods for correlation and distribution analysis

## 📈 Visualization Highlights

### **Interactive Choropleth Maps**
- Department-level political orientation mapping
- Abstention rate geographical distribution
- GeoJSON integration for accurate French boundaries

### **Statistical Graphics**
- Box plots revealing abstention-extremism correlations
- Violin plots showing department size effects
- Scatter plots identifying geographical outliers

### **Comparative Analysis**
- Bar charts with politically-aware color schemes
- Pie charts for participation analysis
- Strip plots combining categorical and continuous data


## 🚀 Skills Demonstrated

### **Data Science Core Competencies**
- ✅ Data quality assessment and preprocessing
- ✅ Statistical analysis (correlation, distribution, outlier detection)
- ✅ Data visualization and cartographic representation
- ✅ Geographical data handling (GeoJSON, choropleth mapping)

### **Software Engineering Practices**
- ✅ Modular code architecture
- ✅ Function documentation and error handling
- ✅ Automated analysis pipeline
- ✅ Version control and project organization

### **Domain Knowledge Application**
- ✅ Political science understanding
- ✅ French electoral system knowledge
- ✅ Statistical methodology selection
- ✅ Academic writing and reporting

## 📁 Repository Structure

```
visualisation_french_elections_results/
├── 📊 data/                    # Electoral datasets
├── 🔧 src/                     # Source code modules
├── 📈 analysis_output/         # Generated Excel reports and plots
├── 📓 notebooks/               # Interactive notebooks
```

## 🏃‍♂️ Quick Start

```bash
# Clone the repository
git clone https://github.com/davidlupau/visualisation_french_elections_results.git

# Install dependencies
pip install pandas matplotlib seaborn plotly openpyxl requests

# Run the complete analysis
python src/main.py

# Explore interactively
jupyter notebook jupyter/exploration.ipynb
```
