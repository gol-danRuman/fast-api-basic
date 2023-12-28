#
# import asyncio
# import httpx
# from nepse import Client
# async def get_high_price(company_symbol: str):
#     # Initializes the client
#     try:
#         client = Client()
#
#         # Gets the data
#         data = await client.security_client.get_company(symbol=company_symbol.upper())
#         print(data)
#         # Prints the highest price for that company today
#         print(data.high_price)
#
#
#         await client.close()
#
#     except Exception as error:
#         print(f"Error while getting high price: {str(error)}")
#
