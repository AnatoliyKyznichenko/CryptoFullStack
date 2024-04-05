from fastapi import APIRouter
from src.init import coin_market_cup

router = APIRouter(
    prefix="/currencies"
)


@router.get("")
async def get_cryptocurrencies():
    return await coin_market_cup.get_top_listings()
   
       
@router.get("/{currency_id}")
async def get_cryptocurrency(currency_id: int):
    return await coin_market_cup.get_cryprocurrency(currency_id)