import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def get_smtp_settings(provider):
		smtp_settings = {
				"GMAIL": {
						"server": "smtp.gmail.com",
						"port": 587,
						"use_tls": True
				},
				"OUTLOOK": {
						"server": "smtp.office365.com",
						"port": 587,
						"use_tls": True
				},
				"YAHOO": {
						"server": "smtp.mail.yahoo.com",
						"port": 587,
						"use_tls": True
				},
				"HOTMAIL": {
						"server": "smtp-mail.outlook.com",
						"port": 587,
						"use_tls": True
				},
				"ZOHO": {
						"server": "smtp.zoho.com",
						"port": 587,
						"use_tls": True
				},
				"AOL": {
						"server": "smtp.aol.com",
						"port": 587,
						"use_tls": True
				},
				"MAIL.COM": {
						"server": "smtp.mail.com",
						"port": 587,
						"use_tls": True
				},
				"PROTONMAIL": {
						"server": "smtp.protonmail.com",
						"port": 587,
						"use_tls": True
				},
				"ICLOUD": {
						"server": "smtp.mail.me.com",
						"port": 587,
						"use_tls": True
				},
				"FASTMAIL": {
						"server": "smtp.fastmail.com",
						"port": 587,
						"use_tls": True
				},
				"YANDEX": {
						"server": "smtp.yandex.com",
						"port": 587,
						"use_tls": True
				},
				"GMX": {
						"server": "smtp.gmx.com",
						"port": 587,
						"use_tls": True
				},
				"SENDINBLUE": {
						"server": "smtp-relay.sendinblue.com",
						"port": 587,
						"use_tls": True
				},
				"MANDRILL": {
						"server": "smtp.mandrillapp.com",
						"port": 587,
						"use_tls": True
				},
				"SENDGRID": {
						"server": "smtp.sendgrid.net",
						"port": 587,
						"use_tls": True
				},
				"ELASTIC EMAIL": {
						"server": "smtp.elasticemail.com",
						"port": 587,
						"use_tls": True
				},
				"MAILGUN": {
						"server": "smtp.mailgun.org",
						"port": 587,
						"use_tls": True
				},
				"AMAZON SES": {
						"server": "email-smtp.us-east-1.amazonaws.com",
						"port": 587,
						"use_tls": True
				},
				"SPARKPOST": {
						"server": "smtp.sparkpostmail.com",
						"port": 587,
						"use_tls": True
				},
				"RUNBOX": {
						"server": "smtp.runbox.com",
						"port": 587,
						"use_tls": True
				},
				"POSTEO": {
						"server": "smtp.posteo.de",
						"port": 587,
						"use_tls": True
				},
				"TUTANOTA": {
						"server": "smtp.tutanota.com",
						"port": 587,
						"use_tls": True
				},
				# Adicione mais provedores conforme necessário
		}
		return smtp_settings.get(provider.upper(), None)

def Sender(objeto):
		try:
				sender_mail = objeto.get("sender_mail") ### Representa o remetente.
				sender_mail_key = objeto.get("sender_mail_key") ### Representa a chave de acesso do remetente.
				recipient_mail = objeto.get("recipient_mail") ### Representa o destinatário para quem deseja enviar o e-mail.
				title = objeto.get("title") ### Representa o titulo do e-mail enviado.
				message = objeto.get("msg") ### Representa a mensagem a ser encaminhada, que será em formato HTML.
				provider = objeto.get("provider") ### Representa o tipo de servidor a sé conectar.
				
				msg = MIMEMultipart()
				msg["From"] = sender_mail
				msg["To"] = recipient_mail
				msg["Subject"] = title
				msg.attach(MIMEText(message, "html"))
				
				msg["Importance"] = "High"
				
				smtp_config = get_smtp_settings(provider)
				
				if smtp_config is None:
						raise ValueError(f"Provedor SMTP '{provider}' não reconhecido.")

				# Conexão com o servidor SMTP
				smtp_server = smtplib.SMTP(smtp_config["server"], smtp_config["port"])
				
				if smtp_config["use_tls"]:
						smtp_server.starttls()
				
				# Autenticação no servidor SMTP
				smtp_server.login(sender_mail, sender_mail_key)
				
				# Envio da mensagem
				smtp_server.sendmail(sender_mail, recipient_mail, msg.as_string())
				
				# Encerramento da conexão SMTP
				smtp_server.quit()
				return "E-mail enviado"
		except Exception as e:
				return str(e)
