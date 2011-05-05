#!/usr/bin/python
# encoding: utf-8
# filename: mapaDeGeolocalizacao.py

from membro import *

class MapaDeGeolocalizacao:
	mapa = None

	def __init__(self, grupo):
		self.grupo = grupo

		print "\n[CRIANDO MAPA DE GEOLOCALIZAÇÃO] (Esta operação pode demorar)"
		self.gerarMapa()


	def gerarMapa(self):
		self.mapa = '<script src="http://maps.google.com/maps?file=api&amp;v=2.x&amp;sensor=false&amp;key='+self.grupo.obterParametro('mapa-google_map_key')+'" type="text/javascript"></script> \n'
		self.mapa+= '<script type="text/javascript"> \n\
        function initialize() { \n\
          if (GBrowserIsCompatible()) { \n\
             var map = new GMap2(document.getElementById("map_canvas")); \n\
             map.setCenter(new GLatLng(0,0), 2); \n\
             map.setUIToDefault(); \n\
             \n\
             var baseIcon0 = new GIcon(G_DEFAULT_ICON);  \n\
             baseIcon0.image = "lattesPoint0.png"; \n\
             markerOptions0 = { icon:baseIcon0 }; \n\
             \n\
             var tinyIcon1 = new GIcon(); \n\
             tinyIcon1.image = "lattesPoint1.png"; \n\
             tinyIcon1.shadow = "lattesPoint_shadow.png"; \n\
             tinyIcon1.iconSize = new GSize(12, 20); \n\
             tinyIcon1.shadowSize = new GSize(22, 20); \n\
             tinyIcon1.iconAnchor = new GPoint(6, 20); \n\
             tinyIcon1.infoWindowAnchor = new GPoint(5, 1); \n\
             markerOptions1 = { icon:tinyIcon1 }; \n\
             \n\
             var tinyIcon2 = new GIcon(); \n\
             tinyIcon2.image = "lattesPoint2.png"; \n\
             tinyIcon2.shadow = "lattesPoint_shadow.png"; \n\
             tinyIcon2.iconSize = new GSize(12, 20); \n\
             tinyIcon2.shadowSize = new GSize(22, 20); \n\
             tinyIcon2.iconAnchor = new GPoint(6, 20); \n\
             tinyIcon2.infoWindowAnchor = new GPoint(5, 1); \n\
             markerOptions2 = { icon:tinyIcon2 }; \n\
             \n\
             var tinyIcon3 = new GIcon(); \n\
             tinyIcon3.image = "lattesPoint3.png"; \n\
             tinyIcon3.shadow = "lattesPoint_shadow.png"; \n\
             tinyIcon3.iconSize = new GSize(12, 20); \n\
             tinyIcon3.shadowSize = new GSize(22, 20); \n\
             tinyIcon3.iconAnchor = new GPoint(6, 20); \n\
             tinyIcon3.infoWindowAnchor = new GPoint(5, 1); \n\
             markerOptions3 = { icon:tinyIcon3 }; \n\
             \n\
             function createMarker0(point, name, address, cvlattes, photo) { \n\
                var marker = new GMarker(point, markerOptions0); \n\
                GEvent.addListener(marker, "click", function() { \n\
                marker.openInfoWindowHtml(" <table> <tr bgcolor=#006400><td><font color=#ffffff><b>scriptLattes</b>: "+name+"</font></td></tr> <tr><td> <table><tr><td valign=top> <img src="+photo+" width=100px> </td><td> <font size=-2>"+address+"<br><p><a href="+cvlattes+" target=_blank>"+cvlattes+"</a></font></td></tr> </table>  </td></tr> </table>"); \n\
                }); \n\
               return marker; \n\
             }; \n\
             \n\
             function createMarker1(point, name, address, advisors, cvlattes, photo) { \n\
                var marker = new GMarker(point, markerOptions1); \n\
                GEvent.addListener(marker, "click", function() { \n\
                marker.openInfoWindowHtml(" <table> <tr bgcolor=#990808><td><font color=#ffffff><b>scriptLattes</b>: "+name+"</font></td></tr> <tr><td> <table><tr><td valign=top> <img src="+photo+" width=100px> </td><td> <font size=-2>"+address+"<br><b>"+advisors+"</b> <br><p><a href="+cvlattes+" target=_blank>"+cvlattes+"</a></font></td></tr> </table>  </td></tr> </table>"); \n\
                });\n\
                return marker; \n\
             };\n\
             function createMarker2(point, name, address, advisors, cvlattes, photo) { \n\
                var marker = new GMarker(point, markerOptions2); \n\
                GEvent.addListener(marker, "click", function() { \n\
                marker.openInfoWindowHtml(" <table> <tr bgcolor=#333399><td><font color=#ffffff><b>scriptLattes</b>: "+name+"</font></td></tr> <tr><td> <table><tr><td valign=top> <img src="+photo+" width=100px> </td><td> <font size=-2>"+address+"<br><b>"+advisors+"</b> <br><p><a href="+cvlattes+" target=_blank>"+cvlattes+"</a></font></td></tr> </table>  </td></tr> </table>"); \n\
                });\n\
                return marker; \n\
             };\n\
             function createMarker3(point, name, address, advisors, cvlattes, photo) { \n\
                var marker = new GMarker(point, markerOptions3); \n\
                GEvent.addListener(marker, "click", function() { \n\
                marker.openInfoWindowHtml(" <table> <tr bgcolor=#eced0c><td><font color=#000000><b>scriptLattes</b>: "+name+"</font></td></tr> <tr><td> <table><tr><td valign=top> <img src="+photo+" width=100px> </td><td> <font size=-2>"+address+"<br><b>"+advisors+"</b> <br><p><a href="+cvlattes+" target=_blank>"+cvlattes+"</a></font></td></tr> </table>  </td></tr> </table>"); \n\
                });\n\
                return marker; \n\
             };\n'

		cvsProcessados = set([])


		if self.grupo.obterParametro('mapa-incluir_membros_do_grupo'):
			for membro in self.grupo.listaDeMembros:
				cvsProcessados.add(membro.idLattes)

				membro.obterCoordenadasDeGeolocalizacao()
				if not membro.enderecoProfissionalLat=='0' and not membro.enderecoProfissionalLon=='0':
					self.mapa += '\nvar point0 = new GLatLng('+membro.enderecoProfissionalLat+'+0.001*Math.random(), '+membro.enderecoProfissionalLon+'+0.001*Math.random());'
					self.mapa += '\nmap.addOverlay(createMarker0(point0,"'+membro.nomeCompleto+'","'+membro.enderecoProfissional+'","'+membro.url+'","'+membro.foto+'"));'


		if self.grupo.obterParametro('mapa-incluir_alunos_de_pos_doutorado'):
			keys =self.grupo.compilador.listaCompletaOCSupervisaoDePosDoutorado.keys()
			for ano in keys:		
				for aluno in self.grupo.compilador.listaCompletaOCSupervisaoDePosDoutorado[ano]:
					idOrientando = aluno.idOrientando

					if len(idOrientando)==16 and cvsProcessados.isdisjoint([idOrientando]):
						membro = Membro('', idOrientando, '', '', '', '', '')
						membro.carregarDadosCVLattes()
						membro.obterCoordenadasDeGeolocalizacao()
						if not membro.enderecoProfissionalLat=='0' and not membro.enderecoProfissionalLon=='0':
							self.mapa += '\nvar point0 = new GLatLng('+membro.enderecoProfissionalLat+'+0.001*Math.random(), '+membro.enderecoProfissionalLon+'+0.001*Math.random());'
							self.mapa += '\nmap.addOverlay(createMarker1(point0,"'+membro.nomeCompleto+'","'+membro.enderecoProfissional+'","'+self.obterNomesDosOrientadores(aluno, self.grupo.listaDeMembros)+'","'+membro.url+'","'+membro.foto+'"));'
						print "-Processando o CV do ex-posdoc: "+idOrientando+" "+membro.nomeCompleto.encode('utf8')
						cvsProcessados.add(idOrientando)


		if self.grupo.obterParametro('mapa-incluir_alunos_de_doutorado'):
			keys =self.grupo.compilador.listaCompletaOCTeseDeDoutorado.keys()
			for ano in keys:		
				for aluno in self.grupo.compilador.listaCompletaOCTeseDeDoutorado[ano]:
					idOrientando = aluno.idOrientando

					if len(idOrientando)==16 and cvsProcessados.isdisjoint([idOrientando]):
						membro = Membro('', idOrientando, '', '', '', '', '')
						membro.carregarDadosCVLattes()
						membro.obterCoordenadasDeGeolocalizacao()
						if not membro.enderecoProfissionalLat=='0' and not membro.enderecoProfissionalLon=='0':
							self.mapa += '\nvar point0 = new GLatLng('+membro.enderecoProfissionalLat+'+0.001*Math.random(), '+membro.enderecoProfissionalLon+'+0.001*Math.random());'
							self.mapa += '\nmap.addOverlay(createMarker2(point0,"'+membro.nomeCompleto+'","'+membro.enderecoProfissional+'","'+self.obterNomesDosOrientadores(aluno, self.grupo.listaDeMembros)+'","'+membro.url+'","'+membro.foto+'"));'
						print "-Processando o CV do ex-aluno de doutorado: "+idOrientando+" "+membro.nomeCompleto.encode('utf8')
						cvsProcessados.add(idOrientando)


		if self.grupo.obterParametro('mapa-incluir_alunos_de_mestrado'):
			keys =self.grupo.compilador.listaCompletaOCDissertacaoDeMestrado.keys()
			for ano in keys:		
				for aluno in self.grupo.compilador.listaCompletaOCDissertacaoDeMestrado[ano]:
					idOrientando = aluno.idOrientando

					if len(idOrientando)==16 and cvsProcessados.isdisjoint([idOrientando]):
						membro = Membro('', idOrientando, '', '', '', '', '')
						membro.carregarDadosCVLattes()
						membro.obterCoordenadasDeGeolocalizacao()
						if not membro.enderecoProfissionalLat=='0' and not membro.enderecoProfissionalLon=='0':
							self.mapa += '\nvar point0 = new GLatLng('+membro.enderecoProfissionalLat+'+0.001*Math.random(), '+membro.enderecoProfissionalLon+'+0.001*Math.random());'
							self.mapa += '\nmap.addOverlay(createMarker3(point0,"'+membro.nomeCompleto+'","'+membro.enderecoProfissional+'","'+self.obterNomesDosOrientadores(aluno, self.grupo.listaDeMembros)+'","'+membro.url+'","'+membro.foto+'"));'
						print "-Processando o CV do ex-aluno de mestrado: "+idOrientando+" "+membro.nomeCompleto.encode('utf8')
						cvsProcessados.add(idOrientando)


		self.mapa+= '\
              } \n\
            } \n\
           </script>\n'


		#print "--------------------------------------------------------------------"
		#print self.mapa.encode('utf8','replace')
		#print "--------------------------------------------------------------------"
		print "\n[MAPA DE GEOLOCALIZACAO CRIADO]"


	def obterNomesDosOrientadores(self, aluno, listaDeMembros):
		lista = list(aluno.idMembro)
		if len(lista)==1:
			m = listaDeMembros[lista[0]]
			s = aluno.tipoDeOrientacao+': '+m.nomeCompleto
		else:
			s = 'Orientadores: ' 
			for i in lista:
				m = listaDeMembros[i]
				s+= m.nomeCompleto+', '
			s= s.rstrip(', ')+'.'

		return s

