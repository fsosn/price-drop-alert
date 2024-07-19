# price-drop-alert

## About The Project

This project is an automated Amazon price tracker. It monitors the current price of an item specified in `src/item.json` and sends an email alert if the price drops below a threshold. This project utilises cron job in a Docker container to run the program every hour.

## Built With

- Python
- requests
- BeautifulSoup
- smtplib
- Docker

## Getting Started

This section provides step-by-step instructions on how to set up the project locally.

### Prerequisites

Ensure you have Docker installed on your local machine.

### Installation

1. Clone the repository

   ```sh
   git clone https://github.com/fsosn/price-drop-alert.git
   ```

2. Create a `src/.env` file and set up environmental variables with SMTP details
   ```sh
   FROM_EMAIL=""
   PASSWORD=""
   TO_EMAIL=""
   ```
3. Build an image
   ```sh
   docker build -t price-drop-alert:1.0 .
   ```
4. Run the container
   ```sh
   docker run -d price-drop-alert:1.0
   ```

## Example email alert

```
Subject: Price Drop!

Great news! The price of the item you're watching has dropped below your target price!

Current price is 685.02 zł.

Buy it here: [link]
```
