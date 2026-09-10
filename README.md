# Exercícios de Programação Orientada a Objetos com Python

Estudos práticos de POO em Python, organizados por projeto. Cada pasta explora um conjunto de conceitos aplicados a um domínio concreto, em vez de exemplos isolados.

## Projetos

### Sabor Express — Cadastro de Restaurantes

Sistema de cadastro e avaliação de restaurantes, usado para exercitar os pilares da orientação a objetos.

**Modelagem:** duas classes com relação de composição — um `Restaurante` possui uma coleção de `Avaliacao`.

```
SaborExpress - POO/RestaurantesPY/
├── app.py            # Ponto de entrada: instancia e exercita as classes
├── restaurante.py    # Classe Restaurante
└── avaliacao.py      # Classe Avaliacao
```

**Conceitos aplicados:**

| Conceito | Implementação |
| --- | --- |
| Atributo de classe | `Restaurante.restaurantes` mantém o registro de todas as instâncias criadas |
| Encapsulamento | `_ativo` e `_avaliacao` sinalizados como internos por convenção |
| `@property` | `media_avaliacoes` e `checar` são acessados como atributo, mas calculados em tempo de leitura |
| `@classmethod` | `listar_restaurantes()` opera sobre a coleção da classe, não sobre uma instância |
| Método mágico `__str__` | Define a representação legível do objeto |
| Composição | Cada avaliação recebida é um objeto `Avaliacao` dentro do restaurante |
| Normalização no construtor | `nome.title()` garante formato consistente na entrada |

A média de avaliações é uma propriedade calculada em vez de um campo armazenado — decisão que evita o risco de o valor ficar defasado quando uma nova avaliação entra. O caso de lista vazia é tratado explicitamente para não gerar divisão por zero.

## Como executar

```bash
git clone https://github.com/DanielC307/Exercicios-de-POO-com-PY.git
cd "Exercicios-de-POO-com-PY/SaborExpress - POO/RestaurantesPY"
pip install rich
python app.py
```

## Tecnologias

- Python 3
- [rich](https://rich.readthedocs.io/) — saída formatada no terminal e inspeção de objetos

## Próximos passos

- [ ] Validar a nota das avaliações na faixa de 1 a 10 dentro do construtor de `Avaliacao`
- [ ] Adicionar `@property` com setter para `nome`, controlando a alteração após a criação
- [ ] Exercitar herança criando especializações de `Restaurante` (delivery, self-service)
- [ ] Implementar `__repr__` e comparação entre objetos com `__eq__`
- [ ] Persistir os restaurantes cadastrados em arquivo
- [ ] Cobrir as classes com testes usando `pytest`
