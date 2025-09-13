import sys
import re

# --- Input Validators ---

def get_valid_string(prompt):
    while True:
        value = input(prompt).strip()
        if value.lower() == "exit":
            print("Exiting...")
            sys.exit()
        if value:
            return value
        print("Please enter a valid, non-empty string.")

def get_valid_integer(prompt, min_value=None, max_value=None):
    while True:
        value = input(prompt).strip()
        if value.lower() == "exit":
            print("Exiting...")
            sys.exit()
        try:
            int_value = int(value)
            if (min_value is not None and int_value < min_value) or (max_value is not None and int_value > max_value):
                if min_value is not None and max_value is not None:
                    print(f"Please enter a number between {min_value} and {max_value}.")
                elif min_value is not None:
                    print(f"Please enter a number greater than or equal to {min_value}.")
                else:
                    print(f"Please enter a number less than or equal to {max_value}.")
            else:
                return int_value
        except ValueError:
            print("Please enter a valid integer.")

def get_valid_name(prompt):
    pattern = re.compile(r"^[A-Za-z\s\-']+$")
    while True:
        value = input(prompt).strip()
        if value.lower() == "exit":
            print("Exiting...")
            sys.exit()
        if pattern.fullmatch(value):
            return value
        print("Please enter a valid name.")

def get_valid_email(prompt):
    pattern = re.compile(r"^[\w\.-]+@[\w\.-]+\.\w{2,}$")
    while True:
        value = input(prompt).strip()
        if value.lower() == "exit":
            print("Exiting...")
            sys.exit()
        if pattern.fullmatch(value):
            return value
        print("Please enter a valid email address.")

def get_valid_phone(prompt):
    pattern = re.compile(r"^\+?[\d\s\-\(\)]{7,20}$")
    while True:
        value = input(prompt).strip()
        if value.lower() == "exit":
            print("Exiting...")
            sys.exit()
        if pattern.fullmatch(value):
            return value
        print("Please enter a valid phone number (digits, spaces, +, -, and parentheses allowed).")

# --- Collecting User Inputs with Validation ---

name = get_valid_name('What is your first name? ')
age = get_valid_integer('How old are you? ', min_value=13, max_value=130)
email = get_valid_email('What is your email address? ')
phone = get_valid_phone('What is your phone number? ')
current_role = get_valid_string('What is your current role? ')
current_company = get_valid_string('Name of your current company? ')
company_applying_for = get_valid_string('Name of the company you are applying for? ')
job_title = get_valid_string('Job title you are applying for? ')
recruiter_or_employer = get_valid_name('Name of the recruiter/employer? ')
notice_period = get_valid_integer('What is your notice period (in weeks)? ')

# --- Cover Letter Template ---

template = f"""
----------------------------------------------------------------------------------------
Hi {recruiter_or_employer},

I am expressing my interest in being a {job_title} for {company_applying_for}.
I am an extremely hard working {age} year old who goes above and beyond to complete all tasks assigned to me.
In addition to this, I am known to take initiative in offering help wherever necessary.

I currently work as a {current_role} for {current_company}. I enjoy working at this company, however I am looking for a new challenge.
My notice period is {notice_period} weeks. Attached is my CV and I hope to be hearing from you soon!

You can reach me via email at {email} or by phone at {phone}.

Regards,

{name}
"""

print(template)
