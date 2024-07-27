def all_variants(text):
    if len(text) == 0:
        yield ""
    else:
        for i in range(len(text)):
            for variant in all_variants(text[:i] + text[i+1:]):
                yield text[i] + variant


a = all_variants("abc")
for i in a:
    print(i)
