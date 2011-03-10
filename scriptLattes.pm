#
#
#  Copyright 2005-2010: Jesús P. Mena-Chalco e Roberto M. Cesar-Jr.
#
#
#  Este arquivo é parte do programa sriptLattes.
#  scriptLattes é um software livre; você pode redistribui-lo e/ou 
#  modifica-lo dentro dos termos da Licença Pública Geral GNU como 
#  publicada pela Fundação do Software Livre (FSF); na versão 2 da 
#  Licença, ou (na sua opnião) qualquer versão.
#
#  Este programa é distribuido na esperança que possa ser util, 
#  mas SEM NENHUMA GARANTIA; sem uma garantia implicita de ADEQUAÇÂO a qualquer
#  MERCADO ou APLICAÇÃO EM PARTICULAR. Veja a
#  Licença Pública Geral GNU para maiores detalhes.
#
#  Você deve ter recebido uma cópia da Licença Pública Geral GNU
#  junto com este programa, se não, escreva para a Fundação do Software
#  Livre(FSF) Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
#


##################################################################################
# scriptLattes                                                                   #
#                                                                                #
# Modulo usado HTML::Parser. Para extrair as produções em C,T & A                #
# de todos os tipos em formato de tabelas HTML                                   #
#                                                                                #
# $self->{Publication_type}[X]: Contem o nomes do tipo de publicações X.         #
# $self->{Publication}[Y]     : Contem as publicações correspondentes ao tipo Y. #
#                                                                                #
# $self->{Orientacoes_status}[P]: Nomes dos estados de orientacao                #
# $self->{Orientacoes_type}[P]  : Nomes dos tipos de orientacao                  #
#                                                                                #
# $self->{Orientacoes_adamento}[P]  : items ...                                  #
# $self->{Orientacoes_concluidas}[P]: items ...                                  #
#                                                                                #
# $self->{ProducaoTecnica_type}[X]:                                              #
# $self->{ProducaoTecnica}[Y]     :                                              #
#                                                                                #
# $self->{ProducaoArtistica_type}[X]:                                            #
# $self->{ProducaoArtistica}[Y]     :                                            #
#                                                                                #
# $self->{BancasExaminadoras_type}[X]:                                           #
# $self->{BancasExaminadoras}[Y]     :                                           #
#                                                                                #
# $self->{ComissoesJulgadoras_type}[X]:                                          #
# $self->{ComissoesJulgadoras}[Y]     :                                          #
#                                                                                #
# $self->{Eventos_type}[X]:                                                      #
# $self->{Eventos}[Y]     :                                                      #
#                                                                                #
# $self->{Name}                                                                  #
# $self->{PhotoID}                                                               #
# $self->{Address}                                                               #
# $self->{Orientandos}[X]                                                        #
# $self->{Updated}                                                               #
#                                                                                #
##################################################################################

package scriptLattes;
use strict;
use vars qw(@ISA $infield $inrecord $intable $inlink $go_on $start_session $table_type $validated_table $newID $start_address $validated_address $validated_name $internal_text);
@ISA = qw(HTML::Parser);
require HTML::Parser;

# Override do prodedimento start
sub start()
{
   my($self,$tag,$attr,$attrseq,$orig) = @_;

   # Variáveis para busca
   if ( $tag eq 'html' ) 
   { 
     $self->{Address} = "";
     $self->{Name} = "";
	 $self->{PhotoID} = "";
	 $self->{Updated} = "";
		
	 # lower cases!
     @{$self->{Publication_type}} = (
	   "Artigos completos publicados em periódicos",
	   "Livros publicados\/organizados ou edições",
	   "Capítulos de livros publicados",
       "Textos em jornais de notícias\/revistas",
	   "Trabalhos completos publicados em anais de congressos",
	   "Resumos expandidos publicados em anais de congressos",
	   "Resumos publicados em anais de congressos",
       "Artigos aceitos para publicação",
	   "Apresentações de trabalho",
	   "Demais tipos de produção bibliográfica",
       );
	 
	 @{$self->{Orientacoes_status}} = (
	   "Orientações em andamento",
	   "Supervisões e orientações concluídas",
	   );
	 
	 @{$self->{Orientacoes_type}} = (
	   "Supervisão de pós-doutorado",
	   "Tese de doutorado",
	   "Dissertação de mestrado",
       "Monografia de conclusão de curso de aperfeiçoamento\/especialização",
	   "Trabalho de conclusão de curso de graduação",
	   "Iniciação científica",
	   "Orientações de outra natureza",
	   );

	 @{$self->{ProducaoTecnica_type}} = (
	   "Softwares com registro de patente",
	   "Softwares sem registro de patente",
	   "Produtos tecnológicos",
       "Processos ou técnicas",
	   "Trabalhos técnicos",
	   "Demais tipos de produção técnica",
	   );

	 @{$self->{ProducaoArtistica_type}} = (
	   "Produção artística\/cultural",
	   );

	###########################################################
	 @{$self->{BancasExaminadoras_type}} = (
	   "Teses de doutorado",
	   "Qualificações de doutorado",
	   "Dissertações",
       "Trabalhos de conclusão de curso de graduação",
	   );
	 
	@{$self->{ComissoesJulgadoras_type}} = (
	   "Professor titular",
	   "Concurso público",
	   "Livre docência",
	   "Avaliação de cursos",
       "Outras participações",
	   );
	
	@{$self->{Eventos_type}} = (
	   "Participação em eventos",
	   "Organização de eventos",
	   );

	###########################################################

	$go_on = 0;
	$internal_text = "";
   }

   if ( $tag eq 'table' && $orig =~ m/class="IndiceTabela"/i )
   { 
     $go_on = 1;
   }

   # Inicio de uma nova tabela
   if ( $tag eq 'table' && $start_session )
   { 
     #$self->{Table} = '<table>'; 
     $self->{Table} = ''; 
	 $intable++; 
	 $validated_table = 1;
   }
   
   # Inicio de uma nova fila
   if ( $tag eq 'tr' && $validated_table ) 
   { 
     #$self->{Row} = '<tr>'; 
     $self->{Row} = ''; 
	 $inrecord++ ; 
   }

   # Inicio de uma celula válida. Não serão consideradas as numerações do HTML Lattes
   if ( $tag eq 'td' && $validated_table && $orig =~'textoProducao' ) 
   { 
     #$self->{Field}  = '<td>'; 
     $self->{Field}  = ''; 
	 $infield++;
   }
   if ( $tag eq 'td' && $start_address ) 
   { 
     $self->{Address}  = ''; 
     $validated_address = 1;
   }

   # Inicio do link
   if ( $tag eq 'a' && $validated_table && $infield && $orig=~m/lattes\.cnpq\.br/i) 
   { 
	 $inlink++; 
	 
	 if ($start_session==2 || $start_session==3) # icone Lattes para os orientandos
     {
	    $self->{Link} = $orig."<img border=0 src=./logolattes.gif>"; 
     }

	 if ($table_type==1 && $start_session==3) # alunos com doutorado concluído
     {
        $orig =~ m/(\d{16})/;
	    $newID = $1;
     }
   }

   if ( $tag eq 'p' && $orig=~m/class="titulo"/i) 
   { 
     $self->{Name}  = '';
     $validated_name = 1; 
   }
  
   if( $tag eq 'br' && $validated_name ) 
   { 
     $validated_name = 0;
   }

   if ( $tag eq 'img' && $orig=~m/servletrecuperafoto/i) 
   { 
     $orig =~ m/id=(\w*)"/;
     $self->{PhotoID} = $1;
   }

   $internal_text = "";
}


# Override do procedimento text
sub text()
{
	# start_session
	#     1 : Publicacoes
	#     2 : Orientacoes em adamento
	#     3 : Orientacoes concluidas
	#     4 : Producao tecnica
	#     5 : Producao artistica
	#     6 : Bancas examinadoras   7.02
	#     7 : Comissoes julgadoras  7.02
	#     8 : Eventos               7.02

	my ($self,$text) = @_;

	$text =~ s/&nbsp;/ /gi;
	$text =~ s/\n/ /gi;
	$text =~ s/\./\. /gi;
	$text =~ s/\s+/ /gi;
	$text =~ s/&ccedil;/ç/gi;
	$text =~ s/&aacute;/á/gi;
	$text =~ s/&eacute;/é/gi;
	$text =~ s/&iacute;/í/gi;
	$text =~ s/&oacute;/ó/gi;
	$text =~ s/&uacute;/ú/gi;
	$text =~ s/&atilde;/ã/gi;
	$text =~ s/&otilde;/õ/gi;
	$text =~ s/&ocirc;/ô/gi;
	$text =~ s/&ecirc;/ê/gi;
	$text =~ s/&Agrave;/À/gi;
	$text =~ s/&agrave;/à/gi;
	$text =~ s/&Egrave;/È/g;
	$text =~ s/&egrave;/è/g;
  
	$internal_text .= $text; 

#	$internal_text =~ s/\n/ /gi;
#	$internal_text =~ s/\s+/ /gi;
	$internal_text =~ s/^\s+//gi;
	$internal_text =~ s/\s+$//gi;

	if ($go_on)
	{
		# -------------------------------------------------------------- # 
		# Seleção do tipo de publicação 
		if ($self->{Publication_type})
		{
			# my $MAX = @{$self->{Publication_type}};
			my $MAX = 10;
	    	for (my $i=0; $i<$MAX; $i++)
		    { 
				if (lc($internal_text) eq lc($self->{Publication_type}[$i]))   
  		   		{ 
	    			$table_type      = $i; 
	  			  	$start_session   = 1; 
				  	$validated_table = 0;
			   	} 
	 		}
		}	
	
		# -------------------------------------------------------------- # 
    	# Seleção do tipo de status
		if ($self->{Orientacoes_status})
		{
		    for (my $i=0; $i<2; $i++)
    		{
				if (lc($internal_text) eq lc($self->{Orientacoes_status}[$i]))
  		   		{ 
  			  		$start_session   = $i+2;
			  		$validated_table = 0;
			   	} 
			}
		}

		# -------------------------------------------------------------- # 
	    # Seleção do tipo de orientacao
		if ($self->{Orientacoes_type} && $start_session)
		{
			# $MAX = @{$self->{Orientacoes_type}};
			my $MAX = 7;
	    	for (my $i=0; $i<$MAX; $i++)
		    {
				if (lc($internal_text) eq lc($self->{Orientacoes_type}[$i]) && $start_session>=2)
  		   		{ 
	    			$table_type      = $i; 
		   		} 
			}
		}

		# -------------------------------------------------------------- # 
		# Seleção do tipo de produção técnica 
		if ($self->{ProducaoTecnica_type})
		{
			# my $MAX = @{$self->{ProducaoTecnica_type}};
			my $MAX = 6;
    		for (my $i=0; $i<$MAX; $i++)
	    	{ 
				if (lc($internal_text) eq lc($self->{ProducaoTecnica_type}[$i]))   
  	   			{ 
	    			$table_type      = $i; 
	  		  		$start_session   = 4; 
				  	$validated_table = 0;
			   	} 
 			}
		}

		# -------------------------------------------------------------- # 
		# Seleção do tipo de produção artística
		if ($self->{ProducaoArtistica_type})
		{
			# my $MAX = @{$self->{ProducaoArtistica_type}};
			my $MAX = 1;
	    	for (my $i=0; $i<$MAX; $i++)
		    { 
				if (lc($internal_text) eq lc($self->{ProducaoArtistica_type}[$i]))   
  	   			{ 
		    		$table_type      = $i; 
		  		  	$start_session   = 5; 
				  	$validated_table = 0;
			   	} 
 			}
		}
		###################################################################################

		# -------------------------------------------------------------- # 
		# Seleção do tipo de bancas examinadoras
		if ($self->{BancasExaminadoras_type})
		{
			my $MAX = 4;
    		for (my $i=0; $i<$MAX; $i++)
	    	{ 
				if (lc($internal_text) eq lc($self->{BancasExaminadoras_type}[$i]))   
  	   			{ 
	    			$table_type      = $i;
	  		  		$start_session   = 6;
				  	$validated_table = 0;
			   	} 
 			}
		}
		
		# -------------------------------------------------------------- # 
		# Seleção do tipo de bancas examinadoras
		if ($self->{ComissoesJulgadoras_type})
		{
			my $MAX = 5;
    		for (my $i=0; $i<$MAX; $i++)
	    	{ 
				if (lc($internal_text) eq lc($self->{ComissoesJulgadoras_type}[$i]))
  	   			{ 
	    			$table_type      = $i;
	  		  		$start_session   = 7;
				  	$validated_table = 0;
			   	} 
 			}
		}

		# -------------------------------------------------------------- # 
		# Seleção do tipo de eventos
		if ($self->{Eventos_type})
		{
			my $MAX = 2;
    		for (my $i=0; $i<$MAX; $i++)
	    	{ 
				if (lc($internal_text) eq lc($self->{Eventos_type}[$i]))
  	   			{
	    			$table_type      = $i;
	  		  		$start_session   = 8;
				  	$validated_table = 0;
			   	} 
 			}
		}


		###################################################################################
		###################################################################################

	}


	if ($internal_text=~"Endereço profissional")
	{
		$start_address = 1;
		$validated_address = 0;
	}

	if ($start_address && $validated_address) 
	{
  		$self->{Address} .= " ".$text; 
	}   
	
	if ($validated_name) 
	{
  		$self->{Name} .= " ".$text; 
	}   
	
 	# -#-#-#-#-#-#-#---------------------------------------------------------------------------
 	$internal_text=~m/última atualização do currículo em (.*)/i;
	if ($1)
	{
		$self->{Updated} = $1;
	}
 	# -#-#-#-#-#-#-#---------------------------------------------------------------------------
	# -------------------------------------------------------------- # 
	# Casos especiais de parada:
    # Acho que não existe alguma outra forma para parar a busca
  ##### if ( $internal_text=~"Bancas" || $internal_text=~"Eventos" || $internal_text=~"Demais trabalhos" || $internal_text=~"Outras informações relevantes" || $internal_text=~"Atuação profissional" || $internal_text=~"Conselhos, Comissões e Consultoria" || $internal_text=~m/ensino.*nível:/i)
    if ( $internal_text=~"Bancas" || $internal_text=~"Demais trabalhos" || $internal_text=~"Outras informações relevantes" || $internal_text=~"Atuação profissional" || $internal_text=~"Conselhos, Comissões e Consultoria" || $internal_text=~m/ensino.*nível:/i)
    { 
    	$start_session   = 0; 
		$validated_table = 0; 
	}

	# Atribuição do texto para tabelas validas
	if ($intable && $inrecord && $infield && $start_session && $validated_table) 
	{
   		$self->{Field} .= $text; 
	}   
	
}

# Override do procedimento end
sub end()
{
   my ($self,$tag) = @_;

   $internal_text = "";
   
   # Fim de uma tabela
   if($tag eq 'table' && $validated_table)
   {
     $intable--;
     #$self->{Table} .= '</table>';
     $self->{Table} .= '';

	 # Finalmente é inserido o item ;-)
	 if ($self->{Table} ne '')
	 {

		##############################################################
		$self->{Table} =~ s/^\.//gi;		

	 	if ($self->{Link})
		 {
		 	$self->{Table} .= $self->{Link}; 
	 		undef $self->{Link}; 
		 }


		##############################################################

	 	if ($start_session==1)
		{
	       push @{$self->{Publication}[$table_type]}, $self->{Table};
		}

	 	if ($start_session==2)
		{
	       push @{$self->{Orientacoes_andamento}[$table_type]}, $self->{Table};
		}

	 	if ($start_session==3)
		{
	       push @{$self->{Orientacoes_concluidas}[$table_type]}, $self->{Table};

	 	   if ($table_type==1 && $newID) # alunos com doutorado concluído e ID Lattes cadastrado
		   {
		       push @{$self->{Orientandos}}, $newID; 
			   undef $newID;
           }
		}

	 	if ($start_session==4)
		{
	       push @{$self->{ProducaoTecnica}[$table_type]}, $self->{Table};
		}

	 	if ($start_session==5)
		{
	       push @{$self->{ProducaoArtistica}[$table_type]}, $self->{Table};
		}
		
		###############################################################
	 	if ($start_session==6)
		{
	       push @{$self->{BancasExaminadoras}[$table_type]}, $self->{Table};
		}
	 	
		if ($start_session==7)
		{
	       push @{$self->{ComissoesJulgadoras}[$table_type]}, $self->{Table};
		}
	 	
		if ($start_session==8)
		{
	       push @{$self->{Eventos}[$table_type]}, $self->{Table};
		}

		###############################################################
	 }
   }

   # Fim de uma linha
   if($tag eq 'tr' && $validated_table ) 
   { 
     $inrecord--; 
	 #$self->{Table} .= $self->{Row} . '</tr>'; 
	 $self->{Table} .= $self->{Row}; 
   }
   
   # Fim de uma celula
   if($tag eq 'td' && $validated_table && $infield) 
   { 
	 ####if ($self->{Link})
	 ####{
	 ####	$self->{Row} .= $self->{Link}; 
	 ####	undef $self->{Link}; 
	 ####}

     $infield--; 
	 $self->{Row} .= $self->{Field}; 
	 #$self->{Row} .= $self->{Field} . '</td>'; 
   }

   if($tag eq 'td' && $validated_address) 
   { 
     $start_address = 0;
     $validated_address = 0;
   }

   if($tag eq 'a' && $validated_table && $infield && $inlink) 
   { 
     $inlink--; 
	 
	 #################### if ($start_session==3 || $start_session==4)
	 if ($start_session==2 || $start_session==3)
	 {
       $self->{Link} .= '</a>'; 
     }
   }

   if($tag eq 'p' && $validated_name) # para nao extrair a bolsa de produtividade...
   { 
     $validated_name = 0;
   }
   
}

1;
