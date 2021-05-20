import pandas

_items_df = pandas.read_csv('items.csv')

# Use this graph_dict variable
graph_dict = dict()

COLUMNS = {'Nama', 'Harga', 'Kategori', 'Merk'}

for column in COLUMNS:
    for index, row in _items_df.iterrows():
        if column == 'Nama':
            graph_dict['Nama-' + row['Nama']] = {
                'Harga-' + row['Harga'],
                'Kategori-' + row['Kategori'],
                'Merk-' + row['Merk'],
            }
        elif column == 'Harga':
            graph_dict['Harga-' + row['Harga']] = {
                'Nama-' + row['Nama'],
            }
        elif column == 'Kategori':
            graph_dict['Kategori-' + row['Kategori']] = {
                'Nama-' + row['Nama'],
            }
        elif column == 'Merk':
            graph_dict['Merk-' + row['Merk']] = {
                'Nama-' + row['Nama'],
            }
