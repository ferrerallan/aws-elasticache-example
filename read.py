from pymemcache.client.base import Client

# Substitua com o seu endpoint do ElastiCache
endpoint = 'filmelier-cache.82izya.cfg.usw2.cache.amazonaws.com'
port = 11211

# Criando uma conexão com o cluster ElastiCache
client = Client((endpoint, port))

# Definindo um valor no cache
client.set('chave', 'valor')

# Obtendo o valor do cache
valor = client.get('chave')
print(f'O valor obtido é: {valor.decode("utf-8")}')

# Fechando a conexão
client.close()
