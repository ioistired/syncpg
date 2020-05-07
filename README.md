# syncpg

A synchronous wrapper for [asyncpg](https://pypi.org/project/asyncpg/).

It has the exact same API as asyncpg except wihtout functionality that only makes sense in an asynchronous context.
Currently this means connection pools and any kind of listeners.
See the asyncpg docs for usage.

## License

BlueOak Model License 1.0.0. See LICENSE.md or <https://blueoakcouncil.org/license/1.0.0>.
