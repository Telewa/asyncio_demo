import pathlib
import re
from aiohttp import ClientSession
from aiofile import async_open
from structlog import getLogger

logger = getLogger(__name__)


async def download_file(url: str, session: ClientSession) -> str:
    """
    This function will download the provided url

    :param url: str
    :param session: ClientSession
    :return: bytes
    """
    try:
        response = await session.request(method="GET", url=url, timeout=10)
        response.raise_for_status()

        logger.info("Download", action="fetch", status="success", url=url)

        buffer = b""
        async for data, _ in response.content.iter_chunks():
            buffer += data
        return buffer
    except Exception as error:
        logger.info("Download", action="fetch", status="failed", error=str(error), url=url)

        return ""


async def download_and_save(filename: str, url: str, session: ClientSession) -> None:
    logger.info("Download", state="start", url=url, filename=filename)

    # download
    res = await download_file(url=url, session=session)
    if res == "":
        return None

    # save the downloaded file
    async with async_open(f"./downloads/{filename}", "wb") as f:
        await f.write(res)

    logger.info("Download", state="complete", url=url, filename=filename)


def safe_file_name(unsafe_string) -> str:
    path = pathlib.Path(unsafe_string)
    s = re.sub('[^0-9a-zA-Z]+', ' ', path.stem).strip().replace(" ", "-")
    return f"{s}{path.suffix}"
