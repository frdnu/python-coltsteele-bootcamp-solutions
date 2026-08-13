# comprehensions
"""
Write a function process_prices(price_map: dict) -> dict that takes a dictionary 
of item names and USD prices (e.g., {"laptop": 1000, "mouse": 20, "free_sample": 0}).
Use a dictionary comprehension to filter out items priced at 0 or below, convert the 
remaining prices to local currency by multiplying by 0.31, and round to 2 decimal places.
"""


def process_prices(price_map: dict) -> dict:
    process_1_prices = {k: v for k, v in price_map if v > 0}
    process_2_prices = {k: v*0.31 for k, v in process_1_prices}
    return process_2_prices


# flexible arguments
"""
Write a function create_user(user_id: int, *skills: str, **attributes):
It must take an integer ID, any number of skill strings as positional arguments, 
and any keyword arguments (like role="dev", location="remote").
Return a single dictionary containing "id", a list of "skills", 
and all passed keyword attributes integrated inside.
"""


def create_user(user_id: int, *skills: str, **attributes):
    return {"id": user_id, "skills": list(skills)} | attributes


# builtin functions
"""
Write a function evaluate_grades(scores: list[int]) -> dict:
Use all() to check if every grade is ge 50.
Use any() to check if at least one grade is ge 90.
Use sum(), len(), min(), and max() to calculate average, minimum, and maximum.
Return these metrics in a clean dictionary.
"""


def evaluate_grades(scores: list[int]) -> dict:
    all_ge_50 = all(score >= 50 for score in scores)
    any_ge_90 = any(score >= 90 for score in scores)
    max = max(scores)
    min = min(scores)
    average = sum(scores)/len(scores)

    return {"all_ge_50": all_ge_50, "any_ge_90": any_ge_90, "average": average}


# error handling
"""
Create a custom exception class InvalidAgeError(Exception).
Write a function verify_age(age_input) that attempts to convert age_input to an integer 
inside a try block.
If conversion fails, catch ValueError and print an error message.
If integer is $< 18$, raise InvalidAgeError.Use else to print "Access Granted",
and finally to print "Verification Complete".
"""
