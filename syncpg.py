# SPDX-License-Identifier: BlueOak-1.0.0

__version__ = '1.0.0'

import asyncpg
import asyncio

def connect(*args, **kwargs):
	loop = asyncio.get_event_loop()
	return Connection(loop.run_until_complete(asyncpg.connect(*args, **kwargs)), loop=loop)

class _Wrapper:
	def __init__(self, conn, *, loop=None, args=(), kwargs=None):
		self._conn = conn
		self._args = args
		self._kwargs = kwargs or {}
		self.loop = loop or asyncio.get_event_loop()

class Connection(_Wrapper):
	def execute(self, *args, **kwargs):
		return self.loop.run_until_complete(self._conn.execute(*args, **kwargs))

	def executemany(self, *args, **kwargs):
		return self.loop.run_until_complete(self._conn.executemany(*args, **kwargs))

	def fetch(self, *args, **kwargs):
		return self.loop.run_until_complete(self._conn.fetch(*args, **kwargs))

	def fetchrow(self, *args, **kwargs):
		return self.loop.run_until_complete(self._conn.fetchrow(*args, **kwargs))

	def fetchval(self, *args, **kwargs):
		return self.loop.run_until_complete(self._conn.fetchval(*args, **kwargs))

	def copy_from_table(self, *args, **kwargs):
		return self.loop.run_until_complete(self._conn.copy_from_table(*args, **kwargs))

	def cursor(self, *args, **kwargs):
		return Cursor(self._conn, loop=self.loop, args=args, kwargs=kwargs)

	def copy_from_query(self, *args, **kwargs):
		return self.loop.run_until_complete(self._conn.copy_from_query(*args, **kwargs))

	def copy_to_table(self, *args, **kwargs):
		return self.loop.run_until_complete(self._conn.copy_to_table(*args, **kwargs))

	def copy_records_to_table(self, *args, **kwargs):
		return self.loop.run_until_complete(self._conn.copy_records_to_table(*args, **kwargs))

	def set_type_codec(self, *args, **kwargs):
		self.loop.run_until_complete(self._conn.set_type_codec(*args, **kwargs))

	def reset_type_codec(self, *args, **kwargs):
		self.loop.run_until_complete(self._conn.reset_type_codec(*args, **kwargs))

	def set_builtin_type_codec(self, *args, **kwargs):
		self.loop.run_until_complete(self._conn.set_builtin_type_codec(*args, **kwargs))

	def is_closed(self):
		return self._conn.is_closed()

	def close(self):
		self.loop.run_until_complete(self._conn.close())

	def transaction(self, **kwargs):
		return Transaction(self._conn, loop=self.loop, kwargs=kwargs)

	def is_in_transaction(self):
		return self._conn.is_in_transaction()

	def terminate(self):
		self._conn.terminate()

	def reset(self, **kwargs):
		self.loop.run_until_complete(self._conn.reset(**kwargs))

class Transaction(_Wrapper):
	def __enter__(self):
		self._tx = self._conn.transaction(**self._kwargs)
		return self.loop.run_until_complete(self._tx.__aenter__())

	def __exit__(self, *excinfo):
		return self.loop.run_until_complete(self._tx.__aexit__(*excinfo))

class Cursor(_Wrapper):
	def __iter__(self):
		cur_factory = self._conn.cursor(*self._args, **self._kwargs)
		self._cur = self.loop.run_until_complete(cur_factory)
		self._it = cur_factory.__aiter__()
		return self

	def __next__(self):
		try:
			return self.loop.run_until_complete(self._it.__anext__())
		except StopAsyncIteration:
			raise StopIteration

	def fetch(self, *args, **kwargs):
		return self.loop.run_until_complete(self._cur.fetch(*args, **kwargs))

	def fetchrow(self, *args, **kwargs):
		return self.loop.run_until_complete(self._cur.fetchrow(*args, **kwargs))

	def forward(self, *args, **kwargs):
		return self.loop.run_until_complete(self._cur.forward(*args, **kwargs))

	def __del__(self):
		self._it.__del__()
