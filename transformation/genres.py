import json

genre_counts = []

for i in range(1959, 2017):
    year_count = {}
    with open('../spotify_data-' + str(i) + '.json', 'r') as infile:
        data = json.load(infile)
    for record in data:
        if record is None:
            continue
        
        for genre in record['genres']:
            if genre in year_count:
                year_count[genre] += 1
            else:
                year_count[genre] = 1
    print(year_count)
    genre_counts.append(year_count)

with open('../genre_counts.json', 'w') as outfile:
    json.dump(genre_counts, outfile)

