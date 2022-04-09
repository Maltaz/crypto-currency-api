#!/usr/bin/env python

import logging
import binance
from datetime import datetime
from binance.delivery import Delivery
from binance import Client
from typing import Dict, List, Optional, Any


class SendCryptoCurrencyEmail:
    """Docstring
    Full API documentation is available here: https://python-binance.readthedocs.io/en/latest/
    """

    def __init__(self):

        #CONSTANS
        #TODO usuń to przed wrzuceniem na gita
        self.api_key = ''
        self.api_secret = ''

        #INITIALIZE
        self.binance_client: Optional[binance.client.Client] = None

    def main(self) -> bool:

        return True

    def initialize_binance(self, binance_client_obj: Optional[binance.client.Client] = None) -> bool:
        if binance_client_obj:
            self.binance_client = binance_client_obj
        elif not binance_client_obj:
            self.binance_client = binance.Client(self.api_key, self.api_secret)
        return True

    def get_crypto_info24(self) -> bool:

        print(self.binance_client.get_ticker(symbol='BNBBTC'))
        return True

    def get_wallet_data(self) -> bool:
        self.initialize_binance()
        print(self.binance_client.get_account())
        return True

    def prepare_payload_for_esignatures(self) -> bool:
        """Prepares the dictionary to sends it via e-mail

        :return bool: True if successfully prepared e-mail data
        """

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

