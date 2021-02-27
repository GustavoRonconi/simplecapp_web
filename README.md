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
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">SimpleCapp - Web</h3>

  <p align="center">
    An awesome README template to jumpstart your projects!
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template">View Demo</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Report Bug</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

There are many great README templates available on GitHub, however, I didn't find one that really suit my needs so I created this enhanced one. I want to create a README template so amazing that it'll be the last one you ever need -- I think this is it.

Here's why:
* Your time should be focused on creating something amazing. A project that solves a problem and helps others
* You shouldn't be doing the same tasks over and over like creating a README from scratch
* You should element DRY principles to the rest of your life :smile:

Of course, no one template will serve all projects since your needs may be different. So I'll be adding more in the near future. You may also suggest changes by forking this repo and creating a pull request or opening an issue. Thanks to all the people have have contributed to expanding this template!

A list of commonly used resources that I find helpful are listed in the acknowledgements.

### Built With

* [Django](https://www.djangoproject.com/)
* [Celery](https://docs.celeryproject.org/)
* [Heroku](https://heroku.com)
* [Postgrees](https://postgrees.org)



<!-- GETTING STARTED -->
## Getting Started

Execute a instalação das dependências e rode o servidor, o mesmo disponibiliza os endpoints de API e um WebSite institucional.

### Prerequisites

django==3.1.5
djangorestframework==3.12.2
djangorestframework_simplejwt==4.6.0
django-rest-framework-social-oauth2==1.1.0
celery==4.4.6
redis==3.5.3
django-celery-results==1.2.1
celery-progress==0.0.10
channels==3.0.3
channels-redis==3.2.0
pytest-asyncio==0.14.0
django-heroku==0.3.1
whitenoise==5.2.0

### Installation

1. Clone the repo and run:
   ```python
   pip install -r requirements.txt
   ```


<!-- USAGE EXAMPLES -->
## Usage

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
## License

Copyright (C) SimpleCapp, Inc - Todos os direitos reservados.
 * Cópias dos arquivos, independente do meio, estão estritamente proibidas
 * Escrito por Gustavo A. Ronconi <gustavoronconi95@gmail.com>, Fevereiro 2021.



<!-- CONTACT -->
## Contact

Gustavo A. Ronconi - gustavoronconi95@gmail.com.com

Project Link: [https://github.com/GustavoRonconi/simplecapp-web](https://github.com/GustavoRonconi/simplecapp-web)



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
