import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

(?=.*[A-Z]) - Хотя бы одна заглавная буква.
(?=.*\d) - Хотя бы одна цифра.
(?=.*[@$!%*?&]) - Хотя бы один спецсимвол.
[A-Za-z\d@$!%*?&]{8,} - Минимальная длина 8 символов.

import re

text = "Сегодня отличный день! #sunny #happy #Python"
pattern = r"#\w+"

hashtags = re.findall(pattern, text)
print(hashtags)
