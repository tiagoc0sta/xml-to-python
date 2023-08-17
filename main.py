import xmltodict

# abrir e ler o arquivo

def ler_xml_danfe(nota):
    with open(nota, 'rb') as arquivo:
        documento = xmltodict.parse(arquivo)
    # print(documento)
    dic_notafiscal = documento['nfeProc']['NFe']['infNFe']

    valor_total = dic_notafiscal['total']['ICMSTot']['vNF']
    cnpj_vendeu = dic_notafiscal['emit']['CNPJ']
    nome_vendeu = dic_notafiscal['emit']['xNome']
    cpf_comprou = dic_notafiscal['dest']['CPF']
    nome_comprou = dic_notafiscal['dest']['xNome']
    produtos = dic_notafiscal['det']
    lista_produtos = []
    for produto in produtos:
        valor_produto = produto['prod']['vProd']
        nome_produto = produto['prod']['xProd']
        lista_produtos.append((nome_produto, valor_produto))
    resposta = {
        'valor_total': [valor_total],
        'cnpj_vendeu': [cnpj_vendeu],
        'nome_vendeu': [nome_vendeu],
        'cpf_comprou': [cpf_comprou],
        'nome_comprou': [nome_comprou],
        'lista_produtos': [lista_produtos],
    }

    return resposta

