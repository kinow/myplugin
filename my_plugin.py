from cylc.flow import LOG
from cylc.flow.main_loop import startup

@startup
async def my_startup_coroutine(schd, state):
   # write Hello <suite name> to the Cylc log.
   LOG.info(f'Hello {schd.suite}')

