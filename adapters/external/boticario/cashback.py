from adapters.external.boticario.client import get_client


async def get_accumulated_cashback(reseller_cpf: str):
    client = get_client()

    response = await client.get("/v1/cashback", params={"cpf": reseller_cpf})

    response.raise_for_status()

    data = response.json()

    return data["body"]["credit"]
