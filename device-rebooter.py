import asyncio
import traceback

from lib.settings import Settings, get_logger
from lib.spark_asyncio import Spark

spark = Spark(Settings.bot_token)
logger = get_logger(__name__)

products = []
#products = ['Cisco Room Navigator']

async def main():
    try:
        url = "https://webexapis.com/v1/devices"
        while url:
            res, resp = await spark.get(url, return_object=True)
            for device in res["items"]:
                try:
                    #logger.debug(device)
                    logger.debug("{0}, {1}, {2}, {3}".format(device["displayName"], device["product"], device["connectionStatus"], device["ip"]))
                    if len(products) == 0 or device["product"] in products:
                        if device["connectionStatus"] != "disconnected":
                            if 'xapi' in device["capabilities"]:
                                logger.info("Rebooting device: {0}, {1}, {2}".format(device["displayName"], device["product"], device["ip"]))
                                data = {"deviceId":device["id"], "arguments": {"Action":"Restart", "Force":"True"} }
                                res = await spark.post("https://webexapis.com/v1/xapi/command/SystemUnit.Boot", data)
                            else:
                                logger.warning("Device is not xAPI enabled (try standalone mode): {0}, {1}, {2} - NOT rebooting.".format(device["displayName"], device["product"], device["ip"]))
                        else:
                            logger.warning("Device is offline: {0}, {1}, {2} - NOT rebooting.".format(device["displayName"], device["product"], device["ip"]))
                except Exception as ex:
                    traceback.print_exc()
            url = resp.headers.get("Link")
            if url:
                url = url[1:].split(">;")[0]
                logger.debug('next url: {0}'.format(url))
        logger.debug("completed")
    except Exception as e:
        traceback.print_exc()

asyncio.run(main())

