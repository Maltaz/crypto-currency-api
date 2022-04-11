import smtplib
import datetime as dt
import random


class SendEmail:
    """Docstring
    """

    def __init__(self):
        self.my_email = "sample@gmail.com"
        self.password = "passw"

    def send_mail(self, motivation_massage: str) -> bool:
        """Docstring

        :param motivation_massage
        """

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=self.my_email, password=self.password)
            connection.sendmail(
                from_addr=self.my_email,
                to_addrs="destination_email@gmail.com",
                msg=f"Subject:Your crypto currency news {date}...\n\n {motivation_massage}"
            )

        return True



