scriptLattes V7
-----------------

SINOPSIS
	scriptLattes <nome_arquivo_de_configuracao>

REQUISITOS
	Para a compilação precisam-se de alguns módulos Perl (a partir da versão 7 é
	requerido o módulo libjson-perl). 
	Para instalar esses módulos execute como root:

	# apt-get install libgd-graph-perl libgd-text-perl libgraphviz-perl libtimedate-perl libjson-perl

EXECUÇÃO
	Teste o scriptLattes com os seguintes exemplos de compilação na linha de comando:

	(i) Exemplo A:
	$ cd <nome_diretorio_scriptLattes>
	$ ./scriptLattes ./exemplo/vision-ime-usp-PARAMETROS-A.txt

	Nesse exemplo consideram-se todas as produções (todos os anos). O relatório, 
	em português, apresenta o mapa de pesquisa. Essa configuração de parâmetros
	é a mais completa. O resultado da compilação estará disponível em:
	./exemplo/vision-ime-usp-RESULTS-A

	(ii) Exemplo B:
	$ cd <nome_diretorio_scriptLattes>
	$ ./scriptLattes ./exemplo/vision-ime-usp-PARAMETROS-B.txt

	Nesse exemplo consideram-se todas as produções cujos anos de publicação
	estão entre 1970 e HOJE. O relatório, em inglês, não apresenta o mapa de pesquisa.
	O resultado da compilação estará disponível em:
	./exemplo/vision-ime-usp-RESULTS-B

	OBS: Veja o arquivo exemplo/vision-ime-usp-IDS.txt um exemplo
	de IDs Lattes usado como entrada para o scriptLattes.

DESENVOLVEDORES
	Jesús P. Mena-Chalco <jmena@vision.ime.usp.br>
	Roberto M. Cesar-Jr <cesar@vision.ime.usp.br>

URL DO PROJETO
	http://scriptlattes.sourceforge.net/

=========================================================================================
LOG

Mon Mar 15 08:02:22 BRT 2010
-- Melhoramento da função de comparação. Em média o algoritmo de comparação da
   versão 7.02 é 13X mais rápido que o anterior.
-- Criação do grafo de colaborações com indicadores de produção usando um mapa
   de cores (hotcolors).
-- Foram consideradas, mediante novos parâmetros, os seguintes relatórios adicionais:
   - Participação em bancas examinadoras.
   - Participação em comissões julgadoras.
   - Eventos.

Ter Out 20 13:32:13 BRST 2009
-- Geração de relatórios disponíveis para os idiomas: inglês, português e espanhol.
-- Criação de uma página de 'detalhe de colaborações'. Clique nas arestas do Grafo de colaborações
   para listar as publicações realizadas entre os membros.
-- Melhoramento da função de localização geográfica (com suporte para endereços do exterior).
   Utilize o arquivo 'scriptLattes.cep' para refinar a localização no googleMaps.
-- Criação de listas de produções em formato JSON: 'database.json'. Tais listas poderiam
   ser utilizadas para exportar as produções ou popular bancos de dados.
-- Melhoramento na visualização/apresentação/compilação dos relatórios.
   O scriptLattes não usa o script 'terminalTags.sh'.

Sáb Abr 18 16:23:31 BRT 2009
-- Foram considerados nas Produções técnicas os "Processos ou técnicas"
-- Foram considerados nas Orientações as "Monografias de conclusão de curso de aperfeiçoamento/especialização"
-- O procedimento para identificação do ano nas produções foi corrigido.
-- "Itens sem ano" estão sendo listados no final de cada relatório.

Ter Mar 24 07:59:43 BRT 2009
-- Mapa de pesquisa, considerando os alunos com doutorado concluído.
-- Foram corrigidos alguns pequenos erros de inicialização de variáveis.

Qua Mar  4 12:45:40 BRT 2009
-- Uso de um arquivo de configuração.
-- Delimitação de produções por períodos (global e local).
-- Mapa de pesquisa (usando o maps.google.com).
-- Produções técnicas e artísticas foram consideradas nos relatórios.
-- Criação de páginas para cada pesquisador.
-- Produção automática de páginas JSP (opcional)
-- Divisão automática de produções em páginas (ex. 1000 produções por página).
-- CSS para todas as páginas.
-- Refatoração do script.

Sáb Nov  8 16:11:46 BRST 2008
-- Versão interativa e postscript do grafo de colaborações.
-- Lista de pesquisadores considerados na execução.
-- Criação de um indice geral.

Seg Mar 24 12:30:03 BRT 2008
-- Refatoração.
-- Link para busca da publicação no Google.
-- Compilação de orientações (em andamento/concluídas).

Sex Fev  8 18:24:33 BRST 2008
-- Criadas as funções de compilação de todas as publicações.
-- Geração automática da página index.html.
-- Geração automática de um grafo de colaborações.

Ter Mar 13 12:04:40 BRT 2007 : 
-- Barras estatísticas das publicações (uso do GD::Graph do perl).
-- Criada a função de similaridade LCS (longest common sequence).
-- Modificada a função de extração de datas das publicações.

Seg Mar 20 17:50:21 BRT 2006 :
-- Atualização das funções básicas.

Sex Mar 25 13:04:27 BRT 2005 : 
-- Criada a função de similaridade básica.

=========================================================================================
