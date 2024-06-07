from pymemcache.client.base import Client

def set_cache(key, value):
    """
    Armazena um valor no cache do Memcached.

    :param key: A chave sob a qual armazenar o valor.
    :param value: O valor a ser armazenado.
    """
    # Substitua com o seu endpoint do ElastiCache
    endpoint = 'filmelier-cache.82izya.cfg.usw2.cache.amazonaws.com'
    port = 11211

    # Criando uma conexão com o cluster ElastiCache
    client = Client((endpoint, port))

    try:
        # Definindo um valor no cache
        client.set(key, value)
        print(f"Valor '{value}' armazenado com a chave '{key}'.")
    except Exception as e:
        print(f"Ocorreu um erro ao tentar definir o valor no cache: {e}")
    finally:
        # Sempre fechar a conexão
        client.close()

# Exemplo de uso
set_cache('minha_chave', 'meu_valor')
