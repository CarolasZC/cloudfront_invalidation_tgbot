# AWS CloudFront Distribution Invalidation Bot

This project provides a Python-based Telegram bot that facilitates invalidating distributions in AWS CloudFront. Users can interact with the bot to purge cached content for a specified domain.

## Features

- Lists available CloudFront distributions.
- Accepts domain input from the user.
- Invalidates CloudFront distributions by purging the cache (`/*` path).
- Provides error handling for AWS and bot-related exceptions.

## Prerequisites

1. **AWS Account**:
   - An active AWS account with CloudFront configured.
   - AWS credentials with permissions to manage CloudFront distributions.
2. **Telegram Bot**:
   - Create a Telegram bot using [BotFather](https://core.telegram.org/bots#botfather).
   - Obtain the bot token.

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/your-repo/aws-cloudfront-bot.git
   cd aws-cloudfront-bot
   ```

2. Install dependencies:

   ```bash
   pip install boto3 pyTelegramBotAPI
   ```

3. Configure environment:

   - Set up AWS credentials (`aws_access_key_id`, `aws_secret_access_key`, and `region_name`).
   - Add your Telegram bot token in the script:

     ```python
     bot = telebot.TeleBot("TELEGRAM_BOT_TOKEN")
     ```

## Usage

1. **Run the Bot**:

   Execute the script:

   ```bash
   python aws_distribution_invalidation.py
   ```

2. **Interact with the Bot**:

   - Send `/start` to the bot for a welcome message.
   - Send `/purge` to initiate a distribution invalidation.
   - Provide the domain name when prompted by the bot.

3. **Invalidation Process**:

   The bot will:
   - Match the provided domain with the available CloudFront distributions.
   - Invalidate the distribution and notify the user with the invalidation status and creation time.

## Error Handling

The bot includes robust error handling for the following scenarios:

- **AWS Errors**:
  - Access denied
  - Invalid arguments
  - Missing body
  - Too many invalidations in progress
  - Batch too large

- **Bot Errors**:
  - Domain not found
  - General exceptions

## Example Bot Interaction

- **Start Command**:
  ```
  User: /start
  Bot: Start using bot to purge distribution's invalidation. Key in '/purge' to select distribution.
  ```

- **Purge Command**:
  ```
  User: /purge
  Bot: Key in domain name
  User: example.com
  Bot: example.com status: Completed at time 2024-12-27 06:21:18.180000+00:00
  ```

## Notes
- You may use [Screen](https://linuxize.com/post/how-to-use-linux-screen/) to run this python program permanently.
- The bot uses AWS CloudFront's paginator to list all distributions.
- Ensure that the AWS credentials have appropriate permissions to perform invalidations.
- Replace placeholder values (e.g., `TELEGRAM_BOT_TOKEN`) in the script before running.

## Support Me

Any kind of support will be much more appreciated

1. Paypal

```
paypal.com/paypalme/carolas0729
```

1. USDT(TRC20)

```
TVLdZKhfyxHAntX2aAFMwFU18aRQqezYeu
```

2. USDT(ERC20)

```
0x74c6bb39a608648fce3c0666d36ad106c3eb5c3e
```

3. BTC

```
13i4ikHftPaL5pU1DNHKn9WZ5Y83ieNuie
```
## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
