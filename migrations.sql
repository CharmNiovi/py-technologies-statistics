CREATE TABLE IF NOT EXISTS hard_skills (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tech_words VARCHAR[100] NOT NULL,
    UNIQUE(tech_words)
);

CREATE TABLE IF NOT EXISTS hard_skill_count (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tech_word_id int NOT NULL,
    word_count INTEGER NOT NULL,
    parse_date DATE DEFAULT (date('now', 'localtime')),
    FOREIGN KEY (tech_word_id) REFERENCES hard_skills(id),
    UNIQUE(tech_word_id, parse_date)
);