# utils/helpers.py
class DatabaseCache:
    def __init__(self):
        # Inizializza il database interno (es. usando un dizionario)
        self.database = {}

    def is_value_present(self, key):
        """
        Verifica se il valore è presente nel database interno.

        Args:
            key (str): Chiave da cercare nel database.

        Returns:
            bool: True se la chiave è presente, False altrimenti.
        """
        return key in self.database

    def get_value(self, key):
        """
        Ottieni il valore associato alla chiave dal database interno.

        Args:
            key (str): Chiave da cercare nel database.

        Returns:
            Any: Valore associato alla chiave, None se la chiave non è presente.
        """
        return self.database.get(key)

    def add_value(self, key, value):
        """
        Aggiungi un valore al database interno.

        Args:
            key (str): Chiave associata al valore.
            value (Any): Valore da aggiungere al database.
        """
        self.database[key] = value