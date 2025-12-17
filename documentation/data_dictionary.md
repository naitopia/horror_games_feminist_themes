## Data Dictionary
**Core metadata fields in final (reviewed) CSV file:**

`title` *name of video game*

`wiki_page` *URL to Wikipedia page*

`horror_subgenre` *category/subgenre the game was scraped from*

`developers` *extracted from infobox*

`female_developer_present?` *manually added column*

`release_date` *earliest release inputted; column manually reviewed and formatted*

`platforms` *column manually reviewed and formatted*

`player_perspective` *column manually added; left blank if unable to identify*

`female_protagonist_playable_character?` *column manually added; if playable character is female or genderfluid = true*

**Theme & Keywords Columns**

>*Each theme has a boolean (true/false) column and a keyword column (semicolon-separated)*

`motherhood` *boolean; indicates themes of motherhood such as pregnancy, birth, and/or maternal roles/relationships*

`motherhood_keywords` *e.g., mother, baby, pregnancy*

`domesticity` *boolean; indicates complicated family structures, patriarchal themes, and domestic abuse*

`domesticity_keywords` *e.g., family, husband, marriage*

`trauma_and_mental_illness` *boolean; indicates references to psychological trauma and/or mental illness*

`trauma_and_mental_illness_keywords` *e.g., asylum, trauma, hallucination*

`embodiment` *boolean; indicates whether game explores bodily experiences, transformation, or loss of bodily autonomy*

`emobdiment_keywords` *e.g., infected, mutation, memories*

`captivity` *boolean; indicates whether confinement, imprisonment, or restricted autonomy is involved*

`captivity_keywords` *e.g., captive, chained, locked, imprisoned*

`violence` *boolean; indicates references to physical violence or bodily harm*

`violence_keywords` *e.g., killed, stabbed*

`sexualized_violence` *boolean; indicates references to sexual violence*

`sexualized_violence_keywords` *e.g., sexual assault, rape*

`girlhood_horror` *boolean; indicates whether the game is centered on young character(s), or has young character(s)*

`girlhood_horror_keywords` *e.g., young girl, school girl, teenager*

`woman_as_monster` *boolean; indicates whether female characters are represented as monstrous, inhuman, or abject* 

`woman_as_monster_keywords` *e.g., demon, vampire, monster, witch*

`queer_themes` *boolean; indicates whether game has LGBTQ+ identities/themes*

`queer_themes_keywords` *e.g., lesbian, nonbinary, genderfluid, queer*

`combined_keywords` *column manually added to combine all theme keywords*

`interpretative_evidence_sentences` *column manually added to store selected or relevant evidence sentences; often added as evidence for manual changes to keywords*
   
