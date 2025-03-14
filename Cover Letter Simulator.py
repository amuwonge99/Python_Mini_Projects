#Cover Letter Template#

name: str = input('What is your name? ')
age: int = input('How old are you? ')
current_role: str = input('What is your current role? ')
current_company: str = input('Name of your current company? ')
company_applying_for: str = input('Name of the company you are applying for? ')
job_title: str = input('Job title you are applying for? ')
recruiter_or_employer: str = input('Name of the recruiter/employer? ')
notice_period: int = input('What is your notice period (in weeks)? ')

Template: str = f"""
----------------------------------------------------------------------------------------
Hi {recruiter_or_employer},

I am expressing my interest in being a {job_title} for {company_applying_for}.
I am an extremely hard working {age} year old who goes above and beyond to complete all tasks assigned to me.
In addition to this, I am known to take initiative in offering help wherever necessary.

I currently work as a {job_title} for {current_company}. I enjoy working at this company, however I am looking for a new challenge.
My notice period is {notice_period} weeks. Attached is my CV and I hope to be hearing from you soon!

Regards,

{name}

"""
print (Template)