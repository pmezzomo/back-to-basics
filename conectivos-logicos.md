# Conectivos lógicos

## Lógica Booleana

A Lógica Booleana foi desenvolvida pelo matemático George Boole e é um dos pilares fundamentais da computação e da programação. Ela se fundamenta no conceito de proposição, que é qualquer afirmação que pode ser classificada como **verdadeira** ou **falsa**.

Em computação, isso significa que tudo pode ser reduzido a dois estados:

- **1** = Verdadeiro
- **0** = Falso

A lógica booleana é usada para tomar decisões dentro dos códigos. Por exemplo:

- *Um usuário pode acessar o sistema?* Sim ou não
- *Esse número é par?* Sim ou não
- *O pagamento foi aprovado?* Sim ou não

A forma como combinamos proposições é o que nos permite criar condições mais complexas para guiar o fluxo dos programas.

---

## O que é uma proposição? 🤔

Uma proposição é uma sentença declarativa que pode ser classificada como verdadeira ou falsa.

Mas lembre-se: para ser considerada uma proposição, a sentença não pode ser ambígua!

Os dois principais tipos são:

### ⤿ Proposições simples

É uma única afirmação que pode ser verdadeira ou falsa.

Ex: Hoje é segunda-feira.

### ⤿ Proposição composta

É formada por duas ou mais proposições simples, conectadas por operadores lógicos.

Ex: Hoje é segunda-feira e está chovendo.

Nesse exemplo temos duas proposições e podemos representar cada uma com uma letra:

- P: *"Hoje é segunda-feira"*
- Q: *"Está chovendo"*

---

## Conectivos lógicos e seus símbolos

Para combinar proposições, usamos operadores lógicos, que seguem regras bem definidas.

Os principais conectivos lógicos são:

### ⤿ Conjunção E

Ex: Estou estudando e aprendendo lógica.

- P: "Estou estudando"
- Q: "Aprendendo lógica"

**Regra:** A conjunção entre duas proposições só será verdadeira se ambas forem verdadeiras.

| P | Q | P ∧ Q |
|---|---|-------|
| V | V | **V** |
| V | F | F |
| F | V | F |
| F | F | F |

---

### ⤿ Disjunção OU

Ex: Eu vou ao cinema ou eu vou à praia.

- P: "Vou ao cinema"
- Q: "Vou à praia"

**Regra:** A disjunção entre duas proposições será verdadeira se pelo menos uma delas for verdadeira.

| P | Q | P ∨ Q |
|---|---|-------|
| V | V | **V** |
| V | F | **V** |
| F | V | **V** |
| F | F | F |

---

### ⤿ Negação

Ex: Não está chovendo.

- P: "Não está chovendo."

**Regra:** A negação simplesmente inverte o valor lógico de uma proposição.

| P | ¬ P |
|---|-----|
| V | F |
| F | V |

---

### ⤿ Disjunção Exclusiva XOU

Ex: Ou vou de ônibus ou vou de bicicleta.

- P: "Vou de ônibus"
- Q: "Vou de bicicleta"

**Regra:** A frase completa será verdadeira somente se exatamente uma das partes for verdadeira.

| P | Q | P ⊕ Q |
|---|---|-------|
| V | V | F |
| V | F | **V** |
| F | V | **V** |
| F | F | F |

---

### ⤿ Consequência Lógica: Condicional

Ex: Se chover, então eu vou usar guarda-chuva.

- P: "Se chover"
- Q: "Vou usar guarda-chuva"

**Regra:** A proposição condicional afirma que, **se** a primeira parte for verdadeira, **então** a segunda parte também deve ser verdadeira.

| P | Q | P → Q |
|---|---|-------|
| V | V | **V** |
| V | F | F |
| F | V | **V** |
| F | F | **V** |

**Explicação:**
- Se P for verdadeira e Q for falsa, a condicional será falsa — esse é o único caso onde a condicional falha.
- Se P for verdadeira e Q for verdadeira, a condicional é verdadeira.
- Se P for falsa (independente de Q), a condicional é considerada verdadeira por definição.

---

### ⤿ Consequência Lógica: Bicondicional

Ex: Eu posso comprar a roupa se e somente se eu tiver dinheiro.

- P: "Comprar a roupa"
- Q: "Somente se eu tiver dinheiro"

**Regra:** A proposição é verdadeira somente quando P e Q têm o mesmo valor lógico.

| P | Q | P ↔ Q |
|---|---|-------|
| V | V | **V** |
| V | F | F |
| F | V | F |
| F | F | **V** |

**Explicação:**
- Se ambos são verdadeiros, a proposição é verdadeira.
- Se ambos são falsos, a proposição também é verdadeira.
- Se um é verdadeiro e o outro é falso, o bicondicional será falso.

---

Os conectivos são ferramentas poderosíssimas que nos permitem criar regras lógicas complexas e determinar o comportamento do sistema de forma mais precisa.

Entender como esses conectivos funcionam e como representar cada um deles corretamente, seja com tabelas verdade ou expressões lógicas, é um passo fundamental para qualquer dev.

Agora, com esses conceitos, você está mais preparado(a) para construir soluções eficientes, tomando decisões automáticas baseadas em condições específicas. 💜

---

> Feito com 💜 por Rocketseat
