- Ne pas oublier d'activer le virtualenv a chaque fois avec cette commande :

`$> . /opt/<proj>/virt/bin/activate`

- Pour lancer le serveur Django :

`./manage.py runserver`

- Pour lancer le serveur Livereload :
`./manage.py livereload`

- Les templates sont dans ce repertoire:

`./src/app/templates/`

- Les assets sont ici:

`./src/assets/`


- Le fichier `./src/app/views.py` permet de definir les vues et leur associer des templates.

- Le fichier `./src/app/urls.py` permet de definir les URL et leur associer des vues.


- Apres avoir ajouté un fichier dans le dossier d'asset, il faut executer cette commande :

`./src/manage.py collectstatic -l --noinput`

- Le dossier `./src/static/` est réservé par Django, il ne faut pas mettre de fichiers directement dedans. Django importe les fichier du dossier assets lorsqu'on effectue la commande ci-dessus.

Maj de la DB avec les nouveaux models:
`./manage.py migrate`
