import pandas as pd

# There's only so many unique prev, curr, type's so add them as you go, working with 1 file at a time

pairs = {}

for i in range(1, 7):
    print(i)
    df = pd.read_csv(f'inputs/clickstream-enwiki-2020-0{i}.tsv', delimiter='\t',
                     names=['prev', 'curr','type', 'n'],
                     on_bad_lines='warn')
    for row in df.itertuples():
        unique_identifier = (row.prev, row.curr, row.type)
        try:
            n = int(row.n)
            if unique_identifier in pairs:
                pairs[unique_identifier] += n
            else:
                pairs[unique_identifier] = n
        except:
            print('failed ' + str(row))

del df
top_50 = sorted(pairs, key=pairs.get, reverse=True)[:50]

top_pairs = {}

for top in top_50:
    top_pairs[top] = pairs[top]

del pairs

for k, v in top_pairs.items():
    print(v, k)

"""
number references (referrer, reference, type)

1676517827 ('other-empty', 'Main_Page', 'external')
332857347 ('other-empty', 'United_States_Senate', 'external')
146381512 ('other-empty', 'Hyphen-minus', 'external')
68803652 ('other-internal', 'Main_Page', 'external')
58805642 ('other-external', 'Hyphen-minus', 'external')
23671769 ('other-search', 'Kobe_Bryant', 'external')
18858094 ('other-search', 'Coronavirus', 'external')
18074986 ('other-empty', 'Bible', 'external')
18042314 ('Main_Page', 'Hyphen-minus', 'other')
17014291 ('other-empty', 'Wikipedia', 'external')
13398022 ('other-search', 'Spanish_flu', 'external')
12051456 ('other-empty', 'Tasuku_Honjo', 'external')
11474182 ('other-search', 'Sushant_Singh_Rajput', 'external')
11470270 ('other-search', 'Michael_Jordan', 'external')
11269497 ('other-search', 'Parasite_(2019_film)', 'external')
10828137 ('other-empty', 'Media', 'external')
10653762 ('other-search', '2019–20_coronavirus_pandemic', 'external')
10520030 ('other-search', 'Main_Page', 'external')
10485024 ('other-empty', 'COVID-19_pandemic', 'external')
10403099 ('other-search', 'Donald_Trump', 'external')
9985625 ('other-empty', '2019–20_coronavirus_pandemic', 'external')
9378333 ('other-search', 'Elon_Musk', 'external')
9051302 ('other-empty', 'Coronavirus', 'external')
7963411 ('other-empty', 'Deaths_in_2020', 'external')
7824547 ('other-search', 'Aaron_Hernandez', 'external')
7751329 ('Main_Page', 'Deaths_in_2020', 'link')
7748189 ('other-search', 'Joe_Exotic', 'external')
7718366 ('other-empty', 'F5_Networks', 'external')
7487168 ('other-empty', 'Microsoft_Office', 'external')
7388907 ('other-search', 'COVID-19_pandemic', 'external')
7331467 ('other-search', 'Coronavirus_disease_2019', 'external')
6603080 ('other-search', 'Money_Heist', 'external')
6469835 ('other-empty', "Kepler's_Supernova", 'external')
6429416 ('other-search', 'XXXX', 'external')
6367780 ('other-search', 'Antifa_(United_States)', 'external')
6335661 ('other-search', 'Billie_Eilish', 'external')
6289776 ('other-search', 'Irrfan_Khan', 'external')
5838871 ('other-search', 'Kim_Jong-un', 'external')
5636688 ('other-search', 'COVID-19_pandemic_in_India', 'external')
5579711 ('other-search', 'Killing_of_George_Floyd', 'external')
5566640 ('other-search', 'Jeffrey_Epstein', 'external')
5524653 ('other-internal', 'Hyphen-minus', 'external')
5510389 ('other-search', '2020_coronavirus_pandemic_in_India', 'external')
5268542 ('other-search', 'List_of_Marvel_Cinematic_Universe_films', 'external')
5152448 ('other-search', 'Waco_siege', 'external')
5035415 ('other-search', '1917_(2019_film)', 'external')
5027304 ('other-search', '2020_Democratic_Party_presidential_primaries', 'external')
4964577 ('other-search', 'Ken_Miles', 'external')
4882588 ('other-empty', 'Art', 'external')
4805025 ('other-empty', 'Brooklyn', 'external')
"""