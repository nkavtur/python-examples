sample_text = '''
    The textwrap module can be used to format text for output in
    situations where pretty-printing is desired.  It offers
    programmatic functionality similar to the paragraph wrapping
    or filling features found in many text editors.
    '''

import textwrap

shifted_text = textwrap.fill(sample_text, width=50)
print(shifted_text, end='\n\n')

dedented_text = textwrap.dedent(sample_text)
print(dedented_text, end='\n\n')

dedented_text = textwrap.dedent(sample_text).strip()
for width in [45, 60]:
    print(f'{width} Columns:\n')
    print(textwrap.fill(dedented_text, width=width))
    print()

import textwrap

dedented_text = textwrap.dedent(sample_text)
wrapped = textwrap.fill(dedented_text, width=50)
wrapped += '\n\nSecond paragraph after a blank line.'
final = textwrap.indent(wrapped, '> ')

print(final, end='\n\n')


def should_indent(line):
    return len(line.strip()) % 2 == 0


dedented_text = textwrap.dedent(sample_text)
wrapped = textwrap.fill(dedented_text, width=50)
final = textwrap.indent(wrapped, 'EVEN ',
                        predicate=should_indent)

print(final, end='\n\n')



dedented_text = textwrap.dedent(sample_text).strip()
print(textwrap.fill(dedented_text,
                    initial_indent='',
                    subsequent_indent=' ' * 4,
                    width=50,
                    ), end='\n\n')


dedented_text = textwrap.dedent(sample_text)
original = textwrap.fill(dedented_text, width=50)
print(original, end='\n\n')

shortened = textwrap.shorten(original, 100)
shortened_wrapped = textwrap.fill(shortened, width=50)
print(shortened_wrapped, end='\n')
