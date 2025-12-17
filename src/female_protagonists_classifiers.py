#detect possible female protagonists
import re
from dataclasses import dataclass


def make_pattern(word):
    if " " in word:
        return re.compile(re.escape(word), re.IGNORECASE)
    else:
        return re.compile(rf"\b{re.escape(word)}\b", re.IGNORECASE)


CONTROL_PHRASES = [
    "player controls",
    "players control",
    "the player controls",
    "the player assumes the role of",
    "the player takes the role of",
    "the player takes control of",
    "the player character is",
    "playable character is",
    "you play as",
    "you control",
    "the protagonist is",
    "main character is",
]

FEMALE_TERMS = [
    "female protagonist",
    "girl",
    "young girl",
    "schoolgirl",
    "teenage girl",
    "young woman",
    "woman",
    "heroine",
    "female lead",
    "woman protagonist",
    "girlfriend",
    "wife",
    "she",
    "her",
]

CONTROL_PATTERNS = [make_pattern(p) for p in CONTROL_PHRASES]
FEMALE_PATTERNS = [make_pattern(t) for t in FEMALE_TERMS]


@dataclass
class FemaleProtagonistResult:
    has_female_protagonist: bool
    evidence_sentence: str | None = None
    evidence_type: str | None = None


class FemaleProtagonistClassifier:

    def classify(self, text: str) -> FemaleProtagonistResult:
        if not text:
            return FemaleProtagonistResult(False)

        text_lower = text.lower()
        sentences = re.split(r"[.!?]\s+", text_lower)


        if re.search(r"\bfemale protagonist\b", text_lower):
            return FemaleProtagonistResult(
                True,
                evidence_sentence="Contains explicit phrase 'female protagonist'.",
                evidence_type="explicit_phrase",
            )

        for sent in sentences:
            if any(p.search(sent) for p in CONTROL_PATTERNS) and \
               any(f.search(sent) for f in FEMALE_PATTERNS):
                return FemaleProtagonistResult(
                    True,
                    evidence_sentence=sent.strip(),
                    evidence_type="control+female_term",
                )

        for sent in sentences:
            if re.search(r"\bprotagonist\b", sent) and re.search(r"\bshe\b", sent):
                return FemaleProtagonistResult(
                    True,
                    evidence_sentence=sent.strip(),
                    evidence_type="protagonist+she",
                )

        return FemaleProtagonistResult(False)
