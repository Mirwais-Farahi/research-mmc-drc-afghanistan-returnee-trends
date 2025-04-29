
# MMC-DRC Refugee Returnee Analysis – Afghanistan

## 📚 Overview

This project analyzes refugee and returnee experiences in Afghanistan based on survey data collected by the Mixed Migration Centre (MMC) and the Danish Refugee Council (DRC). It aims to unpack the complex drivers of migration, the realities of return, and the challenges faced by returnees upon reintegration into Afghan society. The study provides evidence to inform programming, protection efforts, and policy decisions on mixed migration and durable solutions.

## 🎯 Objectives

- Explore drivers and motivations behind migration and return.
- Assess reintegration challenges across economic, social, legal, and psychological domains.
- Map experiences of protection risks, access to services, and rights violations.
- Inform stakeholders with gender-, location-, and age-disaggregated insights.

## 📦 Project Structure

```
├── data/                  # Raw and processed survey data
├── notebooks/             # Jupyter notebooks for EDA and analysis
├── scripts/               # Python scripts for preprocessing, cleaning, and visualization
├── outputs/               # Generated charts, maps, and summary reports
├── README.md              # Project documentation
├── requirements.txt       # Python dependencies
├── LICENSE                # License file (e.g., MIT)
```

## 🗂️ Data Overview (Survey Modules)

| Module | Thematic Area |
|--------|----------------|
| Informed Consent & Enumerator Observation | Consent, privacy, presence of others |
| Migration History | Country of return, duration abroad, legal status |
| Education & Skills | Formal education, skill acquisition |
| Economic Activity | Income sources, sectors, remittances, current livelihood |
| Return Experience | Legal status, deportation, voluntary return, route |
| Reintegration Challenges | Safety, housing, income, documentation, stigma |
| Access to Services | Health, education, shelter, ID documentation |
| Social Integration | Belonging, community ties, contributions |
| Psychological Wellbeing | Emotional stress, trauma, coping mechanisms |
| Support & Assistance | Before return, after return, by whom |
| Future Plans | Intentions to re-migrate, investment, satisfaction |

## ⚙️ Methodology

- **Data Cleaning**: Handling missing entries, value standardization, logical consistency checks.
- **Quantitative Analysis**:
  - Descriptive statistics (frequencies, cross-tabs)
  - Comparative analysis (e.g., gender-wise experience differences)
  - Statistical tests (e.g., chi-square, t-tests)
- **Qualitative Tagging** (for open-ended responses)
- **Visualization**: Province-wise maps, migration journey flows, stacked bar and donut charts.

## 📊 Key Analytical Scenarios

- **Gender-wise analysis**: return reasons, reintegration stress, school attendance
- **Province-wise returnee distribution**
- **Correlation between legal status abroad & reason for return**
- **Income generation vs. economic reintegration challenges**
- **Safety and psychological stress comparison (by gender, province)**
- **Impact of prior support received on reintegration outcomes**
- **Mapping intention to migrate again vs. satisfaction level**

## 🛠️ Requirements

```bash
pip install -r requirements.txt
```

Key Libraries:
- `pandas`, `numpy`, `matplotlib`, `seaborn`
- `scikit-learn` (for clustering or pattern analysis)
- `geopandas` and `folium` (for map visualizations)

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/[your-username]/mmc-drc-refugee-returnee-analysis-afghanistan.git
   ```

2. Navigate to the project folder:
   ```bash
   cd mmc-drc-refugee-returnee-analysis-afghanistan
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Open JupyterLab/Notebook to begin analyzing:
   ```bash
   jupyter notebook
   ```

## 📈 Sample Visualizations

- Gender-wise reason for migration (stacked bar)
- Timeline of return across provinces (line plot)
- Returnee economic activities by location (donut chart)
- Psychological stress indicators by gender (heatmap)

## 🤝 Acknowledgements

This work is made possible through collaboration with:
- **Mixed Migration Centre (MMC)**
- **Danish Refugee Council (DRC)**
- **Adroit Associates** – Research and Analysis Unit

## 📜 License

MIT License – Use and share freely, with attribution.
