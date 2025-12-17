# Methodology

# Project Overview
This project constructs a dataset of horror video games that present possible feminist themes drawn from Wikipedia’s *Horror Video Games* category tree. The goal is to create a dataset that can help analyze patterns, harmful tropes, and portrayals of women and queer characters.

# Theoretical Framework
### Johanna Drucker — Data as Interpretation
- Classification requires acknowledging all interpretive decisions, subjective boundaries, and biases.
- “Data is capta.”

> "Capta is “taken” actively while data is assumed to be a “given” able to be recorded and observed."

### Catherine D’Ignazio & Lauren Klein — Data Feminism
- Exposing invisible labor 
- Examining structural inequalities

> “Data feminism asserts that data are not neutral or objective. They are the products of unequal social relations, and this context is essential for conducting accurate, ethical analysis.”

### Barbara Creed — The Monstrous-Feminine
- Horror historically frames female bodies and reproductive system as threatening, monstrous, or abject.
- This perspective helps interpret themes of embodiment, motherhood, trauma, and “female monstrosity” in games.

Horror studies is typically centered around film, and video games are often underexamined as cultural artifacts. Insights and analyses from scholars such as Barbara Creed such as monstrosity, embodiment, and patriarchal anxieties in horror film highlight the parallel structures and patterns within horror video games, revealing how similar gendered logics operate across different types of media.

---

# Data Collection

### 1. Wikipedia Web-Scrape
Using `Python`, `BeautifulSoup`, and `wikipediaapi`, the scraper collected:
- All Wikipedia pages within **Category:Horror_video_games**
- All subcategories (e.g., "1990s horror video games," "Survival horror")

Extracted metadata included:
- Title  
- Wikipedia page URL
- Category/subgenre

### 2. Female Protagonist Classification
Created a classifier to find games with possible female protagonists, using:
- Control phrases (“you play as…”, “the protagonist is…”)
- Gender terms (“woman,” “girl,” “she,” etc.)

---

### 3. Manual Review and Curation
Because Wikipedia pages vary in depth/development:
- Each flagged game was manually reviewed.
- Only games with:
  - Playable female and/or genderfluid protagonists
  - Sufficiently developed content on Wikipedia pages

were kept in the curated list of games to interpret. 

---

### 4. Theme Classification
After created a curated list, a new classifier was made to detect possible femninist themes.

**Themes detected:**
- Motherhood  
- Domesticity  
- Trauma and mental illness  
- Embodiment  
- Captivity  
- Violence  
- Sexualized violence    
- Girlhood horror  
- Female monstrosity  
- Queer themes  

---

### 5. Manual Review and Interpretation
- Metadata columns manually added 
- All detected keywords were manually reviewed, and terms were adjusted or removed when they did not substantively align with the interpretive goals of the thematic category.
 
---

### 6. Limitations
- Wikipedia pages vary drastically in length and detail which is not always a reliable source of complete analysis. 
- Classifiers may miss other themes.  

---

### 7. Future Goals
- Improve and expand classifiers 
- Incorporate non-Wikipedia sources (developer interviews, reviews, essays)  
- Visualize patterns