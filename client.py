import requests
import logging

# ---------------------------------------------------------
# Logging konfigurieren
# ---------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

logger = logging.getLogger(__name__)


class JsonServerClient:
    def __init__(self, base_url, timeout=5):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        logger.info(f"Client initialisiert für {self.base_url}")

    # -----------------------------------------------------
    # Hilfsfunktion: Request ausführen + Fehler behandeln
    # -----------------------------------------------------
    def _request(self, method, url, **kwargs):
        try:
            logger.info(f"{method.upper()} {url} | Payload: {kwargs.get('json')}")
            response = requests.request(method, url, timeout=self.timeout, **kwargs)
            response.raise_for_status()
            logger.info(f"Antwort: {response.status_code}")
            return response.json() if response.content else None

        except requests.exceptions.Timeout:
            logger.error("Timeout – Server antwortet nicht")
            raise RuntimeError("Timeout – Server antwortet nicht")

        except requests.exceptions.ConnectionError:
            logger.error("Verbindung fehlgeschlagen – Läuft der JSON‑Server?")
            raise RuntimeError("Verbindung fehlgeschlagen – Läuft der JSON‑Server?")

        except requests.exceptions.HTTPError as e:
            logger.error(f"HTTP Fehler: {e} | Antwort: {response.text}")
            raise RuntimeError(f"HTTP Fehler: {e}")

        except Exception as e:
            logger.error(f"Unerwarteter Fehler: {e}")
            raise RuntimeError(f"Unerwarteter Fehler: {e}")

    # -----------------------------------------------------
    # GET: Alle Einträge
    # -----------------------------------------------------
    def get_all(self, params=None):
        return self._request("get", self.base_url, params=params)

    # -----------------------------------------------------
    # GET: Einzelner Eintrag
    # -----------------------------------------------------
    def get_one(self, item_id):
        url = f"{self.base_url}/{item_id}"
        return self._request("get", url)

    # -----------------------------------------------------
    # POST: Neuer Eintrag
    # -----------------------------------------------------
    def create(self, data):
        return self._request("post", self.base_url, json=data)

    # -----------------------------------------------------
    # PUT: Komplett ersetzen
    # -----------------------------------------------------
    def update_full(self, item_id, data):
        url = f"{self.base_url}/{item_id}"
        return self._request("put", url, json=data)

    # -----------------------------------------------------
    # PATCH: Teilweise ändern
    # -----------------------------------------------------
    def update_partial(self, item_id, data):
        url = f"{self.base_url}/{item_id}"
        return self._request("patch", url, json=data)

    # -----------------------------------------------------
    # DELETE: Eintrag löschen
    # -----------------------------------------------------
    def delete(self, item_id):
        url = f"{self.base_url}/{item_id}"
        self._request("delete", url)
        return {"deleted": item_id}
