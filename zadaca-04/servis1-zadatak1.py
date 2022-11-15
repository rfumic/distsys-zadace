import asyncio
import aiohttp
from aiohttp import web

routes = web.RouteTableDef()


@routes.get("/getActivity")
async def get_activity(req):
    try:
        async with aiohttp.ClientSession() as session:
            for _ in range(5):
                tasks = []
                for __ in range(8):
                    data = await session.get("https://www.boredapi.com/api/activity")
                    json = await data.json()
                    tasks.append(
                        asyncio.create_task(
                            session.post(
                                "http://localhost:8081/parseActivities", json=json
                            )
                        )
                    )
            response = await asyncio.gather(*tasks)
            response = [await x.json() for x in response]
        return web.json_response(response)
    except Exception as e:
        return web.json_response({"status": "failed", "message": str(e)})


app = web.Application()

app.router.add_routes(routes)

web.run_app(app)
