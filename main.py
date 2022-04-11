#!/usr/bin/env python

import logging
import binance
import email_sender
from datetime import datetime
from binance import Client
from typing import Dict, List, Optional, Any


class SendCryptoCurrencyEmail:
    """An SDK for working with binance API and sending email with your current crypto details.
    Full API documentation is available here: https://python-binance.readthedocs.io/en/latest/
    """

    def __init__(self):

        #CONSTANS
        #TODO usuń to przed wrzuceniem na gita
        self.api_key = ''
        self.api_secret = ''

        #INITIALIZE
        self.binance_client: Optional[binance.client.Client] = None

        #GET
        self.wallet_crypto_details: Optional[List[dict]] = []
        self.wallet_crypto_change24: Optional[List[dict]] = []

        #PREPARE
        #self.sosa

    def main(self) -> bool:
        if not self.prepare_payload_for_email():
            print("Failed to prepare email data! Exiting...")
        elif not self.send_crypto_news_email():
            print("Failed to send email! Exiting...")
        else:
            return True
        return False

    def initialize_binance(self, binance_client_obj: Optional[binance.client.Client] = None) -> bool:
        if binance_client_obj:
            self.binance_client = binance_client_obj
        elif not binance_client_obj:
            self.binance_client = binance.Client(self.api_key, self.api_secret)
        return True

    def get_wallet_data(self) -> bool:
        self.initialize_binance()
        for crypto_dict in self.binance_client.get_account().get('balances', []):
            if float(crypto_dict.get('free', '0')) > 0 or float(crypto_dict.get('locked', '0')) > 0:
                self.wallet_crypto_details.append(crypto_dict)
        print(self.wallet_crypto_details)
        return True

    def get_crypto_info24(self) -> bool:
        self.get_wallet_data()
        for crypto in self.wallet_crypto_details:
            if crypto.get("asset", "BTC") == 'BUSD':
                self.wallet_crypto_change24.append(self.binance_client.get_ticker(symbol=crypto.get("asset", "BUSD") + 'USDT'))
            else:
                self.wallet_crypto_change24.append(self.binance_client.get_ticker(symbol=crypto.get("asset", "BTC") + 'USDC'))
        print(self.wallet_crypto_change24)
        return True

    def prepare_payload_for_email(self) -> bool:
        """Prepares the message to sends it via e-mail

        :return bool: True if successfully prepared e-mail data
        """
        self.get_crypto_info24()

        return True

    def send_crypto_news_email(self) -> bool:
        """Docstring

        :return: bool: True if successfully send e-mail
        """
        with open("email.txt", "r") as file:
            email_list = file.readlines()
        send_obj = email_sender.SendEmail()
        send_obj.send_mail(motivation_massage=massage)

        return True

    @staticmethod
    def get_current_date() -> str:
        """Prepares the current date in the following format: Month day, year
        For example: "January 31, 2022", "May 3, 2000"

        :return str:  today's date formatted
        """
        try:
            return datetime.now().strftime('%B %-d, %Y')
        except ValueError:  # Previous convention for Linux, following convention for Windows
            return datetime.now().strftime('%B %#d, %Y')


cos = SendCryptoCurrencyEmail()
cos.get_wallet_data()
cos.get_crypto_info24()
