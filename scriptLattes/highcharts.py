#!/usr/bin/python
# -*- coding: utf-8 -*-
# filename: highcharts.py
#
#  scriptLattes V8
#  Copyright 2005-2013: Cristhian W. Bilhalva
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


class jscmd(object):
    cmd = ''
    def __init__(self,cmd):
        self.cmd = cmd
    def __str__(self):
        return self.cmd

class jsbool(object):
    value = False
    def __init__(self,v):
        if v:
            self.value = True
        else:
            self.value = False
    def __str__(self):
        return 'true' if self.value else 'false'

class bgcolor(object):
    colorstr = '(Highcharts.theme && Highcharts.theme.legendBackgroundColor || \'#FFFFFF\')'
    def __str__(self):
        return self.colorstr

true = jsbool(True)
false = jsbool(False)


def format_json(d):
    s = u''
    if isinstance(d,dict) or isinstance(d,list):
        s += '{' if isinstance(d,dict) else '['
        keys = d.keys()
        for k in keys:
            s += (',' if k != keys[0] else '') + str(k) + ': '
            if isinstance(d[k],dict):
                s += format_json(d[k])
            elif isinstance(d[k],str) or isinstance(d[k],unicode):
                s += '\''+d[k]+'\''
            else:
                s += str(d[k])
                
        s += '}' if isinstance(d,dict) else ']'
        
    return s       

class charttype(object):
    line = 'line'
    spline = 'spline'
    area = 'area'
    areaspline = 'areaspline'
    column = 'column'
    bar = 'bar'
    pie = 'pie'
    scatter = 'scatter'
    gauge = 'gauge'
    arearange = 'arearange'
    areasplinerange = 'areasplinerange'
    columnrange = 'columnrange'    

  
jsondata = {
            'chart': {
                'type': charttype.bar
            },
            'title': {
                'text': ''
            },
            'subtitle': {
                'text': ''
            },
            'xAxis': {
                'categories': [''],
                'title': {
                    'text': ''
                }
            },
            'yAxis': {
                'min': 0,
                'title': {
                    'text': '',
                    'align': 'high'
                },
                'labels': {
                    'overflow': 'justify'
                }
            },
            'tooltip': {
                'enabled': false,
                'valueSuffix': ''
            },
            'plotOptions': {
                'bar': {
                    'dataLabels': {
                        'enabled': true
                    }
                }
            },
            'legend': {
                'layout': 'vertical',
                'align': 'right',
                'verticalAlign': 'top',
                'x': -40,
                'y': 100,
                'floating': true,
                'borderWidth': 1,
                'backgroundColor': bgcolor(),
                'shadow': true
            },
            'credits': {
                'enabled': false
            },
            'series': []
        }

class highchart(dict):
    
    htmldata = u"""
		<script type="text/javascript" src="./js/jquery.min.js"></script>
		<script type="text/javascript" src="./js/highcharts.js"></script>
		<script type="text/javascript" src="./js/modules/exporting.js"></script>
		<script type="text/javascript">
		$(function () {
		    $('#container').highcharts(@jsondata@);
		});
        </script>
        """
    
    html = htmldata
    
    def __init__(self):
        dict.__init__(self,jsondata)
    
    def settitle(self,title):
        self['title']['text'] = title
    
    def setXtitle(self,title):
        self['xAxis']['title']['text'] = title
    
    def setYtitle(self,title):
        self['yAxis']['title']['text'] = title
    
    def setcharttype(self,chartt):
        self['chart']['type'] = chartt
    
    def listaCompleta(self,lista):
        keys = lista.keys()
        keys.sort()
        series = []
        for k in keys:
            qtd = len(lista[k])
            if qtd>0:
                s = {'name':k,'data':[qtd]}
                series.append(s)
        self['series'] = series
        
    def html(self):
        return self.htmldata.replace('@jsondata@',format_json(self))
    
    def json(self):
        return format_json(self)
    
