import asyncio
import aiohttp
from aiohttp import web

routes = web.RouteTableDef()

storage = []


async def get_random_user(client):
    async with client.get("https://randomuser.me/api/") as res:
        json = await res.json()
        return json["results"][0]


@routes.post("/otherActivities")
async def other_activities(req):
    try:
        activity = await req.json()
        async with aiohttp.ClientSession() as session:
            user = await get_random_user(session)
            storage.append(
                {
                    "ime": user["name"]["first"],
                    "prezime": user["name"]["last"],
                    "datum_rodenja": user["dob"]["date"],
                    **activity,
                }
            )
        return web.json_response({"status": "success"})

    except Exception as e:
        return web.json_response(
            {
                "status": "Request not successful",
                "message": str(e),
            }
        )


@routes.post("/charityAndRecreational")
async def charity_and_recreational(req):
    try:
        activity = await req.json()
        async with aiohttp.ClientSession() as session:
            user = await get_random_user(session)
            storage.append(
                {
                    **user["location"]["coordinates"],
                    **activity,
                }
            )
        return web.json_response({"status": "success"})

    except Exception as e:
        return web.json_response(
            {
                "status": "Request not successful",
                "error": str(e),
            }
        )


app = web.Application()

app.router.add_routes(routes)

web.run_app(app, port=8082)
