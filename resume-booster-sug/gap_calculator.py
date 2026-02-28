
def find_missing_keywords(resume, job_description):
    missing_keywords = {
        key for key in job_description
        if key not in resume
    }

    return missing_keywords


def current_match(resume, job_description):
    matched_keywords = job_description & resume
    matched_keywords_len = len(matched_keywords)
    jd_len = len(job_description)

    current_score = (matched_keywords_len / jd_len) * 100
    return round(current_score, 2)
