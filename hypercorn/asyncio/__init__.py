import warnings
from typing import Type, Optional

from .run import worker_serve
from ..config import Config
from ..typing import ASGIFramework
from multiprocessing.synchronize import Event as EventType


async def serve(app: Type[ASGIFramework], config: Config,
                shutdown_event: Optional[EventType] = None,
                startup_event: Optional[EventType] = None
                ) -> None:
    """Serve an ASGI framework app given the config.

    This allows for a programmatic way to serve an ASGI framework, it
    can be used via,

    .. code-block:: python

        asyncio.run(serve(app, config))

    It is assumed that the event-loop is configured before calling
    this function, therefore configuration values that relate to loop
    setup or process setup are ignored.

    """
    if config.debug:
        warnings.warn("The config `debug` has no affect when using serve", Warning)
    if config.workers != 1:
        warnings.warn("The config `workers` has no affect when using serve", Warning)
    if config.worker_class != "asyncio":
        warnings.warn("The config `worker_class` has no affect when using serve", Warning)

    await worker_serve(app, config, shutdown_event=shutdown_event, startup_event=startup_event)
