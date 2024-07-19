import smtplib
from constants import FROM_EMAIL, PASSWORD, TO_EMAIL


def send_email(current_price: float, url: str):
    subject = "Price Drop!"
    body = (
        "Great news! The price of the item you're watching has dropped below your target price!\n\n"
        + f"Current price is {current_price} zł.\n\n"
        + f"Buy it here: {url}"
    )
    message = f"Subject: {subject}\n\n{body}".encode("utf-8")
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=FROM_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=FROM_EMAIL, to_addrs=TO_EMAIL, msg=message)
