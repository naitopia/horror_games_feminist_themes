# Horror Games Feminist Themes Dataset
*A project for Introduction to Digital Humanities (DHUM 7000) at the CUNY Graduate Center, instructed by Dr. Jojo Karlin and Dr. Krystyna Michael.*

---

### Trigger Warning
This project includes analysis of sensitive themes such as horror content, trauma, gender-based and sexual violence.

---

### Project Aims
The horror video game genre, shaped by a male-dominated industry, has historically centralized masculine perspectives in both creation and representation. Women and the LGBTQ+ community are underrepresented both in production roles as developers and designers, and also in game content, where characters often portray characters through harmful tropes, such as hyper-sexualization and/or victimization. 

**This data set seeks to identify and analyze:**
- Possible feminist themes
    - Motherhood, trauma, oppression, gender-based violence
- Harmful tropes
    -Sexual violence, female monstrosity 
- LGBTQ+ themes when present

**What problems does this dataset seek to address?**
- There are no existing datasets categorizing horror video games through the feminist lens.
- Horror scholarship traditionally focuses on films, not games. 
- Video games are artifacts that hold valuable cultural insight.

---

**This dataset is based on publicly available Wikipedia content.**

All analysis is based solely on Wikipedia text, acknowledging:
- Uneven article quality
- Structural bias in what gets documented
- The limitations of keyword-based classification

---

**This project requires Python 3.10 or 3.11**.

Create a virtual environment:

    python -m venv venv
    venv\Scripts\activate      # Windows
    source venv/bin/activate   # macOS / Linux

Install dependencies:

    pip install -r requirements.txt


### File Structure
    horror_games_feminist_themes/
    |
    |- data/
    |   feminist_themes_reviewed.csv
    |        raw/
    |        feminist_themes_raw.csv
    |        with_female_protagonists.curated.csv
    |        with_female_protagonists_raw.csv
    |   
    |- documentation/
    |   data_dictionary.md
    |   methodology.md
    |   README.md
    |   requirements.txt
    |
    |- notebooks/
    |   scrape_wiki_female_protagonists.ipynb
    |   scrape_wiki_themes.ipynb
    |  
    |- src/
    |   __init__.py
    |   female_protagonists_classifiers.py
    |   theme_classifiers.py
    |   wiki_scraper.py 
    |
    |- venv #this project was executed on a virtual environment


---

### Contact
Naila Butt | Email: nbutt@gradcenter.cuny.edu 






