from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

SKILLS = [
    "python",
    "java",
    "javascript",
    "react",
    "flask",
    "django",
    "sql",
    "mysql",
    "mongodb",
    "html",
    "css",
    "tailwind",
    "pandas",
    "numpy",
    "matplotlib",
    "seaborn",
    "scikit-learn",
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "nlp",
    "power bi",
    "tableau",
    "excel",
    "tensorflow",
    "pytorch",
    "git",
    "github",
    "data analysis",
    "data science",
    "statistics",
    "aws",
]


def extract_skills(text):

    text = text.lower()

    found = []

    for skill in SKILLS:

        if skill in text:

            found.append(skill)

    return sorted(set(found))


def calculate_matching(resume_text, job_description):

    vectorizer = TfidfVectorizer(stop_words="english")

    vectors = vectorizer.fit_transform([resume_text, job_description])

    similarity = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]

    similarity_score = round(similarity * 100, 2)

    resume_skills = extract_skills(resume_text)

    job_skills = extract_skills(job_description)

    matched_skills = [skill for skill in job_skills if skill in resume_skills]

    missing_skills = [skill for skill in job_skills if skill not in resume_skills]

    skill_score = 0

    if len(job_skills) > 0:

        skill_score = round(len(matched_skills) / len(job_skills) * 100, 2)

    final_score = round(similarity_score * 0.6 + skill_score * 0.4, 2)

    return {
        "similarity": similarity_score,
        "skill_score": skill_score,
        "final_score": final_score,
        "resume_skills": resume_skills,
        "job_skills": job_skills,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
    }
