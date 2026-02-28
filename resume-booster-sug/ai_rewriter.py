from openai import OpenAI

import config

client = OpenAI(api_key=config.OPENAI_API_KEY)

def suggest_improvements(resume, job_description, missing_keywords):
    prompt = f"""
        Compare the resume and job description below.
        
        Resume:
        {resume}
        
        Job Description:
        {job_description}
        
        Missing Keywords:
        {missing_keywords}
        
        Provide short bullet-point improvement suggestions.
        Use plain ASCII only.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    # print("bot generated response: ",response)
    reply = response.choices[0].message.content.strip()

    return reply
