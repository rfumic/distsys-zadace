import asyncio
import aiohttp
from aiohttp import web

routes = web.RouteTableDef()


@routes.post("/parseActivities")
async def parse_activities(req):
    try:
        data = await req.json()
        async with aiohttp.ClientSession() as session:
            if data["type"] == "charity" or data["type"] == "recreational":
                async with session.post(
                    "http://localhost:8082/charityAndRecreational", json=data
                ) as res:
                    response = await res.json()

            else:
                async with session.post(
                    "http://localhost:8082/otherActivities", json=data
                ) as res:
                    response = await res.json()
        return web.json_response(response)

    except Exception as e:
        return web.json_response({"status": "failed", "message": str(e)})


app = web.Application()

app.router.add_routes(routes)

web.run_app(app, port=8081)
