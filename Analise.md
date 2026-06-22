# Trab-governanca
Neste trabalho, o foco seria justamente a analise da diferenca no output de IAs generativas para situacoes com e sem governanca. Neste estudo, foram utilizadas duas IAs diferentes: ChatGPT e Claude. O Claude foi utilizado para fins de organizacao do fluxo de trabalho, bem como a criacao do codigo inicial com as vulnerabilidades a serem observadas. O fim era evitar qualquer tipo de bias, caso ambos os codigos gerados com e sem vulnerabilidades e posteriormente analisados fossem provenientes da mesma IA generativa (ex: GPT poderia apresentar vicios que poderiam ser facilmente detectados por si mesmo em teste posterior, o que poderia anular a credibilidade do estudo em questao).
No trabalho de governanca, foram utilizados primariamente dois cenarios como guia:

  Cenario A - com governanca (ChatGPT):
    No cenario A, foi dado ao ChatGPT o codigo gerado pelo Claude, com as vulnerabilidades de codigo. Juntamente, foi inserido um texto com recomendacoes/regras de governanca, que serviriam de diretrizes para a analise utilizada pela IA generativa. Desse modo, o     intuito inicial era justamente compreender quais regras seriam (e se seriam realmente) seguidas, com o rigor necessario.<br>
    Foi notado que, durante o cenario A, houve nao apenas o respeito as diretrizes impostas (como por exemplo de nao fazer algo caso nao possa ser documentavel. ex: alterar valores de constantes ambientais sem uma referencia clara antes), mas tambem a criacao de     novos artefatos que pudessem ser utilizados para tais fins.<br>
    Tambem houve uma clareza notoria da IA generativa no tom descritivo das mudancas, bem como as diretrizes que antes estavam sendo violadas, para referencia e documentacao futuras.
    
  Cenario B - sem governanca (ChatGPT):
    De forma analoga ao cenario A, foi dado o mesmo codigo gerado pelo Claude, mas ao inves de ter um guia de regras/diretrizes a serem seguidas, foi dada uma certa liberdade para a IA no que tangente a forma como as vulnerabilidades devem ser geridas.<br>
    Como esperado, durante o cenario B, ainda que a IA respeitasse boas praticas de programacao, ate certo nivel, nao houve uma clareza na parte de documentacao/explicacao nas mudancas ocorridas. No contexto da GreenOps, esse tipo de erro seria considerado           critico, ja que uma empresa amplamente afetada por regulamentacoes ambientais e de seguranca poderia facilmente ser alvo de investigacoes ao nao adotar certas diretrizes legais/tecnicas e rigor durante o decorrer de seus processos.<br>
    Foram notadas algumas sugestoes da IA, que poderiam tambem ser utilizadas/adotadas arbitrariamente por programadores, sem qualquer cuidado ou documentacao, que poderia ou nao ocorrer por parte dos mesmos.<br>
    Foi feito um teste extra, para fins de curiosidade, com o mesmo prompt utilizado. Como esperado, a forma que a IA lidou com o codigo foi completamente diferente da inicial (que esta documentada), e isso poderia gerar inconsistencias no proprio codigo. Houve      um ponto em comum entre ambos, que foi justamente a falta de rigor durante a parte de documentacao para usos futuros.

Em seguida, as perguntas a serem respondidas no tangente ao item 4 do trabalho, para fins de auditoria:
1. A IA seguiu as regras de governança quando devidamente instruída? Onde falhou ou foi imprecisa?
    De forma surpreendente, as regras foram seguidas com rigor. Foi dado inclusive a sugestao de criacao de uma nova funcao que alinhasse o projeto as conformidades previstas nas diretrizes de governanca. As falhas vieram majoritariamente do cenario B:               ocultacao/omissao de certos processos que poderiam resultar em medidas legais cabiveis (como a falta de testes dos sensores, que por si so ja gerariam irregularidades), sugestoes que poderiam ou nao ser seguidas, imprecisao na hora de detalhar o que foi          feito etc.
2. Quais riscos concretos surgiram no Cenário B? Como eles se relacionam com a vulnerabilidade escolhida?
    Como mencionado no item 1, surgiram diversas variaveis, que poderiam alterar a forma que o processo foi documentado e gerar incerteza em sua auditabilidade, bem como abrir precedentes para questionar a legalidade de certas praticas. Isso poderia prejudicar       diretamente a empresa.
4. Como você, como analista de Governança de TI, detectaria essas violações em ambiente real de trabalho (ferramentas, processos, auditorias)?
    Alem de seguir a risca as diretrizes ja documentadas (legais, tecnicas etc) em voga, poderiam tambem ser utilizados frameworks de qualidade, revisoes de codigo e ferramentas de analise que verifiquem a conformidade, rastreabilidade etc.
6. Que ajustes faria nas regras de governança após observar os resultados da simulação?
    Como as regras foram em algum grau guiadas tambem pelas vulnerabilidades que foram encontradas, muito provavelmente nao haveriam ajustes nesse caso. Entretanto, compreendo que esse nao seria o caso na maioria dos casos, onde o escopo pode ser muito maior, a      depender da area e do tamanho do projeto.
7. Quais são os limites do controle via prompt? O que a governança de IA exige além da instrução textual?
    Como a IA pode acabar interpretando as coisas de forma um pouco mais "livre", isso pode (ou nao) acarretar em um nivel de heterogeneidade nos resultados. Por isso, acaba sendo de suma importancia que haja a auditoria, de forma independente e constante, feita     por e para seres humanos, de forma a garantir sempre a rastreabilidade, conformidade, transparencia e legitimidade dos dados apresentados.

Disclaimers: 
1. Analise critica feita INTEIRAMENTE por mim, sem assistencia alguma.
2. Foram utilizadas ferramentas de IA para elaboracao do cenario (1), contexto (1), codigo com falhas(3) e regras de governanca(2), todas com a devida revisao e supervisao humana. 
