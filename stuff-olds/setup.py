# Arquivo para geração do executável 'scriptLattes'
#
# Run the build process by running the command 'python setup build'
#
# If everything works well you should find a subdirectory in the build
# subdirectory that contains the files needed to run the script without Python
#
# Seg Abr 01 08:21:21 BRT 2011

import sys
from cx_Freeze import setup, Executable

buildOptions = dict(
        compressed = True,
        includes = ["scriptLattes", "grupo", "membro", "parserLattes", "geradorDePaginasWeb", "compiladorDeListas", "pygraphviz", "matplotlib","geolocalizador", "graficoDeBarras", "graficoDeProporcoes", "grafoDeColaboracoes", "mapaDeGeolocalizacao", "orientacaoConcluida", "orientacaoEmAndamento", "producaoArtistica", "apresentacaoDeTrabalho", "livroPublicado", "textoEmJornalDeNoticia", "artigoAceito", "outroTipoDeProducaoBibliografica", "trabalhoCompletoEmCongresso", "artigoEmPeriodico", "resumoEmCongresso", "capituloDeLivroPublicado", "resumoExpandidoEmCongresso", "outroTipoDeProducaoTecnica", "produtoTecnologico", "softwareSemPatente", "processoOuTecnica", "softwareComPatente", "trabalhoTecnico", "areaDeAtuacao", "formacaoAcademica", "idioma", "premioOuTitulo", "projetoDePesquisa", "matplotlib.backends.backend_tkagg"],
        path = sys.path + ["scriptLattes"])

setup(
        name = "advanced_cx_Freeze_sample",
        version = "0.1",
        description = "Advanced sample cx_Freeze script",
        options = dict(build_exe = buildOptions),
        executables = [Executable("scriptLattes.py")] )

