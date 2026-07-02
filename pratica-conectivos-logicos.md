# Prática - Conectivos Lógicos

Faaaaaala, dev! Agora que você já estudou os conectivos lógicos e entendeu como funciona a tabela verdade, é hora de colocar a mão na massa!

Esses exercícios vão te ajudar a fixar o raciocínio lógico e entender como a lógica formal se aplica na programação. Bora lá? 🚀

Leia atentamente cada uma das frases abaixo e represente logicamente utilizando os conectivos apropriados. Em seguida, monte a tabela verdade correspondente, analisando todas as possíveis combinações de verdadeiro (V) e falso (F) para as proposições.

---

> **Regras dos conectivos:**
> - **E (∧)** é verdadeiro apenas se ambas as proposições forem verdadeiras
> - **OU (∨)** é verdadeiro se pelo menos uma das proposições for verdadeira
> - **SE ENTÃO (→)** é falso apenas quando a primeira proposição é verdadeira e a segunda é falsa
> - **SE E SOMENTE SE (↔)** é verdadeiro quando ambas as proposições possuem o mesmo valor

---

## 1. Eu estudei para a prova e fiz todos os exercícios.

- P: "Eu estudei para a prova"
- Q: "Fiz todos os exercícios"
- Conectivo: **E (∧)**

| P | Q | P ∧ Q |
|---|---|-------|
| V | V | **V** |
| V | F | **F** |
| F | V | **F** |
| F | F | **F** |

---

## 2. Eu vou ao cinema ou fico em casa assistindo séries.

- P: "Vou ao cinema"
- Q: "Fico em casa assistindo séries"
- Conectivo: **OU (∨)**

| P | Q | P ∨ Q |
|---|---|-------|
| V | V | **V** |
| V | F | **V** |
| F | V | **V** |
| F | F | **F** |

---

## 3. Se eu acordar cedo, então conseguirei pegar o ônibus.

- P: "Eu acordar cedo"
- Q: "Conseguirei pegar o ônibus"
- Conectivo: **SE ENTÃO (→)**

| P | Q | P → Q |
|---|---|-------|
| V | V | **V** |
| V | F | **F** |
| F | V | **V** |
| F | F | **V** |

---

## 4. Se eu estudar muito, então passarei na prova e ganharei um presente.

- P: "Eu estudar muito"
- Q: "Passarei na prova"
- R: "Ganharei um presente"
- Conectivo: **SE ENTÃO + E → P → (Q ∧ R)**

| P | Q | R | Q ∧ R | P → (Q ∧ R) |
|---|---|---|-------|-------------|
| V | V | V | **V** | **V** |
| V | V | F | **F** | **F** |
| V | F | V | **F** | **F** |
| V | F | F | **F** | **F** |
| F | V | V | **V** | **V** |
| F | V | F | **F** | **V** |
| F | F | V | **F** | **V** |
| F | F | F | **F** | **V** |

---

## 5. Eu vou jogar videogame ou vou estudar lógica de programação.

- P: "Vou jogar videogame"
- Q: "Vou estudar lógica de programação"
- Conectivo: **OU (∨)**

| P | Q | P ∨ Q |
|---|---|-------|
| V | V | **V** |
| V | F | **V** |
| F | V | **V** |
| F | F | **F** |

---

## 6. Eu comi pizza e tomei refrigerante.

- P: "Comi pizza"
- Q: "Tomei refrigerante"
- Conectivo: **E (∧)**

| P | Q | P ∧ Q |
|---|---|-------|
| V | V | **V** |
| V | F | **F** |
| F | V | **F** |
| F | F | **F** |

---

## 7. Se eu tiver dinheiro, então viajarei nas férias.

- P: "Tiver dinheiro"
- Q: "Viajarei nas férias"
- Conectivo: **SE ENTÃO (→)**

| P | Q | P → Q |
|---|---|-------|
| V | V | **V** |
| V | F | **F** |
| F | V | **V** |
| F | F | **V** |

---

## 8. Eu lerei um livro se e somente se terminar meu trabalho.

- P: "Lerei um livro"
- Q: "Terminar meu trabalho"
- Conectivo: **SE E SOMENTE SE (↔)**

| P | Q | P ↔ Q |
|---|---|-------|
| V | V | **V** |
| V | F | **F** |
| F | V | **F** |
| F | F | **V** |

---

## 9. Se estiver sol, então irei à praia ou ao parque.

- P: "Estiver sol"
- Q: "Irei à praia"
- R: "Irei ao parque"
- Conectivo: **SE ENTÃO + OU → P → (Q ∨ R)**

| P | Q | R | Q ∨ R | P → (Q ∨ R) |
|---|---|---|-------|-------------|
| V | V | V | **V** | **V** |
| V | V | F | **V** | **V** |
| V | F | V | **V** | **V** |
| V | F | F | **F** | **F** |
| F | V | V | **V** | **V** |
| F | V | F | **V** | **V** |
| F | F | V | **V** | **V** |
| F | F | F | **F** | **V** |

---

## 10. Eu farei um bolo se e somente se comprar os ingredientes.

- P: "Farei um bolo"
- Q: "Comprar os ingredientes"
- Conectivo: **SE E SOMENTE SE (↔)**

| P | Q | P ↔ Q |
|---|---|-------|
| V | V | **V** |
| V | F | **F** |
| F | V | **F** |
| F | F | **V** |

---

> Feito com 💜 por Rocketseat
