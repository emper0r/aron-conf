# File dei codice per i messaggi
# 1xx - Info
# 2xx - Domande
# 3xx - Risposta
# 4xx - Azioni interne


def msg(code=None):
    text = ''
    if code == 100:
        text = 'Configurazione aggiornata'
    if code == 101:
        text = 'I files con estensione supportati sono: BMP, JPG o PNG'
    if code == 102:
        text = 'Inserito campo nel database '
    if code == 103:
        text = 'Inserito Hardware '
    if code == 104:
        text = 'Password modificata'
    if code == 105:
        text = 'Cliente inserito '
    if code == 106:
        text = 'Inserita configurazione'
    if code == 107:
        text = 'Cancellata righa configurazione cliente '
    if code == 108:
        text = 'Cancellato cliente '
    if code == 109:
        text = 'Cancellato Item '
    if code == 110:
        text = 'Cancellato Hardware '
    if code == 111:
        text = 'Visualizzazione immagine '
    if code == 112:
        text = 'Salvata immagine '
    if code == 113:
        text = 'Cancellata immagine '
    if code == 114:
        text = 'Il campo "utente" o "password" non possono essere vuoti'
    if code == 115:
        text = 'Accesso al sistema Aron-Conf'
    if code == 116:
        text = 'Campo inserito '
    if code == 117:
        text = 'I files con estensione supportati sono: TXT, RTF, XLS, XLSX, CONF, DAT, DOC, DOCX, XLSX, PDF, XML e SQL'
    if code == 201:
        text = 'Sicuro di cancellare questa informazione '
    if code == 202:
        text = 'Sicuro che vuole cancellare con tutte le informazione all\'interno del Cliente: '
    if code == 203:
        text = 'Sicuro che vuole cancellare il file del Cliente: '
    if code == 204:
        text = 'Sicuro che vuole cancellare l\'immagine del Cliente: '
    if code == 301:
        text = 'Devi selezionare prima un cliente o crearne uno nuovo'
    if code == 302:
        text = 'Scegliere un cliente e filtri per poter aggiungere'
    if code == 303:
        text = 'Devi selezionare prima una riga nella tabella'
    if code == 304:
        text = 'Devi selezionare prima un item nel filtro'
    if code == 305:
        text = 'Devi selezionare prima un hardware nel filtro'
    if code == 306:
        text = 'Devi scegliere prima una foto della tabella'
    if code == 307:
        text = 'Questi valori non possono essere duplicati nel database'
    if code == 308:
        text = 'Questo campo non puo\' essere vuoto'
    if code == 309:
        text = 'Deve riempire tutti campi'
    if code == 310:
        text = 'Le password non sono uguali ...'
    if code == 311:
        text = 'Questo non e\' un indirizzo IP valido'
    if code == 401:
        text = 'Errore nella connessione col database'
    if code == 402:
        text = 'Uscita della applicazione'
    if code == 404:
        text = 'Tentativo di accesso erroneo '
    if code == 405:
        text = 'Loggato come: '
    if code == 406:
        text = 'Caricato file: '
    if code == 407:
        text = 'Visualizzato file: '
    if code == 408:
        text = 'Cancellato file: '
    if code == 409:
        text = 'Scaricato file: '
    if code == 410:
        text = 'Modificato configurazione TXT: '
    if code == 411:
        text = 'Aggiornata/Modificata/Vista impostazion database'
    if code == 500:
        text = 'Generato file di configurazione PDF '
    return text
