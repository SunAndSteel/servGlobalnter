from django.db import models

class SynchrodbConfig(models.Model):
    """
    Modèle Django représentant une configuration de synchronisation de base de données.

    Ce modèle contient des informations sur des configurations spécifiques,
    identifiées par un nom (`config_name`) et une valeur associée (`config_value`).

    Attributs :
        config_id (int) : Identifiant unique auto-incrémenté pour chaque configuration.
        config_name (str) : Nom de la configuration.
        config_value (str) : Valeur associée à la configuration.

    Meta :
        managed (bool) : Spécifie que Django ne gère pas la table associée à ce modèle.
    """

    # Identifiant unique pour chaque configuration
    config_id = models.AutoField(primary_key=True)

    # Nom de la configuration (par exemple : 'API_URL', 'TIMEOUT')
    config_name = models.CharField(max_length=255)

    # Valeur de la configuration (par exemple : 'https://api.example.com', '30s')
    config_value = models.CharField(max_length=255)

    class Meta:
        """
        Options de métadonnées pour le modèle SynchrodbConfig.

        Attributs :
            managed (bool) : Si `False`, Django ne crée pas, ne modifie pas,
                            et ne supprime pas cette table dans la base de données.
        """
        managed = False  # La table est gérée manuellement en dehors de Django.
