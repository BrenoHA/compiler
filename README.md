# Mgol Compiler

by <a href="https://github.com/BrenoHA">Breno Hasparyk</a> and <a href="https://github.com/edu290399">Eduardo Silvestre</a>

## Autômato finito determinístico - Analisador Léxico

<img align="center" width="350"  src="public/automatoLexico.jpg">

## Descrição Geral

A atividade prática, estudo de caso dividido em três etapas T1 (Implementação do Trabalho 1), T2
(Implementação do Trabalho 2) e T3 (Implementação do Trabalho 3) em Compiladores, é um
componente para a avaliação e desenvolvimento dos conhecimentos desenvolvidos nas disciplinas
ofertadas para Ciência da Computação e Engenharia de Computação - Compiladores e
Compiladores 1. O valor total dos três trabalhos é 8,0, conforme estabelecido no Plano de curso da
disciplina, e compõe a média de aprovação na disciplina.

A disciplina de compiladores preocupa-se em estudar técnicas e teorias com a finalidade de
proporcionar o conhecimento para a construção de um compilador. Para tal, durante o semestre
investigar-se-á seus componentes sobre aspectos teóricos e práticos em um estudo de caso. Esse
estudo envolverá o desenvolvimento (implementação) de um compilador que receberá como entrada
um arquivo fonte na linguagem de programação Mgol (linguagem desenvolvida para o estudo de
caso em questão), realizará as fases de análise e síntese (T1,T2 e T3) e gerará um arquivo objeto
em linguagem C. O arquivo final deverá ser compilável em compilador C, ou seja, o código gerado
deverá estar completo para compilação e execução.

A Figura 1 apresenta o modelo de arquitetura do compilador que será desenvolvido durante o
semestre. Os módulos a serem implementados contemplam:

• T1 – Implementação do Trabalho 1: desenvolvimento do analisador léxico e da tabela de
símbolos;

• T2 - Implementação do Trabalho 2: desenvolvimento do analisador sintático ascendente
SLR(1) para verificação de sintaxe com dados obtidos do analisador léxico (T1) e também a
recuperação do erro com reestabelecimento da análise;

• T3 – Implementação do Trabalho 3: desenvolvimento do analisador semântico e geração de
código final a partir do método tradução dirigida pela sintaxe (conexão com T2)
