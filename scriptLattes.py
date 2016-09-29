#!/usr/bin/env python 
# encoding: utf-8
#
#
#  scriptLattes V8
#  Copyright 2005-2014: Jesús P. Mena-Chalco e Roberto M. Cesar-Jr.
#  http://scriptlattes.sourceforge.net/
#
#
#  Este programa é um software livre; você pode redistribui-lo e/ou 
#  modifica-lo dentro dos termos da Licença Pública Geral GNU como 
#  publicada pela Fundação do Software Livre (FSF); na versão 2 da 
#  Licença, ou (na sua opinião) qualquer versão.
#
#  Este programa é distribuído na esperança que possa ser util, 
#  mas SEM NENHUMA GARANTIA; sem uma garantia implicita de ADEQUAÇÂO a qualquer
#  MERCADO ou APLICAÇÃO EM PARTICULAR. Veja a
#  Licença Pública Geral GNU para maiores detalhes.
#
#  Você deve ter recebido uma cópia da Licença Pública Geral GNU
#  junto com este programa, se não, escreva para a Fundação do Software
#  Livre(FSF) Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
#

import sys
import shutil
import Levenshtein
import os, errno
import warnings
import requests, BeautifulSoup # required by QualisExtractor
warnings.filterwarnings('ignore')


from scriptLattes.producoesBibliograficas import *
from scriptLattes.producoesTecnicas import *
from scriptLattes.producoesArtisticas import *
from scriptLattes.producoesUnitarias import *
from scriptLattes.orientacoes import *
from scriptLattes.eventos import *
from scriptLattes.charts import *
from scriptLattes.internacionalizacao import *
from scriptLattes.qualis import *
from scriptLattes.patentesRegistros import *

from scriptLattes.grupo import *

from scriptLattes.util import *

if 'win' in sys.platform.lower():
    os.environ['PATH'] += ";" + os.path.abspath(os.curdir + '\\Graphviz2.36\\bin')
sys.stdout = OutputStream(sys.stdout, sys.stdout.encoding)
sys.stderr = OutputStream(sys.stderr, sys.stdout.encoding)

if __name__ == "__main__":
	arquivoConfiguracao = sys.argv[1]
	#os.chdir( os.path.abspath(os.path.join(arquivoConfiguracao, os.pardir)))
	novoGrupo = Grupo(arquivoConfiguracao)
	#novoGrupo.imprimirListaDeParametros()
	novoGrupo.imprimirListaDeRotulos()

	if criarDiretorio(novoGrupo.obterParametro('global-diretorio_de_saida')):
		novoGrupo.carregarDadosCVLattes() #obrigatorio
		novoGrupo.compilarListasDeItems() # obrigatorio
		novoGrupo.identificarQualisEmPublicacoes() # obrigatorio
		novoGrupo.calcularInternacionalizacao() # obrigatorio
		#novoGrupo.imprimirMatrizesDeFrequencia() 

		novoGrupo.gerarGrafosDeColaboracoes() # obrigatorio
		#novoGrupo.gerarGraficosDeBarras() # java charts
		novoGrupo.gerarMapaDeGeolocalizacao() # obrigatorio
		novoGrupo.gerarPaginasWeb() # obrigatorio
		novoGrupo.gerarArquivosTemporarios() # obrigatorio

		# copiar imagens e css
		copiarArquivos(novoGrupo.obterParametro('global-diretorio_de_saida'))

		# finalizando o processo
		#print '[AVISO] Quem vê \'Lattes\', não vê coração! B-)'
		#print '[AVISO] Por favor, cadastre-se na página: http://scriptlattes.sourceforge.net\n'
		print '\n\n\n[PARA REFERENCIAR/CITAR ESTE SOFTWARE USE]'
		print '    Jesus P. Mena-Chalco & Roberto M. Cesar-Jr.'
		print '    scriptLattes: An open-source knowledge extraction system from the Lattes Platform.'
		print '    Journal of the Brazilian Computer Society, vol.15, n.4, páginas 31-39, 2009.'
		print '    http://dx.doi.org/10.1007/BF03194511'
		print '\n\nscriptLattes executado!'

