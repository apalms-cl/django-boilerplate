# django-boilerplate

Este boilerplate para Django está construido utilizando el framework Django 4.x siguiendo algunas de las prácticas recomendadas en Two Scoops of Django 3.x. La documentación oficial de Django en conjunto con las buenas prácticas documentadas en el libro son recomendadas antes de modificar este proyecto.

## Consideraciones

### Automatización

Este proyecto considera la automatización de algunas tareas, por ejemplo:

- Actualización automática de los requirements.
- Actualización automática de los submodules.
- Formateo automático usando PEP8 usando `black` y linter del código usando `flake8`.

Estas automatizaciones se basan en rutas y nombres que deben ser actualizadas. Revisa las disponibles en:

- app/Makefile

### Al correrlo de forma local con Docker

```console
dev@LEMS ~/.docker/ $ make _build
dev@LEMS ~/.docker/ $ docker exec boilerplate python manage.py migrate
dev@LEMS ~/.docker/ $ docker exec -it boilerplate python manage.py createsuperuser
dev@LEMS ~/.docker/ $ docker exec -it boilerplate python manage.py loaddata _backup/polls.json
```
