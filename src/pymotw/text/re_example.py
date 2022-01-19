import re

# search

pattern = 'this'
text = 'Does this text match the pattern this?'

match = re.search(pattern, text)
start, end = match.start(), match.end()

print(f"Found '{match.re.pattern}'\nin '{match.string}'\nfrom {start} to {end} ('{text[start:end]}')")
print()
print()

# Precompile the patterns
regexes = [
    re.compile(p)
    for p in ['this', 'that']
]

text = 'Does this text match the pattern?'

print(f"Text: {text}\n")

for regex in regexes:
    print(f"Seeking '{regex.pattern}' ->' ", end=' ')
    if regex.search(text):
        print('match!')
    else:
        print('no match')

print()
print()

# multiple matches

text = 'abbaaabbbbaaaaa'
pattern = 'ab'

for match in re.findall(pattern, text):
    print(f"Found {match}")

print()
print()

text = 'abbaaabbbbaaaaa'
pattern = 'ab'

for match in re.finditer(pattern, text):
    s = match.start()
    e = match.end()
    print(f"Found {text[s:e]} at {s}:{e}")

print()
print()

# verbose expression + named patterns
address = re.compile(
    r'''
    (?P<username>[\w\d.+-]+)       # username
    @
    (?P<domain>[\w\d.]+)+\.    # domain name prefix
    (com|org|edu)
    ''',
    re.VERBOSE)

candidates = [
    u'first.last@example.com',
    u'first.last+category@gmail.com',
    u'valid-address@mail.example.com',
    u'not-valid@example.foo',
]

for candidate in candidates:
    match = address.search(candidate)
    if match:
        print(f"{candidate} Matches. Groups: {match.groupdict()}")
    else:
        print(f"{candidate} No match")

print()
print()

# substitute
bold = re.compile(r'\*{2}(.*?)\*{2}')
text = 'Make this **bold**.  This **too**.'
print('Text:', text)
print('Bold:', bold.sub(r'<b>\1</b>', text))
print()

# substitute by patters
bold = re.compile(r'\*{2}(?P<bold>.*?)\*{2}')
text = 'Make this **bold**.  This **too**.'
print('Text:', text)
print('Bold:', bold.sub(r'<b>\g<bold></b>', text))

print()
print()

beacon_id = 'ac8724db-4303-4670-ab01-6f0f5815fa29.42.802'

beacon_id_pattern = re.compile(
    r'''
    (?P<uuid>[0-9a-f]{8}\b-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-\b[0-9a-f]{12}) # UUID
    \.
    (?P<major>\d+)   # Major
    \.
    (?P<minor>\d+)   # Minor
    ''',
    re.VERBOSE)

match = beacon_id_pattern.search(beacon_id)
print(match.groupdict())
