<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="static/images/icone.png" alt="Logo" width="300" height="300">
  </a>

  <h3 align="center">SimpleCapp - Web</h3>

  <p align="center">
    API para integração de carteira de investimentos e cálculo de imposto de renda.
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Sumário</summary>
  <ol>
    <li>
      <a href="#about-the-project">Sobre o projeto</a>
      <ul>
        <li><a href="#built-with">Construído a partir</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Iniciando</a>
      <ul>
        <li><a href="#prerequisites">Pré-requisitos</a></li>
        <li><a href="#installation">Instalação</a></li>
      </ul>
    </li>
    <li><a href="#usage">Utilização</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#license">Licença</a></li>
    <li><a href="#contact">Contato</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## Sobre o Projeto


Só no ano passado um milhão de brasileiros passaram a investir na bolsa de valores, vários destes brasileiros têm dificuldade de entender a influência de seus investimentos sobre o IRPF, a intenção do aplicativo é auxiliar os usuários sobre como declarar a renda obtida nos investimentos, calcular tudo que é necessário para simplificar esta declaração e por fim gerar documentos e relatórios necessários para o processo.

Este reposítorio contempla toda a parte de backend relacionada ao projeto, incluindo um site institucional.

### Construído a partir:

* [Django](https://www.djangoproject.com/)
* [Celery](https://docs.celeryproject.org/)
* [Heroku](https://heroku.com)
* [Postgrees](https://postgrees.org)



<!-- GETTING STARTED -->
## Iniciando

Execute a instalação das dependências e rode o servidor, o mesmo disponibiliza os endpoints de API e um WebSite institucional.

### Pré-requisitos

* django==3.1.5
* djangorestframework==3.12.2
* djangorestframework_simplejwt==4.6.0
* django-rest-framework-social-oauth2==1.1.0
* celery==4.4.6
* redis==3.5.3
* django-celery-results==1.2.1
* celery-progress==0.0.10
* channels==3.0.3
* channels-redis==3.2.0
* pytest-asyncio==0.14.0
* django-heroku==0.3.1
* whitenoise==5.2.0

### Instalação

1. Clone o projeto e rode:
   ```python
   pip install -r requirements.txt
   ```


<!-- USAGE EXAMPLES -->
## Utilização

API para sincronização da carteira de investimentos e realização dos cálculos de imposto de renda.

1. Para iniciar:
   ```sh
   daphne simplecapp.asgi:application --port 8000 --bind 0.0.0.0 -v2
   celery -A simplecapp worker -l info  
   ```


<!-- ROADMAP -->
## Roadmap

Todo roadmap está disponível no [Trello] (https://trello.com/b/OZz7B2ac/simplecapp-desenvolvimento-de-produto).



<!-- LICENSE -->
## Licença

Copyright (C) SimpleCapp, Inc - Todos os direitos reservados.
 * Cópias dos arquivos, independente do meio, estão estritamente proibidas
 * Escrito por Gustavo A. Ronconi <gustavoronconi95@gmail.com>, Fevereiro 2021.



<!-- CONTACT -->
## Contato

Gustavo A. Ronconi - gustavoronconi95@gmail.com.com



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

