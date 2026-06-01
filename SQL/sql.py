import sqlite3
import pandas as pd

# para tratar um banco de dados, é necessária criar um chave de conexão
conn = sqlite3.connect('web.db')

# df_data = pd.read_csv('SQL/bd_data.csv', index_col=0)
# df_data.index.name = 'index_name'
# df_data.to_sql('data', conn, index_label='index_name')


# é necessário criar um ponteiro entre o python e o sql
c = conn.cursor()
# CREATE cria a tabela
# c.execute('CREATE TABLE products(product_id, product_name, price)')
# conn.commit()

# DROP remove a tabela(dropa)
# c.execute('DROP TABLE data')
# c.execute('DROP TABLE products')

# c.execute('CREATE TABLE products([product_id] INTEGER PRIMARY KEY, [product_name] TEXT, [price] FLOAT)')


# INSERT, adiciona na tabela
# os dados são passados como tuplas, separados por ,
# tem que botar o commit para executar o insert into
# c.execute('''INSERT INTO products (product_id, product_name, price)
#         VALUES  
#           (1, 'Computer', 800),
#           (2, 'Printer', 200),
#           (3, 'Tablet', 300)          
# ''')
# conn.commit()
# não é recomendado utilizar insert into
# é melhor pegar pelo pandas

# df_data2 = df_data.floc[::-2]
# df_data2.to_sql('data', conn, if_exists='append')

# SELECT, é utilizado para leitura, sempre vem junto de um from, é necessário colocar o nome das colunas ou *(seleciona tudo)
c.execute('SELECT * FROM products')
c.fetchone()
c.fetchall()
df = pd.DataFrame(c.fetchall()) # não é uma boa prática
# possui o where, [](quando) do pandas

# query = 'SELECT * FROM data'
# df = pd.read_sql(query, con= conn, index_col='index_name')

# UPDATE e DELETE
c.execute('UPDATE products SET price =750 WHERE product_id=1')
conn.commit() # é utlizado para inserção

c.execute('DELETE FROM products WHERE product_id=1')