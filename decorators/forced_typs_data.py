'''
Forçando tipos de dados com decoradores
'''


def forca_tipo(*tipos):
    def decorador(funcao):
        def coverte(*args, **kwargs):
            novo_args = []
            for (valor, tipo) in zip(args, tipos):
                novo_args.append(tipo(valor))
            return funcao(*novo_args, **kwargs)
        return coverte
    return decorador


@forca_tipo(str, int)
def repete_msg(msg, vezes):
    for _ in range(vezes):
        print(msg)


repete_msg('Olá', 3)
