# Example how to use apostrophe correctly, ano when not

message = "For programmer John O'Hara one of the advantages of Python is it versatility and devoted community"
print(message)

#bad formated message:
message = 'For programmer John O'Hara one of the advantages of Python is it versatility and devoted community'
print(message)
# Output:
"""
File ~/IDE/Python/Python-Refreshing/08_apostrophe.py:7
    message = 'For programmer John O'Hara one of the advantages of Python is it versatility and devoted community'
                                                                                                                 ^
SyntaxError: unterminated string literal (detected at line 7)
"""