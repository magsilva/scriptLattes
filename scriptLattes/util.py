#!/usr/bin/env python 
# encoding: utf-8
#
#
import logging

import os
import shutil
import sys

import Levenshtein


SEP = os.path.sep
BASE = 'scriptLattes' + SEP
ABSBASE = os.path.abspath('.') + SEP


class OutputStream:
    def __init__(self, output, encoding):
        self.encoding = encoding
        self.output = output

    def write(self, text):
        try:
            text = text.decode(self.encoding)
        except:
            try:
                text = text.decode('utf8').encode('iso-8859-1')
            except:
                try:
                    text = text.encode('iso-8859-1')
                except:
                    pass
        try:
            self.output.write(text)
        except:
            try:
                self.output.write(unicode(text))
            except:
                self.output.write('ERRO na impressao')


def buscarArquivo(filepath, arquivoConfiguracao=None):
    if not arquivoConfiguracao:
        arquivoConfiguracao = sys.argv[1]
    curdir = os.path.abspath(os.path.curdir)
    if not os.path.isfile(filepath) and arquivoConfiguracao:
        # vamos tentar mudar o diretorio pro atual do arquivo
        os.chdir(os.path.abspath(os.path.join(arquivoConfiguracao, os.pardir)))
    if not os.path.isfile(filepath):
        # se ainda nao existe, tentemos ver se o arquivo não está junto com o config
        filepath = os.path.abspath(os.path.basename(filepath))
    else:
        # se encontramos, definimos então caminho absoluto
        filepath = os.path.abspath(filepath)
    os.chdir(curdir)
    return filepath


def copiarArquivos(dir):
    base = ABSBASE

    try:
        dst = os.path.join(dir, 'css')
        if os.path.exists(dst):
            shutil.rmtree(dst)
        shutil.copytree(os.path.join(base, 'css'), dst)
    except OSError, e:
        pass  # provavelmente diretório já existe
        logging.warning(e)

    # shutil.copy2(os.path.join(base, 'css', 'scriptLattes.css'), dir)
    # shutil.copy2(os.path.join(base, 'css', 'jquery.dataTables.css'), dir)

    shutil.copy2(os.path.join(base, 'images', 'lattesPoint0.png'), dir)
    shutil.copy2(os.path.join(base, 'images', 'lattesPoint1.png'), dir)
    shutil.copy2(os.path.join(base, 'images', 'lattesPoint2.png'), dir)
    shutil.copy2(os.path.join(base, 'images', 'lattesPoint3.png'), dir)
    shutil.copy2(os.path.join(base, 'images', 'lattesPoint_shadow.png'), dir)
    shutil.copy2(os.path.join(base, 'images', 'doi.png'), dir)

    try:
        dst = os.path.join(dir, 'images')
        if os.path.exists(dst):
            shutil.rmtree(dst)
        shutil.copytree(os.path.join(base, 'images'), dst)
    except OSError, e:
        pass  # provavelmente diretório já existe
        logging.warning(e)

    try:
        dst = os.path.join(dir, 'js')
        if os.path.exists(dst):
            shutil.rmtree(dst)
        shutil.copytree(os.path.join(base, 'js'), dst)
    except OSError, e:
        pass  # provavelmente diretório já existe
        logging.warning(e)

    # shutil.copy2(os.path.join(base, 'js', 'jquery.min.js'), dir)
    # shutil.copy2(os.path.join(base, 'js', 'highcharts.js'), dir)
    # shutil.copy2(os.path.join(base, 'js', 'exporting.js'), dir)
    # shutil.copy2(os.path.join(base, 'js', 'drilldown.js'), dir)
    # shutil.copy2(os.path.join(base, 'js', 'jquery.dataTables.min.js'), dir)
    # shutil.copy2(os.path.join(base, 'js', 'jquery.dataTables.rowGrouping.js'), dir)

    print "Arquivos salvos em: >>'%s'<<" % os.path.abspath(dir)

# ---------------------------------------------------------------------------- #
def compararCadeias(str1, str2, qualis=False):
    str1 = str1.strip().lower()
    str2 = str2.strip().lower()

    if len(str1) == 0 or len(str2) == 0:
        return 0

    if len(str1) >= 20 and len(str2) >= 20 and (str1 in str2 or str2 in str1):
        return 1

    if qualis:
        dist = Levenshtein.ratio(str1, str2)
        if len(str1) >= 10 and len(str2) >= 10 and dist >= 0.80:
            # return 1
            return dist

    else:
        if len(str1) >= 10 and len(str2) >= 10 and Levenshtein.distance(str1, str2) <= 5:
            return 1
    return 0


def criarDiretorio(dir):
    if not os.path.exists(dir):
        try:
            os.makedirs(dir)
        ### except OSError as exc:
        except:
            print "\n[ERRO] Não foi possível criar ou atualizar o diretório: " + dir.encode('utf8')
            print "[ERRO] Você conta com as permissões de escrita? \n"
            return 0
    return 1
