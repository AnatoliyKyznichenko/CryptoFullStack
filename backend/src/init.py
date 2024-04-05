from src.http_client import CoinMarketCupClient
from src.config import settings


coin_market_cup = CoinMarketCupClient(
    base_url='https://pro-api.coinmarketcap.com',
    api_key=settings.CoinMarketCupApiKey
)