# Resumo do Capítulo 7: Tratamento de Erros (Michael Feathers)

## Uso de Exceções em vez de Retornar Códigos

Historicamente, a ausência de suporte a exceções nas linguagens de programação fazia com que erros fossem tratados por meio de flags ou códigos de erro. Isso dificultava a leitura e manutenção do código. Utilizar exceções melhora a clareza do código, separando a lógica principal do tratamento de erros.

## Crie Primeiro sua Estrutura try-catch-finally

Estruturas `try-catch-finally` ajudam a definir escopos claros para o tratamento de exceções. Inicie o código com essas estruturas para garantir que exceções sejam tratadas adequadamente, mantendo a consistência do estado do programa.

## Use Exceções Não Verificadas

Exceções verificadas podem quebrar o encapsulamento e levar a modificações indesejadas em diversos níveis do código. Embora sejam úteis em bibliotecas críticas, no desenvolvimento geral de aplicativos, as desvantagens superam as vantagens.

## Forneça Exceções com Contexto

Mensagens de erro devem ser informativas e detalhadas, mencionando a operação que falhou e o tipo de falha. Stack traces são úteis, mas muitas vezes insuficientes para entender o objetivo da operação que falhou.

## Defina as Classes de Exceções Segundo as Necessidades do Chamador

Classifique exceções com base em como serão capturadas. Utilize wrappers para APIs de terceiros, simplificando o tratamento de exceções e minimizando dependências.

## Defina o Fluxo Normal

Separar a lógica do negócio do tratamento de erros é essencial. Use o padrão do Caso Especial (Special Case Pattern) para evitar a necessidade de lidar com comportamentos excepcionais diretamente no código cliente.

## Não Retorne null

Retornar null leva a verificações excessivas e propensas a erros. Considere lançar exceções ou retornar objetos de Caso Especial em vez de null.

## Não Passe null

Passar null para métodos é ainda mais problemático do que retorná-lo. Proíba, por padrão, a passagem de null para evitar erros de execução.

## Conclusão

Um código limpo deve ser legível e robusto. Tratar o tratamento de erro como uma preocupação separada facilita a manutenção e a clareza do código.