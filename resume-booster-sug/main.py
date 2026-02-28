import ai_rewriter
import gap_calculator
import text_analyser


def main():
    resume_content = """Software Engineer with 2 years of experience in backend and full-stack development. 
    Proficient in Java, Spring Boot, and REST API development. 
    Worked on microservices architecture and integrated AWS services such as EC2 and S3. 
    Experienced in SQL and database optimization. 
    Built scalable systems with Docker and basic CI/CD pipelines. 
    Collaborated with cross-functional teams in Agile environment. 
    Strong understanding of data structures and system design fundamentals."""


    job_description_content = """We are looking for a Backend Software Engineer with strong experience in Java and Spring Boot. 
    The candidate should have hands-on experience building scalable microservices and RESTful APIs. 
    Experience with AWS services including EC2, S3, and Lambda is required. 
    Knowledge of Docker, Kubernetes, and CI/CD pipelines is preferred. 
    Strong understanding of database design, SQL, and system architecture is expected. 
    Familiarity with distributed systems and cloud-native development is a plus."""

    # extract keywords
    resume_keywords = text_analyser.extract_keywords(resume_content)
    jd_keywords = text_analyser.extract_keywords(job_description_content)

    # collect gaps
    missing_keywords = gap_calculator.find_missing_keywords(resume_keywords, jd_keywords)
    # find current ATS
    current_score = gap_calculator.current_match(resume_keywords, jd_keywords)

    # know the gaps and improvement pointers
    suggestions = ai_rewriter.suggest_improvements(resume_content, job_description_content, missing_keywords)

    print("ATS Match Score:", current_score)
    print("Missing Keywords:", missing_keywords)
    print("Suggested Improvements:\n", suggestions)



if __name__ == "__main__":
    main()
