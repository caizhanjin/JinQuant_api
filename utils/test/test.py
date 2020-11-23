import asyncio


class AsyncContextManager:
    def __init__(self):
        self.conn = None

    async def do_something(self):
        # 异步操作数据库
        return 666

    async def __aenter__(self):
        print(123)
        # 异步链接数据库
        self.conn = await asyncio.sleep(1)
        return self

    async def __aexit__(self, exc_type, exc, tb):
        print(456)
        # 异步关闭数据库链接
        await asyncio.sleep(1)


async def func():
    async with AsyncContextManager() as f:
        result = await f.do_something()
        print(result)




if __name__ == '__main__':
    asyncio.run(func())