from Models.Word import Word


def read_csv():
    file = open('src/504.csv')
    values = list()
    x = 0
    for line in file.readlines():
        if x == 0:
            x += 1
            continue

        value = tuple(line.strip().split('|'))[:13]

        lessons = range(1, 43)
        try:
            lesson = int(value[0])
        except:
            lesson = False

        if lesson not in lessons:
            continue

        values.append(value)
        x += 1

    return values


attributes = ("lesson", "title", "trans", "definition", "definition_trans", "first_example", "first_example_trans",
              "second_example", "second_example_trans", "third_example", "third_example_trans", "story_title",
              "story_title_trans")

word = Word()
word.create(attributes, read_csv())
print('504 record added')
