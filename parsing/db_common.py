from collections import Counter

from settings import DB


def save_to_db_hard_skills_and_count(words_counter: Counter, db=DB):
    cursor = db.cursor()
    cursor.executemany(
        """
        INSERT OR IGNORE INTO hard_skills (tech_words) VALUES (?)
        """,
        [(key,) for key in words_counter.keys()]
    )
    cursor.executemany(
        """
        INSERT OR IGNORE INTO hard_skill_count 
        (tech_word_id, word_count) 
        VALUES ((SELECT id FROM hard_skills WHERE tech_words = ?), ?)
        """,
        [(key, value) for key, value in words_counter.items()]
    )
    db.commit()
