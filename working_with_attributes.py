from president import President

p = President(29)
print(p.last_name)
print(p.party, "\n")

attribute_name = "birth_place"
print(getattr(p, attribute_name))

attribute_name = "birth_state"
print(getattr(p, attribute_name))
print("-" * 60)

for attribute_name in dir(p):
    if attribute_name.startswith('_'):
        continue
    attribute_value = getattr(p, attribute_name)
    print(attribute_name, attribute_value)

