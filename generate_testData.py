import pandas as pd

data = {
    'Original Sentence': [
        "What type of creatures breathe air and don't lay eggs underwater?",
        "Was Ulysses Grant a general in the American Civil War?",
        "Was Grant's father-in-law a Democrat?",
        "Did Ulysses win the Battle of Champion Hill?",
        "Who was Grant's brother in law?",
        "Where was Grant born?",
        "What was Grant's political affiliation?",
        "Why did Grant say 'Damn, I had nothing to do with this battle.'?"
    ],
    'Paraphrased Sentence': [
        "Which animals breathe air and do not lay eggs beneath the water?",
        "Was Ulysses S. Grant a general during the American Civil War?",
        "Was Grant's father-in-law affiliated with the Democratic Party?",
        "Was Ulysses victorious at the Battle of Champion Hill?",
        "Who was Grant's sibling's spouse?",
        "In which place was Grant's birth?",
        "What were Grant's political beliefs?",
        "What was the reason behind Grant exclaiming, 'I had no involvement in this battle.'?"
    ]
}

df = pd.DataFrame(data)
df.to_excel("test_data.xlsx")
