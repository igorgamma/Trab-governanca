# Trab-governança

Neste trabalho, o foco seria justamente a análise da diferença no output de IAs generativas para situações com e sem governança. Neste estudo, foram utilizadas duas IAs diferentes: ChatGPT e Claude. O Claude foi utilizado para fins de organização do fluxo de trabalho, bem como a criação do código inicial com as vulnerabilidades a serem observadas. O fim era evitar qualquer tipo de viés, caso ambos os códigos gerados com e sem vulnerabilidades e posteriormente analisados fossem provenientes de uma mesma IA generativa (ex: GPT poderia apresentar vícios que poderiam ser facilmente detectados por si mesmo em teste posterior, o que poderia anular a credibilidade do estudo em questão).

No trabalho de governança, foram utilizados primariamente dois cenários como guia:

Cenário A - com governança (ChatGPT):
No cenário A, foi dado ao ChatGPT o código gerado pelo Claude, com as vulnerabilidades de código. Juntamente, foi inserido um texto com recomendações/regras de governança, que serviriam de diretrizes para a análise utilizada pela IA generativa. Desse modo, o intuito inicial era justamente compreender quais regras seriam (e se seriam realmente) seguidas, com o rigor necessário.
Foi notado que, durante o cenário A, houve não apenas o respeito às diretrizes impostas (como, por exemplo, de não fazer algo caso não possa ser documentável, ex: alterar valores de constantes ambientais sem uma referência clara antes), mas também a criação de novos artefatos que pudessem ser utilizados para tais fins.
Também houve uma clareza notória da IA generativa no tom descritivo das mudanças, bem como as diretrizes que antes estavam sendo violadas, para referência e documentação futuras.

Cenário B - sem governança (ChatGPT):
De forma análoga ao cenário A, foi dado o mesmo código gerado pelo Claude, mas, ao invés de ter um guia de regras/diretrizes a serem seguidas, foi dada uma certa liberdade para a IA no que tangente à forma como as vulnerabilidades devem ser geridas.
Como esperado, durante o cenário B, ainda que a IA respeitasse boas práticas de programação até certo nível, não houve uma clareza na parte de documentação/explicação nas mudanças ocorridas. No contexto da GreenOps, esse tipo de erro seria considerado crítico, já que uma empresa amplamente afetada por regulamentações ambientais e de segurança poderia facilmente ser alvo de investigações ao não adotar certas diretrizes legais/técnicas e rigor durante o decorrer de seus processos.
Foram notadas algumas sugestões da IA, que poderiam também ser utilizadas/adotadas arbitrariamente por programadores, sem qualquer cuidado ou documentação, o que poderia ou não ocorrer por parte dos mesmos.
Foi feito um teste extra, para fins de curiosidade, com o mesmo prompt utilizado. Como esperado, a forma que a IA lidou com o código foi completamente diferente da inicial (que está documentada), e isso poderia gerar inconsistências no próprio código. Houve um ponto em comum entre ambos, que foi justamente a falta de rigor durante a parte de documentação para usos futuros.
Em seguida, as perguntas a serem respondidas no tangente ao item 4 do trabalho, para fins de auditoria:

1.A IA seguiu as regras de governança quando devidamente instruída? Onde falhou ou foi imprecisa?
De forma surpreendente, as regras foram seguidas com rigor. Foi dado inclusive a sugestão de criação de uma nova função que alinhasse o projeto às conformidades previstas nas diretrizes de governança. As falhas vieram majoritariamente do cenário B: ocultação/omissão de certos processos que poderiam resultar em medidas legais cabíveis (como a falta de testes dos sensores, que por si só já gerariam irregularidades), sugestões que poderiam ou não ser seguidas, imprecisão na hora de detalhar o que foi feito etc.
2.Quais riscos concretos surgiram no Cenário B? Como eles se relacionam com a vulnerabilidade escolhida?
Como mencionado no item 1, surgiram diversas variáveis que poderiam alterar a forma que o processo foi documentado e gerar incerteza em sua auditabilidade, bem como abrir precedentes para questionar a legalidade de certas práticas. Isso poderia prejudicar diretamente a empresa.
3.Como você, como analista de Governança de TI, detectaria essas violações em ambiente real de trabalho (ferramentas, processos, auditorias)?
Além de seguir à risca as diretrizes já documentadas (legais, técnicas etc.) em voga, poderiam também ser utilizados frameworks de qualidade, revisões de código e ferramentas de análise que verifiquem a conformidade, rastreabilidade etc.
4.Que ajustes faria nas regras de governança após observar os resultados da simulação?
Como as regras foram em algum grau guiadas também pelas vulnerabilidades que foram encontradas, muito provavelmente não haveriam ajustes nesse caso. Entretanto, compreendo que esse não seria o caso na maioria das situações, onde o escopo pode ser muito maior, a depender da área e do tamanho do projeto.
5.Quais são os limites do controle via prompt? O que a governança de IA exige além da instrução textual?
Como a IA pode acabar interpretando as coisas de forma um pouco mais "livre", isso pode (ou não) acarretar em um nível de heterogeneidade nos resultados. Por isso, acaba sendo de suma importância que haja a auditoria, de forma independente e constante, feita por e para seres humanos, de forma a garantir sempre a rastreabilidade, conformidade, transparência e legitimidade dos dados apresentados.

Disclaimers:

Análise crítica feita inteiramente por mim, sem assistência alguma.
Foram utilizadas ferramentas de IA para elaboração do cenário (1), contexto (1), código com falhas (3) e regras de governança (2), todas com a devida revisão e supervisão humana.
