import boto3
import boto3.session
import telebot #pip install pyTelegramBotAPI
import time

from botocore.exceptions import NoCredentialsError,PartialCredentialsError

access_key =""
secret_access_key =""
default_region=""
TELEGRAM_BOT_TOKEN =""

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

try:
		session = boto3.session.Session(
		aws_access_key_id=access_key,
		aws_secret_access_key=secret_access_key,
		region_name=default_region,
	)
		cf = session.client('cloudfront')
		paginator =	cf.get_paginator('list_distributions')
		
		for page in paginator.paginate():
			domains =[]		
			for x,dist in enumerate(page['DistributionList']['Items']):
	 			# print(f"{dist['Id']} {dist['Aliases']['Items'][0]}")
				domains.extend([[dist['Aliases']['Items'][0],dist['Id']]])

		@bot.message_handler(commands=['start'])
		def send_welcome(message):
			bot.reply_to(message, "Start using bot to purge distribution's invalidation. Key in '/purge' to select distribution")
			
		@bot.message_handler(commands=['purge']) 
		def domain_handler(message):
			domain = bot.send_message(message.chat.id, "Key in domain name", parse_mode="Markdown")
			bot.register_next_step_handler(domain,purge_handler)

		def purge_handler(domain):
			distribution = domain.text
			distributeId = [distid for distri,distid in domains if distri == distribution]
			
			if distributeId:
				try:
					res = cf.create_invalidation(
						DistributionId=distributeId[0],
						InvalidationBatch={
							'Paths': {
								'Quantity': 1,
								'Items': [
									'/*'
								]
							},
							'CallerReference': str(time.time()).replace(".", "")
						}
				)
					bot.send_message(domain.chat.id,text=f"{domain.text} status: {res['Invalidation']['Status']} at time {res['Invalidation']['CreateTime']}", parse_mode="Markdown")	
				except (
					cf.exceptions.AccessDenied,
					cf.exceptions.MissingBody,
					cf.exceptions.InvalidArgument,
					cf.exceptions.NoSuchDistribution,
					cf.exceptions.BatchTooLarge,
					cf.exceptions.TooManyInvalidationsInProgress,
					cf.exceptions.InconsistentQuantities
				) as e:
					bot.send_message(domain.chat.id,text=f"Error when creating invalidation for {domain.text}: {e}", parse_mode="Markdown")	
				except Exception as e:
					bot.send_message(domain.chat.id,text=f"General error when creating invalidation for {domain.text}: {e}", parse_mode="Markdown")
			else:
				bot.send_message(domain.chat.id,text=f"Domain {domain.text} not found", parse_mode="Markdown")

		bot.infinity_polling()
			
except (NoCredentialsError,PartialCredentialsError) as e:
		print(e)