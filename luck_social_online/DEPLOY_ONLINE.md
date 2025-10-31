
# Desplegar Luck Online

## Render (gratis)
1) Sube esta carpeta a un repositorio en GitHub.
2) En Render: New → Web Service → Build from repo o Blueprint (usa `render.yaml` si quieres disco persistente).
3) Render instalará dependencias y arrancará con esta orden:
   `gunicorn -w 2 -k gthread -t 120 -b 0.0.0.0:$PORT app:app`
4) Cuando acabe, te dará una URL pública https://...onrender.com

## Railway
1) Conecta tu repo.
2) Start Command: `gunicorn -w 2 -k gthread -t 120 -b 0.0.0.0:$PORT app:app`
3) Añade `PORT` si lo pide.

## Notas
- Las subidas se guardan en `static/uploads`. Con Render, el blueprint ya monta un **disco persistente** ahí.
- En producción, pon `SECRET_KEY` como variable de entorno.
