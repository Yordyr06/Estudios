-- TAGS Y VERSIONES EN GIT Y GITHUB --

Los tags o etiquetas nos permiten asignar versiones a los commits
con cambios más importantes o significativos de nuestro proyecto.



-- COMANDOS BÁSICOS PARA TRABAJAR CON ETIQUETAS (TAGS) --

* git tag -a nombre-del-tag id-del-commit: Crear un nuevo tag y asignarlo a un commit
* git tag -d nombre-del-tag: Borrar un tag en el repositorio local.
* git tag o git show-ref --tags: Listar los tags de nuestro repositorio local.
* git push origin --tags: Publicar un tag en el repositorio remoto
* git tag -d nombre-del-tag y git push origin :refs/tags/nombre-del-tag:
    Borrar un tag del repositorio remoto.



-- CÓMO AGREGAR UN ALIAS SOLO PARA GIT --

1. Para un proyecto: git config alias.arbolito "log --all --graph --decorate --oneline"
2. Global: git config --global alias.arbolito "log --all --graph --decorate --oneline"
3. Para correrlo: git arbolito
