# História de Usuário: Integração de Dados Multifonte

Título: Desenvolver um sistema de processamento de dados para integração de diversas fontes e destinos.

## Descrição:

Como usuário, desejo um sistema eficiente que possa coletar dados de várias origens, processá-los de acordo com regras específicas e enviá-los para diferentes destinos. O sistema deve ser baseado em conceitos de programação orientada a objetos, como abstração, interfaces, classes, polimorfismo e encapsulamento.

## Critérios de Aceitação:

### Processor Central:

- Deve existir uma classe principal chamada DataProcessor que atua como o processador central.
- DataProcessor deve ser abstrato, implementando interfaces para manipulação de dados.
- O processador central deve obter os dados, passar a responsabilidade de transformação para a classe filha e após a transformação a classe filha deve chamar a classe base para persistencia dos dados
- O processador central deve implementar registros de logs comuns a todos os processamentos com as seguintes informações, nome da rotina, data de inicio e fim do processamento, e tempo de execução.

### Origens e Destinos:

- Suportar origens e destinos de dados como MySQL, arquivos CSV e APIs.
- Cada origem e destino deve ser encapsulado em classes separadas, implementando interfaces específicas.
- A interface para as classes de origens deve ter o metodo obter_dados que deverá ser implementado pelas classes de cada origem
- A interface para as classes de destinos deve ter o metodo salvar_dados que deverá ser implementado pelas classes filhas

### Rotinas de Processamento:

- Cada classe filha de DataProcessor deve implementar suas próprias rotinas de processamento de dados.
- As rotinas devem incluir lógica para lidar com diferentes tipos de dados provenientes das diversas origens.
- As rotinas de processamento deve instanciar as classes de origens e destinos especificas e passar essas instancias para classe base (DataProcessor) saber como obter e salvar os dados.
### Encapsulamento:

- Utilizar encapsulamento para proteger os detalhes de implementação das classes de origem e destino.
- Garantir que a classe DataProcessor seja responsável apenas pela coordenação do fluxo de dados, sem expor detalhes internos.


### Estrutura

Organizar o código de forma eficiente é crucial para manter a clareza e a manutenibilidade em projetos Python. Existem várias maneiras de estruturar pastas e adotar convenções, mas aqui está uma sugestão com base em boas práticas:

```plaintext
|-- main.py
|-- origens/
|   |-- source_interface.py
|   |-- mysql_source.py
|   |-- csv_source.py
|   |-- api_source.py
|-- destinos/
|   |-- target_interface.py
|   |-- mysql_destination.py
|   |-- csv_destination.py
|   |-- api_destination.py
|-- processamento/
|   |-- data_processor.py
|   |-- rotinas/
|       |-- mysql_processing.py
|       |-- csv_processing.py
|       |-- api_processing.py
|-- requirements.txt
|-- README.md
```


### Convenções:

- Pacotes e Módulos: Utilize nomes de pacotes e módulos em minúsculas e evite caracteres especiais.

- Classes e Funções: Use CamelCase para nomes de classes e minúsculas_separadas_por_underscores para funções e métodos.

- Documentação: Inclua docstrings para documentar suas classes, métodos e funções.

- README: Forneça informações essenciais sobre o projeto, como instalação e execução, no arquivo README.md.

- Adapte essa estrutura conforme as necessidades específicas do seu projeto, mantendo sempre a coesão e a clareza do código.
