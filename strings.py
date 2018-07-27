strings = ['This', 'list', 'is', 'now', 'all', 'together']
sentence = ''

sentence = strings[0]
for i in range(1, len(strings)):
    sentence = sentence + ' ' + strings[i]

print(sentence)
print(' '.join(strings))
