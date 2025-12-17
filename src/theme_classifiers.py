#detect feminist themes in horror video games
import re
from dataclasses import dataclass


THEME_KEYWORDS = {

    "motherhood": [
        "mother", "motherhood", "pregnant", "pregnancy", "childbirth", "birth",
        "giving birth", "giving birth to", "labor", "delivery",
        "miscarriage", "infant", "baby", "maternal", "her son", "daughter"
    ],

    "domesticity": [
        "domestic", "domestic abuse", "domestic violence",
        "abusive husband", "controlling husband", "controlling partner",
        "toxic relationship", "abusive relationship",
        "oppressed", "patriarchal", "patriarchy", "oppression",
        "marriage", "spouse", "wife", "husband",
        "home life", "housewife", "family", "father"
    ],

    "trauma and mental illness": [
        "trauma", "psychosis", "mental illness", "hallucination",
        "depression", "self-harm", "suicide attempt", "suicidal", "suicide",
        "ptsd", "mentally ill", "scarred", "post-traumatic", "post traumatic",
        "asylum", "bipolar", "bi-polar", "hallucinate",
        "dissociation", "repressed memory", "memory loss", "traumatic past"
    ],

    "embodiment": [
        "body horror", "embodiment", "flesh", "mutation", "mutated",
        "body", "disfigured", "disfigurement", "mutilated",
        "bodily autonomy", "experimentation", "body modification",
        "medical experimentation", "fragmented", "erased memory",
        "soul", "alter ego", "alternate reality", "memories",
        "infected", "illness"
    ],

    "captivity": [
        "kidnapped", "abducted", "held captive", "imprisoned",
        "chained", "locked up", "captive", "captivity",
        "jail cell", "locked", "escape", "escaped", "must escape",
        "prison", "restrained", "shackled"
    ],

    "violence": [
        "violent", "violence", "physical assault", "assault",
        "murder", "murdered", "killed", "stabbed",
        "decapitated", "torture", "tortured",
        "sexually assaulted", "rape", "raped",
        "forcibly", "forcefully", "abused", "kill"
    ],

    "sexualized violence": [
        "violated", "sexual assault", "sexually assaulted",
        "rape", "raped", "sexually abused", "forced"
    ],

    "female monstrosity": [
        "witch", "hag","succubus", "vampiress", "vampire", 
        "demoness", "banshee","monster", "evil", "creature"
    ],

    "girlhood horror": [
        "schoolgirl", "teenage girl", "teen", "young girl",
        "coming of age", "adolescent", "youth", "student",
        "high school", "girlhood", "girl", "young", "teenager"
    ],

    "queer themes": [
        "queer", "lgbtq", "lesbian", "bisexual", 
        "same-sex relationship", "pronouns", 
        "nonbinary", "genderfluid", "gender fluid", "sapphic"
    ]
}


@dataclass
class ThemeResult:
    themes: list
    keywords: list
    evidence_sentences: list


class ThemesClassifier:

    def __init__(self):
        self.keywords = THEME_KEYWORDS

    def classify(self, text: str) -> ThemeResult:

        if not text:
            return ThemeResult([], [], [])

        text_lower = text.lower()
        sentences = re.split(r"[.!?]\s+", text_lower)

        detected_themes = []
        detected_keywords = []
        evidence_sentences = []

        for theme, kw_list in self.keywords.items():

            theme_triggered = False

            for kw in kw_list:
                if kw in text_lower:
                    detected_keywords.append(kw)

                    
                    for sent in sentences:
                        if kw in sent and sent not in evidence_sentences:
                            evidence_sentences.append(sent.strip())
                            break

                    theme_triggered = True

            if theme_triggered:
                detected_themes.append(theme)

        return ThemeResult(detected_themes, detected_keywords, evidence_sentences)
