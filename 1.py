import re

text = "Email me at example@gmail.com or admin@yahoo.com"

pattern = r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b'

# Search
match = re.search(pattern, text)

# Find all
matches = re.findall(pattern, text)

print("Search Result:", match.group() if match else "No match")
print("All Matches:", matches)























# import re

# # Sample text
# text = """
# Contact us at support@example.com or admin@test.org.
# Call us at +91-9876543210 or 9123456789.
# Python is powerful. Python is easy to learn.
# """

# # 1. Search for a word using re.search()
# pattern_word = r"Python"
# search_result = re.search(pattern_word, text)

# if search_result:
#     print("Word Found:", search_result.group())
#     print("Position:", search_result.start(), "to", search_result.end())
# else:
#     print("Word Not Found")

 

# # 2. Find all occurrences using re.findall()
# pattern_all_words = r"Python"
# all_matches = re.findall(pattern_all_words, text)
# print("All occurrences of 'Python':", all_matches)

 

# # 3. Match pattern at the beginning using re.match()
# pattern_begin = r"Contact"
# match_result = re.match(pattern_begin, text)

# if match_result:
#     print("Match found at beginning:", match_result.group())
# else:
#     print("No match at beginning")

 

# # 4. Extract all email addresses
# email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
# emails = re.findall(email_pattern, text)
# print("Email Addresses Found:", emails)

 

# # 5. Extract all mobile numbers (10 digits)
# phone_pattern = r"\b[6-9]\d{9}\b"
# phones = re.findall(phone_pattern, text)
# print("Mobile Numbers Found:", phones)
