custom_string = 'X-MAPDS-Confidence:0.8475'
find_char = custom_string.find(':')
new_string = custom_string[find_char + 1:]
new_string = float(new_string)
print(new_string)