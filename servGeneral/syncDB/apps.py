from django.apps import AppConfig

class SyncdbConfig(AppConfig):
    """
    Configuration de l'application Django 'syncDB'.

    Cette classe configure les paramètres spécifiques à l'application 'syncDB',
    tels que le nom de l'application et le type par défaut des champs auto-incrémentés.

    Attributs :
        default_auto_field (str) : Spécifie le type de champ par défaut utilisé
                                    pour les clés primaires auto-incrémentées.
        name (str) : Le nom de l'application, utilisé par Django pour référencer
                    cette application dans le projet.
    """

    # Type de champ par défaut pour les clés primaires auto-incrémentées
    default_auto_field = 'django.db.models.BigAutoField'

    # Nom de l'application Django
    name = 'syncDB'
