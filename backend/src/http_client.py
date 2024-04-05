from aiohttp import ClientSession
from async_lru import alru_cache

class HTTPClient:
    def __init__(self, base_url: str, api_key: str):
        self._session = ClientSession(
            base_url=base_url,
            headers={
                'X-CMC_PRO_API_KEY': api_key
            }
        )
        
        
class CoinMarketCupClient(HTTPClient):
    @alru_cache()
    async def get_top_listings(self):
        async with self._session.get('/v1/cryptocurrency/listings/latest') as response:
            result = await response.json()
            return result['data']
        
    @alru_cache()    
    async def get_cryprocurrency(self, currency_id: int):
        async with self._session.get('/v1/cryptocurrency/quotes/latest',
                    params={'id': currency_id}
            ) as response:
            result = await response.json()
            return result['data'][str(currency_id)]
        
        