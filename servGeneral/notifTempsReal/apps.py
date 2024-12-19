from django.apps import AppConfig

class NotiftempsrealConfig(AppConfig):
    """
    Configuration de l'application Django 'notifTempsReal'.

    Cette classe permet de configurer les paramètres spécifiques de l'application
    'notifTempsReal'. Elle définit le type de champ par défaut pour les clés
    primaires auto-incrémentées et le nom de l'application.

    Attributs :
        default_auto_field (str) : Type de champ par défaut utilisé pour les clés primaires auto-incrémentées.
        name (str) : Nom de l'application, utilisé pour référencer cette application dans le projet Django.
    """

    # Type de champ par défaut pour les clés primaires auto-incrémentées
    default_auto_field = 'django.db.models.BigAutoField'

    # Nom de l'application
    name = 'notifTempsReal'
